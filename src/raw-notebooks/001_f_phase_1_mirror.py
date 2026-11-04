#!/usr/bin/env python
# coding: utf-8

# # Phase 1 — Familiarise with the data and assess its suitability
# 
# **FUUCCE · P1.01–P1.18 · implementation ready; empirical assessment pending.**
# 
# This notebook assesses whether the ERP extracts can support the thesis investigation:
# ordering activity, recorded net order value and assortment over an explicit 24-month window.
# It prepares recommendations for Phase 2; it does not detect changes or establish taxonomy types.
# The four research contributions are detection, taxonomy, automatic assignment and evidence-based descriptions.
# 
# Authoritative references: [project plan](../../docs/project/bachelor_thesis_project_plan.md),
# [FUUCCE Phase 1](../../docs/framework/fuucce_framework.md#phase-1---familiarise-yourself-with-the-data-and-assess-its-suitability),
# [data description](../../docs/project/data_description.md), [backlog](../../BACKLOG.md).
# 
# ## Run instructions
# 
# 1. Select the project Python kernel. Launch Jupyter from the repository root with
#    `PYTHONPATH="$PWD/src" uv run --locked jupyter lab`; editor kernels also need `src` on their import path.
# 2. Review the settings and extraction register below. Run structural assessment first.
# 3. Before behavioural exploration, define the 24-month bounds, confirm extraction coverage, reason-code
#    treatment and the evidence-use plan. All date intervals use **start inclusive, end exclusive**.
# 4. Restart the kernel and Run All after changing inputs/settings. The default empty extracts yield
#    diagnostics and pending decisions, with no invented findings. Synthetic verification uses only invented records.
# 5. Review the findings/decision register and completion checklist. Enable exports explicitly when ready.
# 
# For user-managed production execution, copy this notebook to the private notebook directory and change
# the explicit configuration import to `config.production`. The declared filenames/schemas must also
# match your extracts; update `SOURCES` and the parsing contract explicitly in the private copy if needed.
# Keep production outputs in that private
# copy and its configured output directories. Agents do not access production inputs or execute that copy.
# Raw extracts and read-only Python mirrors are never modified.
# 
# ## Contents
# 
# 1. Configuration and extraction register
# 2. Data assessment
# 3. Evidence-use record
# 4. Customer histories and focused exploration
# 5. Preparation decisions, blockers and Phase 2 handover
# 6. Synthetic verification, reproducibility and optional exports
# 

# In[ ]:


# Explicit public default. In a user-managed private copy, select config.production instead.
# CONFIG roots derive from the repository location, not the kernel's working directory.
from config.example import CONFIG

from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import json
import platform
import importlib.metadata
import re

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import duckdb
import matplotlib.pyplot as plt
from IPython.display import display, Markdown


# In[ ]:


SOURCES = {
    "orders": {"file": "001_order_header_pos_data_eg.parquet", "entity": "order item with repeated order header",
        "columns": "SALESORDER SALESORDERTYPE OVERALLSDPROCESSSTATUS SDDOCUMENTREASON OVERALLSDDOCUMENTREJECTIONSTS SALESORDERDATE SOLDTOPARTY TOTALNETAMOUNT TRANSACTIONCURRENCY SALESORDERITEM MATERIAL CONFDDELIVQTYINORDERQTYUNIT".split(),
        "key": ["SALESORDER", "SALESORDERITEM"]},
    "products": {"file": "002_product_master_data_eg.parquet", "entity": "product master candidate",
        "columns": "PRODUCT PRODUCTGROUP TO_PLANT_BASEUNIT TO_PRODUCTBASICTEXT_LONGTEXT".split(), "key": ["PRODUCT"]},
    "prices": {"file": "003_product_price_data_eg.parquet", "entity": "price condition with validity and customer scope",
        "columns": "MATERIAL CONDITIONVALIDITYSTARTDATE CONDITIONVALIDITYENDDATE CUSTOMERPRICEGROUP CUSTOMER CONDITIONTYPE CONDITIONRATEVALUE CONDITIONRATEVALUEUNIT".split(),
        "key": "MATERIAL CONDITIONVALIDITYSTARTDATE CONDITIONVALIDITYENDDATE CUSTOMERPRICEGROUP CUSTOMER CONDITIONTYPE".split()},
    "customers": {"file": "004_customer_master_data_eg.parquet", "entity": "customer master candidate",
        "columns": "CUSTOMER CUSTOMERFULLNAME POSTALCODE INDUSTRY CUSTOMERPRICEGROUP".split(), "key": ["CUSTOMER"]},
    "reasons": {"file": "005_order_sddocumentreason_mapping_eg.parquet", "entity": "order reason lookup",
        "columns": ["SDDOCUMENTREASON", "SDDOCUMENTREASONTEXT"], "key": ["SDDOCUMENTREASON"]},
    "groups": {"file": "006_product_productgroup_mapping_eg.parquet", "entity": "product group lookup",
        "columns": ["PRODUCTGROUP", "PRODUCTGROUPTEXT"], "key": ["PRODUCTGROUP"]},
    "conditions": {"file": "007_product_conditiontype_mapping_eg.parquet", "entity": "condition type lookup",
        "columns": ["CONDITIONTYPE", "CONDITIONTYPETEXT"], "key": ["CONDITIONTYPE"]},
    "industries": {"file": "008_customer_industry_mapping_eg.parquet", "entity": "industry lookup",
        "columns": ["INDUSTRY", "INDUSTRYTEXT"], "key": ["INDUSTRY"]},
}
DATE_COLUMNS = {"SALESORDERDATE", "CONDITIONVALIDITYSTARTDATE", "CONDITIONVALIDITYENDDATE"}
NUMBER_COLUMNS = {"TOTALNETAMOUNT", "CONFDDELIVQTYINORDERQTYUNIT", "CONDITIONRATEVALUE"}
ID_COLUMNS = {"SALESORDER", "SALESORDERITEM", "SOLDTOPARTY", "MATERIAL", "PRODUCT", "CUSTOMER", "POSTALCODE",
              "PRODUCTGROUP", "CUSTOMERPRICEGROUP", "SDDOCUMENTREASON", "CONDITIONTYPE", "INDUSTRY"}
HEADER_COLUMNS = SOURCES["orders"]["columns"][:9]
CORE_MEASURES = ["ORDERCOUNT", "TOTALORDERVALUE", "AVGORDERVALUE", "DISTINCTPRODUCTCOUNT", "DISTINCTPRODUCTGROUPCOUNT"]
# Explicit parsing contract: change only after checking the extraction specification.
DATE_FORMAT = "%Y-%m-%d"
DECIMAL_MARK = "."  # use ',' only when documented; thousands separators are not guessed
MISSING_TOKENS = {"", "NULL", "null", "N/A", "NA"}  # review: a token can also be a legitimate ERP code


# ## 1. Configuration and extraction register · P1.01–P1.03
# 
# The schema documents meaning; it does not establish extraction completeness, key uniqueness or actual
# formats. The empty Parquet files currently store fields as strings. Numeric/date parsing is explicit
# and failed conversions are counted. Identifier strings retain leading zeros; zeros already lost in a
# numeric extract cannot be reconstructed. Trimming whitespace and recognising missing tokens are
# **provisional preparation choices** recorded below, not modifications to raw sources.
# 
# Fill the extraction register from the extraction process, not from first/last observed orders.
# The order-date coverage intervals must describe the completeness of the **eligible order universe**,
# including extract filters and customer coverage. If coverage differs by customer, leave global coverage
# empty and extend the coverage specification before asserting inactivity. No order rows is not evidence
# of no purchasing. Product/customer masters may be snapshots rather than historical states.
# 

# In[ ]:


# All values below are user-editable inputs. None means unresolved, not inferred.
OBSERVATION_START = None       # e.g. "2024-01-01"; the end must equal start + 24 months
OBSERVATION_END = None         # exclusive, e.g. "2026-01-01"
ORDER_COVERAGE = []            # verified complete [start, end) intervals only
EXTRACTION = {name: {"EXTRACTEDAT": None, "FILTERS": None, "COVERAGE": None,
                     "SOURCEVERSION": None, "NOTES": None} for name in SOURCES}

ANALYSIS_CURRENCY = None       # explicit restriction, e.g. "EUR"; no automatic FX conversion
ACCEPTED_REASON_CODES = None  # explicit set of verified eligible reason IDs; no guessed cancellation codes
INCLUDE_PARTIAL_REJECTIONS = False  # provisional sensitivity alternative; net amount meaning unresolved
ELIGIBILITY_RULES_CONFIRMED = False
IDENTIFIER_SEMANTICS_CONFIRMED = False

# Customer-level separation is the starting design. Freeze before behavioural exploration.
SPLIT_SALT = "fuucce-phase1-v1"
EVALUATION_FRACTION = 0.20     # proposal, not a plan-mandated sample size
PRIOR_EXPOSURE = {}           # customer ID -> exposure description; exposed IDs are development only
PRIOR_EXPOSURE_REVIEWED = False
EVIDENCE_PLAN_CONFIRMED = False
# Prevent silent re-splitting. A confirmed analysis always freezes this file before exploration.
EVIDENCE_FILE = CONFIG.data_dir / "interim" / "p1_evidence_manifest.parquet"

# Enter findings and recommendations after reviewing the generated evidence.
# Each record: TOPIC, STATUS (adopted_for_exploration/proposed_for_preparation/unresolved),
# EVIDENCE (output/table reference), DECISION, RATIONALE, NEXTACTION.
REVIEWED_DECISIONS = []
EMPIRICAL_REVIEW_COMPLETE = False
EXPORT_ARTIFACTS = False      # general outputs opt in; confirmed analysis always freezes its evidence manifest
FIGURE_DIR = CONFIG.output_dir / "phase_1" / "figures"
TABLE_DIR = CONFIG.output_dir / "phase_1" / "tables"
PROFILE_DIR = CONFIG.data_dir / "interim"


# In[ ]:


def normalise_table(frame, table_name):
    """Return a typed copy and per-field audit; raw extracts remain unchanged."""
    spec = SOURCES[table_name]
    typed = frame.copy()
    audit = []
    for column in spec["columns"]:
        missing_column = column not in frame.columns
        raw = frame[column] if not missing_column else pd.Series(pd.NA, index=frame.index, dtype="string")
        text = raw.astype("string").str.strip()
        missing = text.isna() | text.isin(MISSING_TOKENS)
        text = text.mask(missing)
        failures = 0
        if column in DATE_COLUMNS:
            parsed = pd.to_datetime(text, format=DATE_FORMAT, errors="coerce")
            failures = int((text.notna() & parsed.isna()).sum())
        elif column in NUMBER_COLUMNS:
            if DECIMAL_MARK not in {".", ","}:
                raise ValueError("DECIMAL_MARK must be '.' or ','; no inferred thousands separator")
            numeric = text.str.replace(",", ".", regex=False) if DECIMAL_MARK == "," else text
            valid = numeric.str.fullmatch(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?", na=False)
            parsed = pd.to_numeric(numeric.where(valid), errors="coerce").astype("Float64")
            parsed = parsed.where(np.isfinite(parsed))
            failures = int((text.notna() & parsed.isna()).sum())
        else:
            parsed = text
        typed[column] = parsed
        audit.append({"TABLE": table_name, "COLUMN": column, "RAWDTYPE": str(raw.dtype),
                      "TYPEDDTYPE": str(parsed.dtype), "MISSINGCOLUMN": missing_column,
                      "MISSINGVALUES": int(missing.sum()), "PARSEFAILURES": failures,
                      "WHITESPACEROWS": int((raw.astype("string") != raw.astype("string").str.strip()).fillna(False).sum()),
                      "NUMERICIDENTIFIERRISK": column in ID_COLUMNS and pd.api.types.is_numeric_dtype(raw.dtype),
                      "LEADINGZEROROWS": int(text.str.match(r"^0[0-9]+$", na=False).sum())})
    return typed, pd.DataFrame(audit)


def load_sources(data_dir):
    """Load exactly the declared immediate Parquet files; no recursive traversal."""
    tables, audits, files = {}, [], []
    raw_dir = data_dir / "raw"
    if raw_dir.is_symlink():
        raise ValueError("Raw source directory must not be a symlink")
    for name, spec in SOURCES.items():
        path = raw_dir / spec["file"]
        if path.is_symlink():
            raise ValueError(f"Symlink source refused: {spec['file']}")
        exists = path.is_file()
        frame = pd.read_parquet(path) if exists else pd.DataFrame()
        typed, audit = normalise_table(frame, name)
        tables[name] = typed
        audits.append(audit)
        # Hash the source bytes for reproducibility without exposing records in the run log.
        digest = None
        if exists:
            with path.open("rb") as stream:
                digest = hashlib.file_digest(stream,"sha256").hexdigest()
        files.append({"TABLE": name, "FILE": spec["file"], "PRESENT": exists,
                      "SHA256": digest, "BYTES": path.stat().st_size if exists else None,
                      "EXTRACOLUMNS": ",".join(sorted(set(frame.columns) - set(spec["columns"])))})
    return tables, pd.concat(audits, ignore_index=True), pd.DataFrame(files)


def structural_assessment(tables):
    inventory, keys, relationships, values, dates = [], [], [], [], []
    for name, spec in SOURCES.items():
        df = tables[name]
        key = spec["key"]
        inventory.append({"TABLE": name, "ENTITY": spec["entity"], "ROWS": len(df), "COLUMNS": len(df.columns),
                          "KNOWLEDGE": "observed structure; entity meaning documented"})
        keys.append({"TABLE": name, "CANDIDATEKEY": "+".join(key),
                     "MISSINGKEYROWS": int(df[key].isna().any(axis=1).sum()),
                     "DUPLICATEROWS": int(df.duplicated(key, keep=False).sum()),
                     "EXACTDUPLICATEROWS": int(df.duplicated(keep=False).sum())})
        for column in df.columns:
            if column in DATE_COLUMNS:
                dates.append({"TABLE": name, "COLUMN": column, "OBSERVEDMIN": df[column].min(),
                              "OBSERVEDMAX": df[column].max(), "MISSING": int(df[column].isna().sum()),
                              "INTERPRETATION": "Observed dates do not prove extraction coverage"})
        categorical = {"orders": ["SALESORDERTYPE", "OVERALLSDPROCESSSTATUS", "OVERALLSDDOCUMENTREJECTIONSTS", "SDDOCUMENTREASON", "TRANSACTIONCURRENCY"],
                       "products": ["TO_PLANT_BASEUNIT", "PRODUCTGROUP"], "prices": ["CONDITIONTYPE", "CONDITIONRATEVALUEUNIT"]}.get(name, [])
        known = {"SALESORDERTYPE": {"OR"}, "OVERALLSDPROCESSSTATUS": {"A", "B", "C"},
                 "OVERALLSDDOCUMENTREJECTIONSTS": {"A", "B", "C"}, "TRANSACTIONCURRENCY": {"EUR", "GBP"},
                 "TO_PLANT_BASEUNIT": {"M", "PC", "ROL", "ZBU"}, "CONDITIONRATEVALUEUNIT": {"EUR"}}
        for column in categorical:
            for value, count in df[column].value_counts(dropna=False).items():
                values.append({"TABLE": name, "COLUMN": column, "VALUE": str(value) if pd.notna(value) else None,
                               "ROWS": int(count), "FLAG": "missing" if pd.isna(value) else
                               ("not_in_documented_codes" if column in known and value not in known[column] else "inspect_mapping_or_documented_code")})
    links = [("orders","MATERIAL","products","PRODUCT"), ("orders","SOLDTOPARTY","customers","CUSTOMER"),
             ("orders","SDDOCUMENTREASON","reasons","SDDOCUMENTREASON"), ("products","PRODUCTGROUP","groups","PRODUCTGROUP"),
             ("prices","MATERIAL","products","PRODUCT"), ("prices","CUSTOMER","customers","CUSTOMER"),
             ("prices","CONDITIONTYPE","conditions","CONDITIONTYPE"), ("customers","INDUSTRY","industries","INDUSTRY")]
    for source, left, target, right in links:
        a, b = tables[source][left], tables[target][right]
        matched = a.notna() & a.isin(b.dropna())
        relationships.append({"SOURCE": source, "FIELD": left, "TARGET": target, "TARGETFIELD": right,
                              "SOURCEROWS": len(a), "MISSINGKEYROWS": int(a.isna().sum()),
                              "UNMATCHEDNONNULLROWS": int((a.notna() & ~matched).sum()),
                              "MATCHEDROWS": int(matched.sum()), "TARGETKEYUNIQUE": not b.duplicated().any() and b.notna().all(),
                              "NOTE": "No join executed; blank price CUSTOMER can indicate group/general scope, not necessarily an error"})
    return {"inventory": pd.DataFrame(inventory), "keys": pd.DataFrame(keys),
            "relationships": pd.DataFrame(relationships),
            "codes": pd.DataFrame(values, columns=["TABLE","COLUMN","VALUE","ROWS","FLAG"]),
            "dates": pd.DataFrame(dates, columns=["TABLE","COLUMN","OBSERVEDMIN","OBSERVEDMAX","MISSING","INTERPRETATION"])}


def order_views(orders):
    """Retain one header per order, flag conflicts; never sum repeated header amounts."""
    rows = orders.drop_duplicates().copy()
    if rows.empty:
        headers = rows[HEADER_COLUMNS].assign(HEADERVALID=pd.Series(dtype=bool), HEADERISSUES=pd.Series(dtype="string"))
        return {"headers": headers, "items": rows.assign(ITEMCONFLICT=pd.Series(dtype=bool)),
                "audit": pd.DataFrame(columns=["SALESORDER","HEADERVALID","HEADERISSUES"])}
    # Missing header versus a value is itself a conflict, not silently filled from another item.
    inconsistent = rows.groupby("SALESORDER", dropna=False)[HEADER_COLUMNS[1:]].nunique(dropna=False).gt(1)
    bad_ids = inconsistent.index[inconsistent.any(axis=1)]
    headers = rows[HEADER_COLUMNS].drop_duplicates("SALESORDER").copy()
    issues = []
    for _, row in headers.iterrows():
        reasons = []
        if pd.isna(row["SALESORDER"]): reasons.append("missing_order_id")
        if pd.isna(row["SOLDTOPARTY"]): reasons.append("missing_customer")
        if pd.isna(row["SALESORDERDATE"]): reasons.append("missing_or_invalid_date")
        if row["SALESORDER"] in bad_ids: reasons.append("conflicting_header")
        issues.append(";".join(reasons))
    headers["HEADERISSUES"] = pd.Series(issues, index=headers.index, dtype="string")
    headers["HEADERVALID"] = headers["HEADERISSUES"].eq("")
    itemkey = ["SALESORDER", "SALESORDERITEM"]
    rows["ITEMCONFLICT"] = rows.duplicated(itemkey, keep=False) | rows[itemkey].isna().any(axis=1)
    return {"headers": headers.reset_index(drop=True), "items": rows.reset_index(drop=True),
            "audit": headers[["SALESORDER","HEADERVALID","HEADERISSUES"]].reset_index(drop=True)}


# ## 2. Data assessment · P1.03–P1.06
# 
# The following checks may cover all extracts because they establish structural properties.
# Code frequencies count item rows (repeated headers included), not distinct orders. Exact duplicate
# rows are removed only in provisional views; candidate-key conflicts remain flagged. Unresolved order
# attribution/eligibility blocks behavioural analysis until corrected, rather than creating false empty periods. Price-condition
# keys are candidates, not proven business keys. Joins are assessed before execution to avoid row inflation.
# 
# A missing amount does not erase an otherwise valid order count. Conflicting headers are quarantined
# from provisional profiles. Ambiguous/missing item keys prevent complete assortment measures.
# Unknown statuses, negative/zero values and unmatched keys are investigation flags; they are not
# silently deleted from the assessment or declared invalid business transactions.
# 

# In[ ]:


tables, field_audit, source_files = load_sources(CONFIG.data_dir)
structure = structural_assessment(tables)
views = order_views(tables["orders"])
extraction_register = pd.DataFrame([{"TABLE": name, **metadata, "KNOWLEDGE": "user-supplied; unresolved when blank"}
                                    for name, metadata in EXTRACTION.items()])
display(source_files, extraction_register, structure["inventory"], field_audit,
        structure["keys"], structure["relationships"], structure["dates"], structure["codes"])
display(views["audit"].groupby(["HEADERVALID","HEADERISSUES"], dropna=False).size().rename("ORDERS").reset_index())
value_flags = pd.DataFrame([
    {"CHECK": "negative_order_amount_rows", "FLAGGEDROWS": int(tables["orders"]["TOTALNETAMOUNT"].lt(0).sum())},
    {"CHECK": "zero_order_amount_rows", "FLAGGEDROWS": int(tables["orders"]["TOTALNETAMOUNT"].eq(0).sum())},
    {"CHECK": "nonpositive_confirmed_quantity_rows", "FLAGGEDROWS": int(tables["orders"]["CONFDDELIVQTYINORDERQTYUNIT"].le(0).sum())},
    {"CHECK": "conflicting_or_missing_item_key_rows", "FLAGGEDROWS": int(views["items"]["ITEMCONFLICT"].sum())},
])
display(value_flags)
observed_dates = views["headers"]["SALESORDERDATE"].dropna()
extraction_timeline = pd.DataFrame(columns=["PERIODSTART","OBSERVEDORDERS","INTERPRETATION"])
if not observed_dates.empty:
    observed_months = observed_dates.dt.to_period("M").value_counts().sort_index()
    grid = pd.period_range(observed_months.index.min(),observed_months.index.max(),freq="M")
    extraction_timeline = pd.DataFrame({"PERIODSTART":grid.to_timestamp(),
        "OBSERVEDORDERS":observed_months.reindex(grid,fill_value=0).to_numpy(),
        "INTERPRETATION":"Structural record counts only; apparent gaps require extraction-process verification"})
    display(extraction_timeline)
print("Observed order span is not verified coverage. Review extraction metadata and apparent gaps with the extractor.")


# ### Optional discount feasibility · P1.O1
# 
# This is a diagnostic screen, not item-price assignment or a discount measure. A condition table alone
# cannot establish the actual after-discount price. The `999999` sentinel is unmaintained, not zero.
# A valid condition needs documented type semantics, date applicability, customer/group precedence,
# compatible units and enough price/quantity information. Overlapping validity and specificity require
# clarification before integration. Do not sum metres, pieces, rolls and bundles.
# 

# In[ ]:


prices = tables["prices"]
price_diagnostics = pd.DataFrame([
    {"CHECK": "unmaintained_price_sentinel", "ROWS": int(prices["CONDITIONRATEVALUE"].eq(999999).sum())},
    {"CHECK": "missing_or_unparseable_rate", "ROWS": int(prices["CONDITIONRATEVALUE"].isna().sum())},
    {"CHECK": "zero_rate_requires_condition_semantics", "ROWS": int(prices["CONDITIONRATEVALUE"].eq(0).sum())},
    {"CHECK": "invalid_validity_order", "ROWS": int((prices["CONDITIONVALIDITYSTARTDATE"] > prices["CONDITIONVALIDITYENDDATE"]).sum())},
    {"CHECK": "missing_validity_endpoint", "ROWS": int(prices[["CONDITIONVALIDITYSTARTDATE","CONDITIONVALIDITYENDDATE"]].isna().any(axis=1).sum())},
    {"CHECK": "customer_and_group_both_unspecified_review_scope", "ROWS": int(prices[["CUSTOMER","CUSTOMERPRICEGROUP"]].isna().all(axis=1).sum())},
])
display(price_diagnostics)
print("Discount integration deferred until condition semantics, scope precedence, overlap and quantity compatibility are verified.")


# ## 3. Evidence-use record · P1.07–P1.08
# 
# **Freeze this design before examining customer histories.** The proposed split hashes each customer ID
# with a recorded salt. A customer and all their overlapping windows have one role. Hashing is independent
# of behaviour and row order; it does not guarantee representative or sufficiently large evaluation samples.
# Review the fraction and prior exposure before confirmation. Customer-level generalisation is the intended
# claim; a temporal alternative needs a separate design addressing overlap and leakage.
# 
# `PRIOR_EXPOSURE` is a user-supplied exposure register. Exposed customers are forced to development.
# Leaving the register blank does not establish independence: `PRIOR_EXPOSURE_REVIEWED` is a separate
# confirmation. Development exploration, feature decisions and preparation sensitivities below never use
# reserved customer histories. Structural checks above may cover all extracts; record any earlier
# behavioural exposure. Controlled evaluation scenarios/realisations will be separated in Phase 6.
# 
# If a persisted manifest exists, a changed assignment or split specification raises an error. Do not
# delete it to obtain a more favourable split. Document an explicit version change and the resulting
# independence limitations. Confirmed roles are saved before the first behavioural calculation, independently of the general export
# switch. Thus enabling analysis writes the evidence CSV/Parquet pair even with `EXPORT_ARTIFACTS=False`.
# If that freeze fails, analysis stops. Development roles should be considered exposed from this point.
# 

# In[ ]:


def assign_evidence(customer_ids, salt, fraction, exposure):
    if not 0 < fraction < 1:
        raise ValueError("Evaluation fraction must lie strictly between 0 and 1")
    if not salt:
        raise ValueError("Record a non-empty split salt")
    records = []
    for customer in sorted({str(x) for x in customer_ids if pd.notna(x)}):
        score = int(hashlib.sha256(f"{salt}:{customer}".encode("utf-8")).hexdigest(), 16) / 2**256
        prior = str(exposure.get(customer, ""))
        records.append({"CUSTOMERID": customer, "ROLE": "development" if prior or score >= fraction else "reserved_evaluation",
                        "PRIOREXPOSURE": prior, "SPLITSALT": salt, "EVALUATIONFRACTION": fraction,
                        "METHOD": "sha256_customer_v1"})
    return pd.DataFrame(records, columns=["CUSTOMERID","ROLE","PRIOREXPOSURE","SPLITSALT","EVALUATIONFRACTION","METHOD"])


def validate_evidence_manifest(proposed, path):
    if path.is_symlink():
        raise ValueError("Evidence manifest must not be a symlink")
    if not path.exists():
        return
    old = pd.read_parquet(path)
    if list(old.columns) != list(proposed.columns) or old["CUSTOMERID"].duplicated().any():
        raise ValueError("Persisted evidence manifest has an incompatible schema or duplicate IDs")
    if not set(old["CUSTOMERID"]).issubset(set(proposed["CUSTOMERID"])):
        raise ValueError("Previously assigned customers disappeared; review source version and evidence manifest")
    common = proposed.set_index("CUSTOMERID").loc[old["CUSTOMERID"]].reset_index()
    try:
        pd.testing.assert_frame_equal(old.reset_index(drop=True), common, check_dtype=False)
    except AssertionError as exc:
        raise ValueError("Evidence specification/exposure changed. Document a versioned revision before exploration") from exc


def validate_window(start, end):
    if start is None or end is None:
        raise ValueError("Set explicit observation bounds; do not infer them from activity")
    start, end = pd.Timestamp(start), pd.Timestamp(end)
    if pd.isna(start) or pd.isna(end) or start.tz is not None or end.tz is not None:
        raise ValueError("Use valid timezone-naive observation dates")
    if start != start.normalize() or end != end.normalize() or start + pd.DateOffset(months=24) != end:
        raise ValueError("Observation bounds must be midnight dates exactly 24 calendar months apart")
    return start, end


def analysis_integrity_issues(order_rows, headers, development_ids):
    """Block uncertain order attribution/eligibility before quarantine could create false zeros.

    This deliberately blocks the development analysis rather than guessing affected periods.
    Missing amount and item evidence are handled per measure instead of excluding orders.
    """
    issues = []
    if order_rows["SOLDTOPARTY"].isna().any():
        issues.append("Missing order customer: resolve attribution before claiming complete development activity")
    raw_dev = order_rows[order_rows["SOLDTOPARTY"].isin(development_ids)]
    # Include headers whose conflicting copies name any development customer.
    dev_orders = set(raw_dev["SALESORDER"].dropna())
    affected = headers[headers["SALESORDER"].isin(dev_orders) | headers["SOLDTOPARTY"].isin(development_ids)]
    if not affected["HEADERVALID"].all():
        issues.append("Unresolved development order headers: quarantine must not imply zero activity")
    if raw_dev["SALESORDER"].isna().any() or raw_dev["SALESORDERDATE"].isna().any():
        issues.append("Missing development order identity/date: resolve before period comparisons")
    candidates = raw_dev[raw_dev["SALESORDERTYPE"].eq("OR").fillna(False)]
    if raw_dev["SALESORDERTYPE"].isna().any():
        issues.append("Missing development document type leaves order eligibility uncertain")
    if (~candidates["OVERALLSDPROCESSSTATUS"].isin(["A","B","C"])).any():
        issues.append("Unknown development processing status leaves eligibility uncertain")
    if (~candidates["OVERALLSDDOCUMENTREJECTIONSTS"].isin(["A","B","C"])).any():
        issues.append("Unknown development rejection status leaves eligibility uncertain")
    if candidates["SDDOCUMENTREASON"].isna().any() or candidates["TRANSACTIONCURRENCY"].isna().any():
        issues.append("Missing development reason/currency leaves eligibility uncertain")
    return issues


def readiness_issues(tables, evidence, start, end, evidence_confirmed, exposure_reviewed, currency, reasons):
    issues = []
    if tables["orders"].empty: issues.append("No order records")
    try:
        validate_window(start, end)
    except ValueError as exc:
        issues.append(str(exc))
    if not evidence_confirmed: issues.append("Evidence plan not confirmed")
    if not exposure_reviewed: issues.append("Prior exposure not reviewed")
    if not currency: issues.append("Currency restriction unresolved")
    if reasons is None: issues.append("Order reason eligibility unresolved")
    if evidence.empty or not evidence["ROLE"].eq("development").any(): issues.append("No development customers")
    return issues


def select_orders(headers, start, end, currency, accepted_reasons, include_partial=False):
    start, end = validate_window(start, end)
    if not currency or accepted_reasons is None:
        raise ValueError("Explicit currency and eligible reason codes are required")
    audit = headers.copy()
    reasons = []
    for _, row in audit.iterrows():
        flags = []
        if not row["HEADERVALID"]: flags.append(str(row["HEADERISSUES"]))
        date = row["SALESORDERDATE"]
        if pd.isna(date) or not start <= date < end: flags.append("outside_window_or_invalid_date")
        if pd.isna(row["SALESORDERTYPE"]) or row["SALESORDERTYPE"] != "OR": flags.append("type_not_provisionally_eligible")
        if pd.isna(row["OVERALLSDPROCESSSTATUS"]) or row["OVERALLSDPROCESSSTATUS"] not in {"A","B","C"}: flags.append("unknown_processing_status")
        rejection = row["OVERALLSDDOCUMENTREJECTIONSTS"]
        if pd.isna(rejection): flags.append("missing_rejection_status")
        elif rejection == "C": flags.append("fully_rejected")
        elif rejection == "B" and not include_partial: flags.append("partial_rejection_pending")
        elif rejection not in {"A","B","C"}: flags.append("unknown_rejection_status")
        if pd.isna(row["SDDOCUMENTREASON"]) or row["SDDOCUMENTREASON"] not in accepted_reasons: flags.append("reason_not_confirmed_eligible")
        if pd.isna(row["TRANSACTIONCURRENCY"]) or row["TRANSACTIONCURRENCY"] != currency: flags.append("currency_restriction")
        reasons.append(";".join(flags))
    audit["SELECTIONREASONS"] = pd.Series(reasons, index=audit.index, dtype="string")
    audit["SELECTED"] = audit["SELECTIONREASONS"].eq("")
    return audit.loc[audit["SELECTED"], headers.columns].reset_index(drop=True), audit


def interval_covered(start, end, coverage):
    """Completeness must cover the full requested interval, with no undocumented gaps."""
    cursor = start
    intervals = []
    for a, b in coverage:
        a, b = pd.Timestamp(a), pd.Timestamp(b)
        if pd.isna(a) or pd.isna(b) or a >= b or a.tz is not None or b.tz is not None:
            raise ValueError("Coverage intervals need valid start < end dates without timezone")
        intervals.append((a,b))
    for a,b in sorted(intervals):
        if a > cursor: break
        if b > cursor: cursor = b
        if cursor >= end: return True
    return False


def build_profiles(headers, items, products, start, end, frequency="MS", coverage=()):
    """Development-only provisional profiles. Unknown coverage leaves primary measures undefined."""
    start, end = validate_window(start, end)
    if frequency not in {"MS","QS"}: raise ValueError("Use MS or QS for the exploratory comparison")
    if headers["TRANSACTIONCURRENCY"].dropna().nunique() > 1:
        raise ValueError("Mixed currencies require an explicit restriction or documented conversion")
    if headers["SALESORDER"].duplicated().any() or not headers["HEADERVALID"].all():
        raise ValueError("Profiles need unique, consistent, valid order headers")
    if products["PRODUCT"].duplicated().any() or products["PRODUCT"].isna().any():
        raise ValueError("Resolve product-master keys before joining; do not arbitrarily deduplicate")
    columns = ["CUSTOMERID","PERIODSTART","PERIODEND","TRANSACTIONCURRENCY","COVERAGEKNOWN","PARTIALPERIOD",
               "OBSERVEDORDERCOUNT","OBSERVEDTOTALORDERVALUE","VALUECOMPLETE","ASSORTMENTCOMPLETE","GROUPCOMPLETE"] + CORE_MEASURES
    if headers.empty: return pd.DataFrame(columns=columns)
    h = headers.loc[headers["SALESORDERDATE"].ge(start) & headers["SALESORDERDATE"].lt(end)].copy()
    period_alias = "M" if frequency == "MS" else "Q"
    h["PERIODSTART"] = h["SALESORDERDATE"].dt.to_period(period_alias).dt.start_time
    first = start.to_period(period_alias).start_time
    bins = pd.date_range(first, end, freq=frequency, inclusive="left")
    joined = items[items["SALESORDER"].isin(h["SALESORDER"])].merge(
        products[["PRODUCT","PRODUCTGROUP"]], left_on="MATERIAL", right_on="PRODUCT", how="left", validate="many_to_one")
    joined = joined.merge(h[["SALESORDER","SOLDTOPARTY","PERIODSTART"]], on="SALESORDER", how="left", validate="many_to_one", suffixes=("_RAW", ""))
    hg = {key: frame for key, frame in h.groupby(["SOLDTOPARTY","PERIODSTART"])}
    ig = {key: frame for key, frame in joined.groupby(["SOLDTOPARTY","PERIODSTART"])}
    records = []
    for customer in sorted(h["SOLDTOPARTY"].dropna().unique()):
        for period in bins:
            calendar_end = period + (pd.offsets.MonthBegin(1) if frequency == "MS" else pd.offsets.QuarterBegin(startingMonth=1))
            lo, hi = max(start,period), min(end,calendar_end)
            group = hg.get((customer,period), h.iloc[:0])
            positions = ig.get((customer,period), joined.iloc[:0])
            covered = interval_covered(lo,hi,coverage)
            count = len(group)
            value_complete = bool(group["TOTALNETAMOUNT"].notna().all())
            # Empty/missing item evidence for any observed order prevents a complete breadth measure.
            item_complete = bool(not positions["ITEMCONFLICT"].any() and positions["MATERIAL"].notna().all()
                                 and set(group["SALESORDER"]).issubset(set(positions["SALESORDER"])))
            group_complete = item_complete and bool(positions["PRODUCTGROUP"].notna().all())
            value = float(group["TOTALNETAMOUNT"].sum()) if value_complete else np.nan
            total = value if covered else np.nan
            n = count if covered else np.nan
            records.append({"CUSTOMERID": customer, "PERIODSTART": period, "PERIODEND": hi,
                "TRANSACTIONCURRENCY": h["TRANSACTIONCURRENCY"].dropna().iloc[0] if h["TRANSACTIONCURRENCY"].notna().any() else pd.NA,
                "COVERAGEKNOWN": covered, "PARTIALPERIOD": lo != period or hi != calendar_end,
                "OBSERVEDORDERCOUNT": count, "OBSERVEDTOTALORDERVALUE": value,
                "VALUECOMPLETE": value_complete, "ASSORTMENTCOMPLETE": item_complete, "GROUPCOMPLETE": group_complete,
                "ORDERCOUNT": n, "TOTALORDERVALUE": total,
                "AVGORDERVALUE": total/count if covered and count else np.nan,
                "DISTINCTPRODUCTCOUNT": positions["MATERIAL"].nunique() if covered and item_complete else np.nan,
                "DISTINCTPRODUCTGROUPCOUNT": positions["PRODUCTGROUP"].nunique() if covered and group_complete else np.nan})
    return pd.DataFrame(records, columns=columns)


def population_assessment(development_ids, selected):
    """Account for every assigned development customer, including no eligible orders."""
    population = pd.DataFrame({"CUSTOMERID":sorted(development_ids)})
    counts = selected.groupby("SOLDTOPARTY").size()
    population["SELECTEDORDERS"] = population["CUSTOMERID"].map(counts).fillna(0).astype("int64")
    population["PROFILESTATUS"] = np.where(population["SELECTEDORDERS"].gt(0),
        "provisional_profile_available","no_eligible_orders_requires_review")
    return population


def history_assessment(headers, profiles, start, end):
    start, end = validate_window(start,end)
    records = []
    for customer, h in headers.groupby("SOLDTOPARTY"):
        h = h.loc[h["SALESORDERDATE"].ge(start) & h["SALESORDERDATE"].lt(end)].sort_values(["SALESORDERDATE","SALESORDER"])
        if h.empty: continue
        dates = h["SALESORDERDATE"]
        gaps = dates.diff().dt.total_seconds().div(86400).dropna()
        p = profiles[profiles["CUSTOMERID"].eq(customer)] if not profiles.empty else pd.DataFrame()
        left = h[h["SALESORDERDATE"].lt(start + pd.DateOffset(months=12))]
        right = h[h["SALESORDERDATE"].ge(start + pd.DateOffset(months=12))]
        usable = p["COVERAGEKNOWN"] & ~p["PARTIALPERIOD"] if not p.empty else pd.Series(dtype=bool)
        records.append({"CUSTOMERID": customer, "OBSERVEDORDERCOUNT": len(h),
            "FIRSTOBSERVEDORDER": dates.min(), "LASTOBSERVEDORDER": dates.max(),
            "ACTIVEOBSERVEDMONTHS": dates.dt.to_period("M").nunique(),
            "MEDIANINTERORDERDAYS": gaps.median(), "MAXINTERORDERDAYS": gaps.max(),
            "DAYSAFTERLASTOBSERVEDORDER": (end-dates.max()).days,
            "KNOWNCOMPLETEPERIODS": int(usable.sum()),
            "KNOWNZEROPERIODS": int((usable & p["ORDERCOUNT"].eq(0)).sum()) if not p.empty else 0,
            "UNKNOWNCOVERAGEPERIODS": int((~p["COVERAGEKNOWN"]).sum()) if not p.empty else pd.NA,
            "ORDERSFIRST12MONTHS": len(left), "ORDERSSECOND12MONTHS": len(right),
            "COMPARISONSUPPORT": "one_side_has_no_observed_orders_review_coverage" if left.empty or right.empty else "both_halves_have_orders_not_a_suitability_verdict",
            "MAXORDERABSVALUESHARE": h["TOTALNETAMOUNT"].abs().max()/h["TOTALNETAMOUNT"].abs().sum()
                if h["TOTALNETAMOUNT"].notna().all() and h["TOTALNETAMOUNT"].abs().sum() else np.nan})
    return pd.DataFrame(records)


# In[ ]:


def export_table(frame, folder, stem):
    """CSV -> DuckDB all-string reader -> explicit Arrow schema -> verified Parquet."""
    if not re.fullmatch(r"[A-Za-z0-9_]+", stem): raise ValueError("Use a plain artifact stem")
    if frame.columns.duplicated().any(): raise ValueError("Export columns must be unique")
    folder = Path(folder)
    if folder.is_symlink(): raise ValueError("Output directory must not be a symlink")
    folder.mkdir(parents=True,exist_ok=True)
    expected = pa.Table.from_pandas(frame,preserve_index=False)
    # Parquet has no seconds timestamp unit. Store those fields losslessly as nanoseconds.
    schema = pa.schema([pa.field(field.name,pa.timestamp("ns",tz=field.type.tz),nullable=field.nullable)
                        if pa.types.is_timestamp(field.type) and field.type.unit == "s" else field
                        for field in expected.schema],metadata=expected.schema.metadata)
    expected = expected.cast(schema)
    null_token = "__FUUCCE_NULL_7D62C8__"
    for column in frame.columns:
        if frame[column].astype("string").eq(null_token).any():
            raise ValueError("CSV null token collides with a literal value")
    with TemporaryDirectory(prefix=".p1-",dir=folder) as work:
        csv_file = Path(work)/f"{stem}.csv"
        parquet_file = Path(work)/f"{stem}.parquet"
        frame.to_csv(csv_file,index=False,encoding="utf-8",na_rep=null_token,float_format="%.17g")
        with duckdb.connect() as con:
            text = con.read_csv(str(csv_file),header=True,all_varchar=True,na_values=null_token).to_arrow_table()
        # Arrow cannot cast a string column to null; validate and construct null fields explicitly.
        arrays = []
        for field in expected.schema:
            column = text[field.name]
            if pa.types.is_null(field.type):
                if column.null_count != len(column):
                    raise AssertionError("Unexpected non-null CSV value in an all-null field")
                arrays.append(pa.nulls(len(column)))
            else:
                arrays.append(column.cast(field.type))
        converted = pa.Table.from_arrays(arrays,schema=expected.schema)
        pq.write_table(converted,parquet_file,compression="zstd")
        roundtrip = pq.read_table(parquet_file)
        if not roundtrip.schema.equals(expected.schema,check_metadata=True):
            raise AssertionError(f"Export schema mismatch for {stem}: {expected.schema} != {roundtrip.schema}")
        restored = roundtrip.to_pandas().astype(frame.dtypes.to_dict())
        # Arrow has one null representation; Python object None/pd.NA are equivalent missing values.
        comparison = frame.reset_index(drop=True).copy()
        actual = restored.copy()
        for column in frame.columns:
            if frame[column].dtype == object:
                comparison[column] = comparison[column].where(comparison[column].notna(),None)
                actual[column] = actual[column].where(actual[column].notna(),None)
        pd.testing.assert_frame_equal(actual,comparison,check_exact=False,rtol=1e-12,atol=1e-12)
        if not np.array_equal(roundtrip.to_pandas().isna().to_numpy(),frame.isna().to_numpy()):
            raise AssertionError("Missing-value mask changed")
        csv_file.replace(folder/f"{stem}.csv")
        parquet_file.replace(folder/f"{stem}.parquet")
    return restored


# In[ ]:


evidence = assign_evidence(views["headers"]["SOLDTOPARTY"], SPLIT_SALT, EVALUATION_FRACTION, PRIOR_EXPOSURE)
validate_evidence_manifest(evidence, EVIDENCE_FILE)
# Display role counts only; do not inspect reserved behavioural histories.
display(evidence.groupby("ROLE").size().rename("CUSTOMERS").reset_index())
print("Evidence plan confirmed:", EVIDENCE_PLAN_CONFIRMED, "| Prior exposure reviewed:", PRIOR_EXPOSURE_REVIEWED)

blocking_issues = readiness_issues(tables,evidence,OBSERVATION_START,OBSERVATION_END,
    EVIDENCE_PLAN_CONFIRMED,PRIOR_EXPOSURE_REVIEWED,ANALYSIS_CURRENCY,ACCEPTED_REASON_CODES)
if not ELIGIBILITY_RULES_CONFIRMED: blocking_issues.append("Provisional eligibility rules not confirmed")
if not IDENTIFIER_SEMANTICS_CONFIRMED: blocking_issues.append("Identifier and missing-token semantics not confirmed")
if field_audit.loc[field_audit["TABLE"].isin(["orders","products"]),"MISSINGCOLUMN"].any():
    blocking_issues.append("Missing documented core order/product fields; review field audit")
if field_audit.loc[field_audit["TABLE"].isin(["orders","products"]),"NUMERICIDENTIFIERRISK"].any():
    blocking_issues.append("Numeric core identifier source risks leading-zero loss; repair extraction")
if tables["products"]["PRODUCT"].duplicated().any() or tables["products"]["PRODUCT"].isna().any():
    blocking_issues.append("Product-master candidate key is not unique/non-null")
if not evidence["ROLE"].eq("reserved_evaluation").any():
    print("No reserved customers currently assigned: final real-case evaluation feasibility remains unresolved.")
development_ids = set(evidence.loc[evidence["ROLE"].eq("development"),"CUSTOMERID"])
blocking_issues.extend(analysis_integrity_issues(tables["orders"],views["headers"],development_ids))
ANALYSIS_READY = not blocking_issues
if ANALYSIS_READY:
    # Mandatory evidence freeze precedes every behavioural calculation, even with exports disabled.
    validate_evidence_manifest(evidence,EVIDENCE_FILE)
    export_table(evidence,EVIDENCE_FILE.parent,EVIDENCE_FILE.stem)
    print("Confirmed evidence assignments persisted before exploration.")
print("Behavioural exploration:", "enabled for development customers" if ANALYSIS_READY else "pending")
for issue in blocking_issues: print(" -",issue)


# ## 4. Customer histories and focused exploration · P1.09–P1.13
# 
# Only development customers enter the following calculations. Selection audits retain every development
# order with all exclusion/quarantine reasons. Open/in-progress orders are eligible under the provisional
# rules; fully rejected orders are excluded. Partly rejected orders are excluded provisionally and examined
# as a sensitivity alternative. Their recorded amount is not automatically interpreted as a retained value.
# A population audit retains all development customers; customers without eligible orders require review
# and are not silently declared suitable or unchanged. Profiles require at least one eligible order.
# No unusual order is removed just for being large, negative or zero. Review questionable values first.
# 
# `ORDERCOUNT` uses one consistent eligible header per order. `TOTALORDERVALUE` counts its amount once;
# any missing amount makes that period's total and average undefined. Product breadth uses item evidence,
# not the sum of incompatible quantities. Missing item/product-group information produces undefined
# breadth rather than a misleading complete count. Currency restriction affects the population analysed.
# 
# Coverage-aware primary measures are undefined when completeness is unknown. `OBSERVEDORDERCOUNT` and
# `OBSERVEDTOTALORDERVALUE` preserve recorded evidence separately; they do not prove complete activity.
# Zero averages remain undefined. Incomplete calendar periods are flagged even if their observed slice is
# covered. Empty covered periods have zero counts/totals, not zero average order size.
# 
# Monthly and quarterly representations are compared as exploratory options. The first/last order dates
# are observations, never acquisition dates or coverage boundaries. The 12-month halves below describe
# comparison support and decline, with **no separate annual minimum**. Two to four annual orders is only
# orientation; final comparison windows and suitability criteria require a reasoned review.
# 

# In[ ]:


profiles = pd.DataFrame()
quarterly_profiles = pd.DataFrame()
histories = pd.DataFrame()
population = pd.DataFrame()
selection_audit = pd.DataFrame()
sensitivity = pd.DataFrame()
resolution_summary = pd.DataFrame()
selected = views["headers"].iloc[:0].copy()
figures = {}

if ANALYSIS_READY:
    development_ids = set(evidence.loc[evidence["ROLE"].eq("development"),"CUSTOMERID"])
    dev_headers = views["headers"][views["headers"]["SOLDTOPARTY"].isin(development_ids)].copy()
    selected, selection_audit = select_orders(dev_headers,OBSERVATION_START,OBSERVATION_END,
        ANALYSIS_CURRENCY,ACCEPTED_REASON_CODES,INCLUDE_PARTIAL_REJECTIONS)
    population = population_assessment(development_ids,selected)
    display(population)
    dev_items = views["items"][views["items"]["SALESORDER"].isin(selected["SALESORDER"])].copy()
    profiles = build_profiles(selected,dev_items,tables["products"],OBSERVATION_START,OBSERVATION_END,coverage=ORDER_COVERAGE)
    quarterly_profiles = build_profiles(selected,dev_items,tables["products"],OBSERVATION_START,OBSERVATION_END,frequency="QS",coverage=ORDER_COVERAGE)
    histories = history_assessment(selected,profiles,OBSERVATION_START,OBSERVATION_END)
    assert set(profiles.get("CUSTOMERID",[])).issubset(development_ids)
    display(selection_audit.groupby(["SELECTED","SELECTIONREASONS"],dropna=False).size().rename("ORDERS").reset_index())
    display(histories)
    rows = []
    for label,p in [("monthly",profiles),("quarterly",quarterly_profiles)]:
        if p.empty: continue
        supported = p[p["COVERAGEKNOWN"] & ~p["PARTIALPERIOD"]]
        rows.append({"RESOLUTION":label,"CUSTOMERPERIODS":len(p),"KNOWNCOMPLETEPERIODS":len(supported),
            "UNKNOWNCOVERAGEPERIODS":int((~p["COVERAGEKNOWN"]).sum()),"PARTIALPERIODS":int(p["PARTIALPERIOD"].sum()),
            "ZEROORDERPROPORTION":float(supported["ORDERCOUNT"].eq(0).mean()) if len(supported) else np.nan})
    resolution_summary = pd.DataFrame(rows)
    display(resolution_summary)
    # Paired preparation sensitivity on the same development population and date/currency basis.
    variants = []
    for partial in [False,True]:
        alternate, _ = select_orders(dev_headers,OBSERVATION_START,OBSERVATION_END,ANALYSIS_CURRENCY,ACCEPTED_REASON_CODES,partial)
        variants.append({"SCENARIO":"exclude_partial" if not partial else "include_partial_unvalidated_amount",
            "ORDERS":len(alternate),"CUSTOMERS":alternate["SOLDTOPARTY"].nunique(),
            "MISSINGAMOUNTORDERS":int(alternate["TOTALNETAMOUNT"].isna().sum()),
            "RECORDEDNETORDERVALUE":alternate["TOTALNETAMOUNT"].sum(min_count=len(alternate)) if len(alternate) else 0.0,
            "STATUS":"provisional sensitivity; does not resolve amount semantics"})
    sensitivity = pd.DataFrame(variants)
    display(sensitivity)
else:
    print("Customer histories, provisional profiles and sensitivities are pending the issues listed above.")


# In[ ]:


measure_assessment = pd.DataFrame([
    {"MEASURE":measure,"NONNULLPERIODS":int(profiles[measure].notna().sum()) if not profiles.empty else 0,
     "PERIODS":len(profiles),"STATUS":"review calculated evidence" if not profiles.empty else "not assessed: no analysis-ready profiles"}
    for measure in CORE_MEASURES])
display(measure_assessment)
print("AVGORDERVALUE = TOTALORDERVALUE / ORDERCOUNT; these are dependent measures.")
print("Fewer orders can reduce observed assortment breadth. Net order amounts do not establish realised revenue.")

if not histories.empty:
    fig, axes = plt.subplots(1,2,figsize=(11,3.5))
    axes[0].hist(histories["OBSERVEDORDERCOUNT"],bins="auto")
    axes[0].set(xlabel="Distinct eligible orders in 24 months",ylabel="Development customers",title="How much comparison evidence is recorded?")
    gaps = histories["MEDIANINTERORDERDAYS"].dropna()
    if len(gaps): axes[1].hist(gaps,bins="auto")
    axes[1].set(xlabel="Median days between recorded orders",ylabel="Development customers",title="Would monthly profiles be sparse?")
    fig.tight_layout(); figures["comparison_support"] = fig; plt.show()
    # Purposeful, reproducible range of histories: ordinary, sparse, dense, incomplete-value and large-order-sensitive.
    ordinary = histories.iloc[(histories["OBSERVEDORDERCOUNT"]-histories["OBSERVEDORDERCOUNT"].median()).abs().argsort()[:1]]
    candidates = [ordinary, histories.nsmallest(1,"OBSERVEDORDERCOUNT"),histories.nlargest(1,"OBSERVEDORDERCOUNT"),
                  histories.nlargest(1,"MAXORDERABSVALUESHARE")]
    missing_value_ids = set(selected.loc[selected["TOTALNETAMOUNT"].isna(),"SOLDTOPARTY"])
    candidates.append(histories[histories["CUSTOMERID"].isin(missing_value_ids)].head(1))
    selected_cases = pd.concat(candidates).drop_duplicates("CUSTOMERID").head(5)
    display(selected_cases)
    for customer in selected_cases["CUSTOMERID"]:
        p = profiles[profiles["CUSTOMERID"].eq(customer)]
        underlying = selected[selected["SOLDTOPARTY"].eq(customer)].sort_values("SALESORDERDATE")
        fig, axes = plt.subplots(3,1,figsize=(10,7),sharex=True)
        axes[0].step(p["PERIODSTART"],p["OBSERVEDORDERCOUNT"],where="post",label="Recorded orders (coverage may be unknown)")
        axes[0].plot(p["PERIODSTART"],p["ORDERCOUNT"],"o",label="Count with confirmed coverage")
        axes[0].set(ylabel="Orders"); axes[0].legend(fontsize=8)
        axes[1].plot(p["PERIODSTART"],p["TOTALORDERVALUE"],"o-",label="Covered period value")
        axes[1].scatter(underlying["SALESORDERDATE"],underlying["TOTALNETAMOUNT"],marker="x",label="Individual header amount")
        axes[1].set(ylabel=f"Net order value ({ANALYSIS_CURRENCY})"); axes[1].legend(fontsize=8)
        axes[2].plot(p["PERIODSTART"],p["DISTINCTPRODUCTCOUNT"],"o-",label="Products")
        axes[2].plot(p["PERIODSTART"],p["DISTINCTPRODUCTGROUPCOUNT"],"s-",label="Groups")
        axes[2].set(ylabel="Breadth",xlabel="Period start"); axes[2].legend(fontsize=8)
        for ax in axes:
            for _, row in p[~p["COVERAGEKNOWN"]].iterrows():
                ax.axvspan(row["PERIODSTART"],row["PERIODEND"],color="grey",alpha=.10)
        fig.suptitle(f"Development customer {customer}: exploratory evidence; grey = unknown coverage")
        fig.tight_layout()
        # Numbered filenames keep customer identifiers out of filenames.
        figures[f"development_history_{len(figures):02d}"] = fig
        plt.show()
        display(underlying[["SALESORDER","SALESORDERDATE","TOTALNETAMOUNT","TRANSACTIONCURRENCY"]])
else:
    print("Focused graphics await development evidence. No behavioural findings have been inferred from the schema.")


# ## 5. Preparation decisions, blockers and Phase 2 handover · P1.14–P1.18
# 
# The register distinguishes documented facts, adopted exploratory choices, preparation proposals and
# unresolved questions. Replace or supplement proposals through `REVIEWED_DECISIONS` with an evidence
# reference and rationale. Reviewing synthetic calculations does not substantiate empirical suitability.
# 
# Before Phase 2, resolve the exact window and extraction coverage/filters, identifier/null semantics,
# header/item conflicts, master-key uniqueness, status/reason eligibility and currency basis. Review
# partly rejected order amounts with the data owner. Confirm whether product groups and customer
# attributes represent the observation period or only an extraction-time snapshot.
# 
# Use comparison support to justify suitability and temporal resolution. One inactive comparison side can
# be relevant to a decline; do not remove such customers with an annual order minimum. Boundary gaps are
# censored observations. A large individual order can dominate values but does not prove project business
# or a sustained change. Findings describe recorded purchasing activity, not motives, churn or profitability.
# 

# In[ ]:


def decision_register(reviewed):
    base = [
        ("Order granularity","adopted_for_exploration","data description; header_audit; selection_audit",
         "Retain each consistent eligible header once; separate item evidence",
         "TOTALNETAMOUNT repeats across items; item joins cannot define monetary totals","Review conflicting headers with extractor"),
        ("Missing/duplicate records","proposed_for_preparation","field_audit; key_audit; header_audit",
         "Trim strings, apply explicit null tokens, remove exact duplicate rows in provisional views; quarantine conflicts",
         "Avoid silently selecting an arbitrary contradictory record","Verify source null tokens, identifier semantics and duplicate causes"),
        ("Coverage","unresolved","extraction_register; date_audit; temporal_resolution",
         "Use only confirmed completeness intervals; unknown periods retain undefined primary measures",
         "Observed order span does not prove continuous extraction","Obtain extraction metadata and customer-specific exceptions"),
        ("Order eligibility","unresolved","code_audit; selection_audit; preparation_sensitivity",
         "OR; process A/B/C; reject C; partial rejection sensitivity; explicitly supplied eligible reason codes",
         "Open processing is not invalid; partial rejection amounts/cancellation reasons need domain verification","Confirm code combinations and net-amount treatment"),
        ("Currency and quantity","proposed_for_preparation","code_audit; field_audit",
         "Restrict monetary analysis to an explicitly chosen currency; no cross-unit quantity aggregation",
         "No exchange rates or unit conversion relationships are specified","Quantify the restricted population and document any later conversion"),
        ("Core measures","proposed_for_preparation","measure_assessment; provisional_monthly",
         "Assess ORDERCOUNT, TOTALORDERVALUE, AVGORDERVALUE and two breadth measures",
         "Compact activity/value/assortment view; average value and breadth are not independent of count","Review completeness and usefulness on development evidence"),
        ("Temporal representation and suitability","unresolved","history_assessment; temporal_resolution; development figures",
         "Compare monthly/quarterly views and available comparison support; impose no annual minimum",
         "Sparse activity can make fine aggregation uninformative; decline must remain representable","Justify windows, support criteria and boundary-period treatment before Phase 2"),
        ("Evaluation boundaries","proposed_for_preparation","evidence_manifest; prior exposure register",
         "Customer-level SHA256 assignment, exposed customers development only; fixed salt and fraction",
         "Keep all overlapping windows from a customer in one role","Confirm exposure, population/sample adequacy and persist before future development"),
        ("Historical master data","unresolved","extraction_register; relationship_audit",
         "Treat current product groups/customer attributes as snapshots unless history is verified",
         "Current categories need not describe past orders","Confirm temporal meaning with extractor"),
        ("Discount extension","unresolved_optional","price_feasibility; relationship_audit",
         "Defer discount integration; no calculation from unverified condition assignment",
         "Sentinels, missing after-discount prices, overlapping scopes and unit compatibility can invalidate discounts","Confirm condition semantics and assignment only if extension is pursued"),
    ]
    columns = ["TOPIC","STATUS","EVIDENCE","DECISION","RATIONALE","NEXTACTION"]
    result = pd.DataFrame(base, columns=columns)
    if reviewed:
        additions = pd.DataFrame(reviewed)
        if set(columns) - set(additions.columns) or additions[columns].isna().any().any():
            raise ValueError("Reviewed decisions require all six non-null fields")
        if not additions["STATUS"].isin(["adopted_for_exploration","proposed_for_preparation","unresolved","unresolved_optional"]).all():
            raise ValueError("Unexpected decision status")
        result = pd.concat([result, additions[columns]], ignore_index=True)
    return result


# In[ ]:


decisions = decision_register(REVIEWED_DECISIONS)
display(decisions)
# A transparent checklist: implementation coverage never substitutes for the actual observed assessment.
completion = pd.DataFrame([
    {"REQUIREMENT":"Data meaning and core relationships", "IMPLEMENTED":True,
     "EMPIRICALSTATUS":"review required" if len(tables["orders"]) else "pending populated extracts"},
    {"REQUIREMENT":"Quality and coverage limitations", "IMPLEMENTED":True,
     "EMPIRICALSTATUS":"review extraction metadata, fields, keys and coverage"},
    {"REQUIREMENT":"Core measure feasibility", "IMPLEMENTED":True,
     "EMPIRICALSTATUS":"review calculated evidence" if len(profiles) else "pending analysis-ready profiles"},
    {"REQUIREMENT":"Activity, temporal representation and suitability", "IMPLEMENTED":True,
     "EMPIRICALSTATUS":"justify recommendations from development evidence"},
    {"REQUIREMENT":"Development/evaluation boundaries", "IMPLEMENTED":True,
     "EMPIRICALSTATUS":"confirmed; verify saved manifest" if EVIDENCE_PLAN_CONFIRMED and PRIOR_EXPOSURE_REVIEWED else "pending plan/exposure confirmation"},
    {"REQUIREMENT":"Explicit Phase 2 preparation recommendations", "IMPLEMENTED":True,
     "EMPIRICALSTATUS":"pending evidence-linked review of decision register"},
])
open_issues = pd.DataFrame([{"ISSUE":issue,"SCOPE":"core","NEXTACTION":"Resolve the corresponding setting or audit before behavioural exploration"}
                           for issue in blocking_issues],columns=["ISSUE","SCOPE","NEXTACTION"])
extra_issues = [
    {"ISSUE":"Extraction coverage not established", "SCOPE":"core", "NEXTACTION":"Obtain verified completeness intervals and filters; unknown periods cannot support inactivity claims"}
    for _ in [0] if not ORDER_COVERAGE]
if not all(EXTRACTION[name]["EXTRACTEDAT"] and EXTRACTION[name]["FILTERS"] is not None and EXTRACTION[name]["COVERAGE"] is not None
           for name in ["orders","products","customers"]):
    extra_issues.append({"ISSUE":"Core extraction metadata incomplete","SCOPE":"core","NEXTACTION":"Complete extraction date, filters and coverage/source semantics for core tables"})
if not REVIEWED_DECISIONS:
    extra_issues.append({"ISSUE":"Evidence-linked preparation recommendations not reviewed","SCOPE":"core","NEXTACTION":"Review all core decision topics and enter recommendations with evidence and rationale"})
if not profiles.empty and profiles["ORDERCOUNT"].notna().sum() == 0:
    extra_issues.append({"ISSUE":"No complete customer-period measures","SCOPE":"core","NEXTACTION":"Resolve coverage or restrict supported analysis scope explicitly"})
if not evidence["ROLE"].eq("reserved_evaluation").any():
    extra_issues.append({"ISSUE":"No reserved real evaluation customers","SCOPE":"core","NEXTACTION":"Review evaluation sampling before using further behavioural evidence"})
open_issues = pd.concat([open_issues,pd.DataFrame(extra_issues)],ignore_index=True)
display(open_issues, completion)
print("Empirical review declared complete:", EMPIRICAL_REVIEW_COMPLETE)
print("Phase 1 completion is a researcher judgement against all six requirements above; it is not auto-certified by a flag.")
print("Next: resolve core blockers, review the evidence and adopt explicit preparation recommendations for Phase 2.")


# ### Backlog coverage and remaining work
# 
# | Tasks | Notebook implementation | Required later evidence/action |
# | --- | --- | --- |
# | P1.01–P1.02 | Scope, configuration, schema manifest, Parquet loading and synthetic verification | User selects kernel and supplies extracts |
# | P1.03–P1.06 | Inventory/extraction register, field/key/relationship/status/date/value diagnostics | Verify metadata and meanings against populated extracts |
# | P1.07–P1.08 | Stable customer roles, exposure register, persisted-manifest validation, behavioural gate | Confirm split and prior exposure; preserve manifest |
# | P1.09–P1.10 | Histories, intervals, active/empty periods, comparison-support indicators | Justify suitability; no separate annual minimum |
# | P1.11–P1.13 | Five measures, monthly/quarterly profiles, purposeful figures and rejection sensitivity | Review measure feasibility and temporal resolution |
# | P1.14–P1.16 | Decisions, blockers/next actions, five required output sections and configured artifacts | Record reviewed findings and recommendations |
# | P1.17 | Synthetic arithmetic, isolation, parsing and export checks; reproducibility record | Reproduce with actual declared inputs in the private environment |
# | P1.18 | Explicit completion review | Assess all framework completion criteria before checking complete |
# | P1.O1 | Price-data screen and documented assignment prerequisites | Full discount feasibility remains optional and unverified |
# | P1.O2 | No speculative subgroup/quantity analysis added | Undertake only for a specific unresolved question |
# 

# ## 6. Synthetic verification, reproducibility and optional exports · P1.02, P1.17
# 
# Verification below uses only invented records, independent of loaded extracts. Expected values are
# hand-derived: an order with two items has **one** order and **100** net order value, not 200; a second
# order has 50. February has zero orders only with confirmed coverage. Missing amount/assortment evidence
# remains undefined. Unresolved order attribution/eligibility blocks development analysis so quarantined
# records cannot be turned into apparent inactivity. These are implementation checks, not findings about customers or final evaluation.
# 
# Reusable outputs use CSV followed by an explicit-schema DuckDB/Arrow conversion to Parquet, with both
# formats retained. The general `setup/csv_to_parquet.py` infers CSV types; that can lose zero-padded IDs
# and reinterpret null-like text. This notebook uses the same DuckDB conversion approach with all CSV
# fields first read as strings, a collision-checked null token, and the intended Arrow schema restored.
# Seconds-resolution timestamps are stored losslessly as nanoseconds because Parquet does not support a
# seconds timestamp unit. The round trip checks values, this storage schema and nulls before replacing the output pair. No original extract
# is overwritten. Subsequent phases read Parquet. Staged writes protect against partial file contents;
# replacement of the CSV/Parquet pair is sequential, not a two-file atomic transaction.
# 

# In[ ]:


import unittest
import tempfile

ns = globals()

def synthetic_tables():
    tables = {name: pd.DataFrame(columns=spec['columns']) for name, spec in ns['SOURCES'].items()}
    # Literal, fully invented records. One order has two items; one has a missing value.
    tables['orders'] = pd.DataFrame([
        ['0001','OR','A','R','A','2024-01-10','0007','100','EUR','10','P1','2'],
        ['0001','OR','A','R','A','2024-01-10','0007','100','EUR','20','P2','3'],
        ['0002','OR','C','R','A','2024-03-10','0007','50','EUR','10','P1','1'],
        ['0003','OR','B','R','A','2024-04-01','0007',None,'EUR','10','P1','1'],
    ], columns=ns['SOURCES']['orders']['columns'])
    tables['products'] = pd.DataFrame([
        ['P1','G1','PC','Synthetic A'], ['P2','G2','M','Synthetic B']
    ], columns=ns['SOURCES']['products']['columns'])
    return {name: ns['normalise_table'](df, name)[0] for name, df in tables.items()}


class Phase1Checks(unittest.TestCase):
    def setUp(self):
        self.assertTrue(callable(ns.get('normalise_table')))
        self.tables = synthetic_tables()

    def test_repeated_headers_count_once(self):
        views = ns['order_views'](self.tables['orders'])
        self.assertEqual(len(views['headers']), 3)
        self.assertEqual(views['headers']['TOTALNETAMOUNT'].sum(), 150)
        self.assertEqual(len(views['items']), 4)

    def test_parse_and_schema_failures_are_visible(self):
        raw = pd.DataFrame({'SALESORDER':['0001'], 'SALESORDERDATE':['31/13/2024'], 'TOTALNETAMOUNT':['1,23']})
        typed, audit = ns['normalise_table'](raw, 'orders')
        self.assertEqual(typed.loc[0, 'SALESORDER'], '0001')
        self.assertTrue(pd.isna(typed.loc[0, 'SALESORDERDATE']))
        self.assertTrue(pd.isna(typed.loc[0, 'TOTALNETAMOUNT']))
        self.assertEqual(audit.set_index('COLUMN').loc['TOTALNETAMOUNT', 'PARSEFAILURES'], 1)
        self.assertTrue(audit.set_index('COLUMN').loc['MATERIAL', 'MISSINGCOLUMN'])

    def test_conflicting_headers_and_items_are_quarantined(self):
        raw = self.tables['orders'].copy()
        raw.loc[1, 'TOTALNETAMOUNT'] = 999
        views = ns['order_views'](raw)
        self.assertFalse(views['headers'].set_index('SALESORDER').loc['0001', 'HEADERVALID'])
        duplicate = pd.concat([self.tables['orders'], self.tables['orders'].iloc[[0]].assign(MATERIAL='P9')], ignore_index=True)
        self.assertTrue(ns['order_views'](duplicate)['items'].query("SALESORDER == '0001' and SALESORDERITEM == '10'")['ITEMCONFLICT'].all())

    def test_relationship_duplicates_do_not_multiply_values(self):
        tables = self.tables.copy()
        tables['products'] = pd.concat([tables['products'], tables['products'].iloc[[0]]], ignore_index=True)
        report = ns['structural_assessment'](tables)
        self.assertGreater(report['keys'].query("TABLE == 'products'")['DUPLICATEROWS'].iloc[0], 0)
        with self.assertRaises(ValueError):
            ns['build_profiles'](ns['order_views'](tables['orders'])['headers'], ns['order_views'](tables['orders'])['items'], tables['products'], '2024-01-01', '2026-01-01', coverage=[('2024-01-01','2026-01-01')])

    def test_known_inactivity_missing_values_and_unknown_coverage(self):
        views = ns['order_views'](self.tables['orders'])
        p = ns['build_profiles'](views['headers'], views['items'], self.tables['products'], '2024-01-01', '2026-01-01', coverage=[('2024-01-01','2026-01-01')]).set_index('PERIODSTART')
        jan, feb, apr = (pd.Timestamp(x) for x in ['2024-01-01','2024-02-01','2024-04-01'])
        self.assertEqual(p.loc[jan,'ORDERCOUNT'], 1)
        self.assertEqual(p.loc[jan,'TOTALORDERVALUE'], 100)
        self.assertEqual(p.loc[jan,'DISTINCTPRODUCTCOUNT'], 2)
        self.assertEqual(p.loc[jan,'DISTINCTPRODUCTGROUPCOUNT'], 2)
        self.assertEqual(p.loc[feb,'ORDERCOUNT'], 0)
        self.assertTrue(pd.isna(p.loc[feb,'AVGORDERVALUE']))
        self.assertTrue(pd.isna(p.loc[apr,'TOTALORDERVALUE']))
        unknown = ns['build_profiles'](views['headers'], views['items'], self.tables['products'], '2024-01-01', '2026-01-01').set_index('PERIODSTART')
        self.assertTrue(pd.isna(unknown.loc[feb,'ORDERCOUNT']))
        self.assertTrue(pd.isna(unknown.loc[jan,'ORDERCOUNT']))
        self.assertEqual(unknown.loc[jan,'OBSERVEDORDERCOUNT'], 1)

    def test_partial_periods_and_missing_assortment(self):
        views = ns['order_views'](self.tables['orders'])
        items = views['items'].copy()
        items.loc[0, 'MATERIAL'] = pd.NA
        p = ns['build_profiles'](views['headers'], items, self.tables['products'], '2024-01-01','2026-01-01', coverage=[('2024-01-01','2026-01-01')])
        self.assertTrue(pd.isna(p.loc[0,'DISTINCTPRODUCTCOUNT']))
        self.assertTrue(pd.isna(p.loc[0,'DISTINCTPRODUCTGROUPCOUNT']))
        partial = ns['build_profiles'](views['headers'], views['items'], self.tables['products'], '2024-01-15','2026-01-15', coverage=[('2024-01-15','2026-01-15')])
        self.assertTrue(partial.iloc[0]['PARTIALPERIOD'])
        self.assertTrue(partial.iloc[-1]['PARTIALPERIOD'])

    def test_currency_and_eligibility(self):
        headers = ns['order_views'](self.tables['orders'])['headers']
        headers.loc[0,'OVERALLSDDOCUMENTREJECTIONSTS'] = 'C'
        headers.loc[1,'OVERALLSDDOCUMENTREJECTIONSTS'] = 'B'
        headers.loc[2,'TRANSACTIONCURRENCY'] = 'GBP'
        chosen, audit = ns['select_orders'](headers, '2024-01-01','2026-01-01', 'EUR', {'R'}, include_partial=False)
        self.assertEqual(len(chosen), 0)
        self.assertTrue(audit['SELECTIONREASONS'].str.contains('fully_rejected').any())
        with self.assertRaises(ValueError):
            ns['build_profiles'](headers, ns['order_views'](self.tables['orders'])['items'], self.tables['products'], '2024-01-01','2026-01-01')

    def test_evidence_is_stable_and_exposure_prevents_holdout(self):
        a = ns['assign_evidence'](['0007','0008','0009'], 'fixed', 0.5, {'0008':'already reviewed'})
        b = ns['assign_evidence'](['0009','0007','0008'], 'fixed', 0.5, {'0008':'already reviewed'})
        pd.testing.assert_frame_equal(a, b)
        self.assertEqual(a.set_index('CUSTOMERID').loc['0008','ROLE'], 'development')
        self.assertEqual(len(a), 3)
        with self.assertRaises(ValueError):
            ns['assign_evidence'](['0007'], 'fixed', 1.0, {})

    def test_history_uses_orders_not_item_rows(self):
        views = ns['order_views'](self.tables['orders'])
        result = ns['history_assessment'](views['headers'], pd.DataFrame(), '2024-01-01','2026-01-01')
        self.assertEqual(result.iloc[0]['OBSERVEDORDERCOUNT'], 3)
        self.assertEqual(result.iloc[0]['ACTIVEOBSERVEDMONTHS'], 3)
        self.assertEqual(result.iloc[0]['MAXINTERORDERDAYS'], 60)

    def test_export_preserves_identifiers_nulls_and_literal_tokens(self):
        df = pd.DataFrame({'CUSTOMERID':pd.Series(['0007','NA',''],dtype='string'), 'LABEL':pd.Series(['literal',None,'NULL'],dtype='string'), 'N':pd.Series([1,None,0],dtype='Int64'), 'DATE':pd.to_datetime(['2024-01-01',None,'2024-01-02'])})
        with tempfile.TemporaryDirectory(prefix='erp-p1-synthetic-') as folder:
            restored = ns['export_table'](df, Path(folder), 'roundtrip')
            pd.testing.assert_frame_equal(restored,df)
            self.assertTrue((Path(folder)/'roundtrip.csv').exists())
            self.assertTrue((Path(folder)/'roundtrip.parquet').exists())

    def test_export_empty_and_all_null_columns(self):
        for df in [pd.DataFrame({'METADATA':[None,None], 'KEY':pd.Series(['0001','0002'],dtype='string')}),
                   pd.DataFrame({'DATE':pd.Series(dtype='datetime64[ns]'), 'KEY':pd.Series(dtype='string')}),
                   pd.DataFrame({'DATE':pd.Series(pd.to_datetime(['2024-01-01'])).astype('datetime64[s]')})]:
            with tempfile.TemporaryDirectory(prefix='erp-p1-null-fixture-') as folder:
                restored=ns['export_table'](df,Path(folder),'nulls')
                pd.testing.assert_frame_equal(restored,df)

    def test_object_null_representations_preserve_missingness(self):
        df=pd.DataFrame({'V':pd.Series([pd.NA,pd.NA],dtype=object)})
        with tempfile.TemporaryDirectory(prefix='erp-p1-object-null-') as folder:
            restored=ns['export_table'](df,Path(folder),'object_nulls')
            self.assertTrue(restored['V'].isna().all())
            self.assertEqual(len(restored),2)

    def test_persisted_evidence_cannot_be_silently_changed(self):
        proposed=ns['assign_evidence'](['0007','0008'], 'initial',0.5,{})
        with tempfile.TemporaryDirectory(prefix='erp-p1-role-fixture-') as folder:
            path=Path(folder)/'roles.parquet'
            proposed.to_parquet(path,index=False)
            ns['validate_evidence_manifest'](proposed,path)
            changed=ns['assign_evidence'](['0007','0008'], 'changed',0.5,{})
            with self.assertRaises(ValueError): ns['validate_evidence_manifest'](changed,path)

    def test_unresolved_headers_block_false_inactivity(self):
        raw = self.tables['orders'].copy()
        conflicted = raw.iloc[[0,1]].copy()
        conflicted['SALESORDER']='BAD'
        conflicted['SALESORDERDATE']=pd.Timestamp('2024-02-01')
        conflicted['TOTALNETAMOUNT']=[50,999]
        raw=pd.concat([raw,conflicted],ignore_index=True)
        views=ns['order_views'](raw)
        self.assertTrue(callable(ns.get('analysis_integrity_issues')), 'Unresolved eligibility must block primary analysis')
        issues=ns['analysis_integrity_issues'](raw,views['headers'],{'0007'})
        self.assertTrue(issues)
        clean=ns['analysis_integrity_issues'](self.tables['orders'],ns['order_views'](self.tables['orders'])['headers'],{'0007'})
        self.assertEqual(clean,[])

    def test_development_customers_without_eligible_orders_remain_accounted_for(self):
        self.assertTrue(callable(ns.get('population_assessment')), 'Do not silently omit zero-eligible-order customers')
        headers=ns['order_views'](self.tables['orders'])['headers']
        result=ns['population_assessment']({'0007','0008'},headers).set_index('CUSTOMERID')
        self.assertEqual(result.loc['0007','SELECTEDORDERS'],3)
        self.assertEqual(result.loc['0008','SELECTEDORDERS'],0)
        self.assertEqual(result.loc['0008','PROFILESTATUS'],'no_eligible_orders_requires_review')

    def test_empty_sources_and_no_silent_behavioural_run(self):
        empty = {name:ns['normalise_table'](pd.DataFrame(columns=spec['columns']), name)[0] for name,spec in ns['SOURCES'].items()}
        report = ns['structural_assessment'](empty)
        self.assertEqual(report['inventory']['ROWS'].sum(), 0)
        self.assertEqual(len(ns['order_views'](empty['orders'])['headers']),0)
        reasons = ns['readiness_issues'](empty, pd.DataFrame(), None, None, False, False, None, None)
        self.assertIn('No order records',reasons)
        self.assertIn('Evidence plan not confirmed',reasons)


synthetic_test_result = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(Phase1Checks))
if not synthetic_test_result.wasSuccessful():
    raise AssertionError("Synthetic Phase 1 checks failed; inspect failures before using outputs")


# In[ ]:


run_record = {
    "IMPLEMENTATION": "phase1-v1", "PYTHON":platform.python_version(),
    "PACKAGES":{name:importlib.metadata.version(name) for name in ["pandas","numpy","pyarrow","duckdb","matplotlib"]},
    "CONFIGURATION":{"ISPRODUCTION":CONFIG.is_production,"OBSERVATIONSTART":OBSERVATION_START,"OBSERVATIONEND":OBSERVATION_END,
        "COVERAGE":ORDER_COVERAGE,"CURRENCY":ANALYSIS_CURRENCY,"ACCEPTEDREASONS":sorted(ACCEPTED_REASON_CODES) if ACCEPTED_REASON_CODES is not None else None,
        "INCLUDEPARTIAL":INCLUDE_PARTIAL_REJECTIONS,"DATEFORMAT":DATE_FORMAT,"DECIMALMARK":DECIMAL_MARK,"MISSINGTOKENS":sorted(MISSING_TOKENS),
        "SPLITSALT":SPLIT_SALT,"EVALUATIONFRACTION":EVALUATION_FRACTION,"EVIDENCECONFIRMED":EVIDENCE_PLAN_CONFIRMED,
        "EXPOSUREREVIEWED":PRIOR_EXPOSURE_REVIEWED,"ELIGIBILITYCONFIRMED":ELIGIBILITY_RULES_CONFIRMED,
        "IDENTIFIERSCONFIRMED":IDENTIFIER_SEMANTICS_CONFIRMED},
    "ANALYSISREADY":ANALYSIS_READY,"BLOCKERS":blocking_issues,
    "SYNTHETICCHECKS":{"RUN":synthetic_test_result.testsRun,"PASSED":synthetic_test_result.wasSuccessful()},
    "EMPIRICALREVIEWCOMPLETE":EMPIRICAL_REVIEW_COMPLETE,
    "LIMITATIONS":"Synthetic checks establish implementation behaviour only; no automatic empirical phase completion",
}
display(pd.DataFrame([{"PROPERTY":key,"VALUE":str(value)} for key,value in run_record.items() if key not in {"PACKAGES","CONFIGURATION"}]))

artifact_tables = {"source_files":source_files,"extraction_register":extraction_register,"field_audit":field_audit,
    "inventory":structure["inventory"],"key_audit":structure["keys"],"relationship_audit":structure["relationships"],
    "date_audit":structure["dates"],"extraction_timeline":extraction_timeline,"code_audit":structure["codes"],"header_audit":views["audit"],"value_flags":value_flags,
    "price_feasibility":price_diagnostics,"measure_assessment":measure_assessment,"decisions":decisions,"open_issues":open_issues,
    "completion_review":completion}
if not evidence.empty: artifact_tables["evidence_manifest"] = evidence
if ANALYSIS_READY:
    artifact_tables.update({"selection_audit":selection_audit,"development_population":population,"history_assessment":histories,
                           "temporal_resolution":resolution_summary,"preparation_sensitivity":sensitivity})
if EXPORT_ARTIFACTS:
    if not synthetic_test_result.wasSuccessful(): raise ValueError("Export requires successful synthetic checks")
    for name,frame in artifact_tables.items():
        if len(frame.columns): export_table(frame,TABLE_DIR,f"p1_{name}")
    if EVIDENCE_PLAN_CONFIRMED and PRIOR_EXPOSURE_REVIEWED and not evidence.empty:
        validate_evidence_manifest(evidence,EVIDENCE_FILE)
        export_table(evidence,EVIDENCE_FILE.parent,EVIDENCE_FILE.stem)
    for name,frame in [("p1_provisional_monthly",profiles),("p1_provisional_quarterly",quarterly_profiles)]:
        if not frame.empty: export_table(frame,PROFILE_DIR,name)
    if figures:
        FIGURE_DIR.mkdir(parents=True,exist_ok=True)
        for name,fig in figures.items(): fig.savefig(FIGURE_DIR/f"p1_{name}.png",dpi=150,bbox_inches="tight")
    run_path = TABLE_DIR/"p1_run_record.json"
    with TemporaryDirectory(prefix=".p1-run-",dir=TABLE_DIR) as work:
        temp_path = Path(work)/run_path.name
        temp_path.write_text(json.dumps(run_record,indent=2,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
        temp_path.replace(run_path)
    print("Exported verified tables and available figures through CONFIG; originals preserved.")
else:
    print("General exports disabled. Analysis-ready runs have already frozen evidence roles before exploration.")


# ### Phase 2 handover checklist
# 
# - Preserve the declared inputs, hashes, parsing contract, evidence manifest and parameter record.
# - Complete extraction metadata and coverage; resolve key conflicts and consequential code semantics.
# - Review the five measures, currency restriction, missing-value effects and comparison support.
# - Record adopted temporal representation, suitability rationale and preparation decisions with evidence.
# - Preserve unresolved optional limitations and avoid reusing development evidence as untouched evaluation.
# - Re-run from a fresh kernel with populated declared inputs. Verify exported schemas, nulls and reconciled
#   order totals, then review framework completion criteria before marking Phase 1 complete.
# 
# The notebook implements the assessment workflow. Empirical results, domain confirmations and final
# recommendations remain the researcher's work until the corresponding evidence has been examined.
# 
