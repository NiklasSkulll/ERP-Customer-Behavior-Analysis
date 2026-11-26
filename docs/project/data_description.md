<div align="center">

# Data description

[![Order Header Pos Data](https://img.shields.io/badge/Order-Header%20and%20Pos-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/001_order_header_pos_data.csv)
[![Customer Master Data](https://img.shields.io/badge/Customer-Master-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/002_customer_master_data.csv)
[![Order SDDOCUMENTREASON Mapping](https://img.shields.io/badge/Order-SDDOCUMENTREASON%20Mapping-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/003_order_sddocumentreason_mapping.csv)
[![Customer INDUSTRY Mapping](https://img.shields.io/badge/Customer-INDUSTRY%20Mapping-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/004_customer_industry_mapping.csv)

</div>

## Table of Contents

- [Overview](#overview)
- [Documentation background](#documentation-background)
- [1 Raw datasets](#1-raw-datasets)
    - [1.1 Order: Header and item data](#11-order-header-and-item-data)
        - [1.1.1 Main dataset](#111-main-dataset)
        - [1.1.2 Lookup and mapping data](#112-lookup-and-mapping-data)
    - [1.2 Customer: Master data](#12-customer-master-data)
        - [1.2.1 Main dataset](#121-main-dataset)
        - [1.2.2 Lookup and mapping data](#122-lookup-and-mapping-data)
    - [1.3 Data relationships](#13-data-relationships)
- [2 Interim datasets](#2-interim-datasets)
    - [2.1 Order: Header data](#21-order-header-data)
- [3 Processed datasets](#3-processed-datasets)
    - [3.1 Customer: Monthly profiles](#31-customer-monthly-profiles)

---

## Overview

This document describes the data basis for analysing changes in customer purchasing behaviour using ERP sales order data. It documents the source datasets and defines the schemas of the enriched order-level interim dataset and the monthly customer profiles by transaction currency. The behavioural analysis uses sales order header information to examine ordering activity, recorded net order values and ordering intervals. Customer industry information provides additional context for grouped analyses.

**The raw data basis consists of two main datasets:**
- **Sales order header and item data:** Order identifiers, customer identifiers, order dates, net order values, currencies and document statuses. The item identifier is retained to assess the source structure. Item-level purchasing characteristics are outside the analytical scope.
- **Customer master data:** Customer identifiers and their assigned industry codes.

Two lookup datasets provide human-readable descriptions of order reasons and customer industries. Document types, processing statuses and rejection statuses are described through the mappings documented below.

**The datasets are organised into three processing stages:**
- **Raw:** Source data and lookup tables used for preparation.
- **Interim:** Validated order-level records enriched with descriptions and customer industry information.
- **Processed:** Monthly customer profiles derived from the interim data, containing order counts, total net order values and average net order values for each customer, calendar month and transaction currency. The schema and calculation rules are specified in Section 3.1.

The documented file paths refer to the example-data environment. Human-readable ERP descriptions are provided in German.

---

## Documentation background

This documentation was compiled as part of the bachelor's thesis project. The field descriptions, value mappings, and business definitions are based on the ERP system's technical documentation and configuration settings. The relevant information was collected, consolidated, and documented to provide a consistent basis for understanding and analyzing the extracted datasets.

---

## 1 Raw datasets

### 1.1 Order: Header and item data

#### 1.1.1 Main dataset

**Data file:** `data/data-example/raw/001_order_header_pos_data.csv`

| **Feature**                     | **Description**                              |
| ------------------------------- | -------------------------------------------- |
| `SALESORDER`                    | Sales order ID                               |
| `SALESORDERTYPE`                | Document Type (OR = Order)                   |
| `OVERALLSDPROCESSSTATUS`        | Overall processing status of the sales order |
| `SDDOCUMENTREASON`              | Reason for the order (ID, Key)               |
| `OVERALLSDDOCUMENTREJECTIONSTS` | Overall rejection status of the sales order  |
| `SALESORDERDATE`                | Sales order date                             |
| `SOLDTOPARTY`                   | Customer ID                                  |
| `TOTALNETAMOUNT`                | Total net value of the order                 |
| `TRANSACTIONCURRENCY`           | Currency of the document                     |
| `SALESORDERITEM`                | Sales order item number (position)           |

**Mapping the values for `OVERALLSDPROCESSSTATUS`:**
- `A` : "Offen" (Open)
- `B` : "In Bearbeitung" (In progress)
- `C` : "Erledigt" (Completed)

**Mapping the values for `SDDOCUMENTREASON`:**
- view `data/data-example/raw/003_order_sddocumentreason_mapping.csv`

**Mapping the values for `OVERALLSDDOCUMENTREJECTIONSTS`:**
- `A` : "Nichts abgesagt" (Nothing rejected)
- `B` : "Teilweise abgesagt" (Partially rejected)
- `C` : "Alles abgesagt" (Fully rejected)

**Mapping the values for `TRANSACTIONCURRENCY`:**
- `EUR` : Euros
- `GBP` : British pounds sterling

> **Data granularity and analytical scope:**
>- The field table above lists the source columns used in this project. The source dataset contains order-item rows, so header-level attributes may be repeated across several rows belonging to the same `SALESORDER`.
>- `SALESORDERITEM` identifies the item within an order. Together with `SALESORDER`, it supports checks of the source granularity and duplicate records. It is not used as a behavioural measure and is not included in the order-level interim dataset.
>- The analysis uses header-level information. Product identifiers, product characteristics, quantities and item-level prices are outside the selected analytical scope.

**Preparation requirements:**
- Verify the source granularity and investigate duplicate combinations of `SALESORDER` and `SALESORDERITEM`.
- Check that repeated header attributes agree within each `SALESORDER`.
- Resolve or explicitly record conflicting header values before constructing the order-level dataset. Do not select an arbitrary row to conceal inconsistencies.
- Retain `TOTALNETAMOUNT` once per order. Repeated header amounts across item rows must not be summed.
- Preserve the original source files and document the transformations used to construct the interim dataset.
- Record the extraction date, covered date range, observed source formats and any known extraction gaps during data assessment.

#### 1.1.2 Lookup and mapping data

**Data file:** `data/data-example/raw/003_order_sddocumentreason_mapping.csv`

| **Feature**             | **Description**                                |
| ----------------------- | ---------------------------------------------- |
| `SDDOCUMENTREASON`      | Reason for the order (ID, Key)                 |
| `SDDOCUMENTREASON_TEXT` | Human-readable description of the order reason |

### 1.2 Customer: Master data

#### 1.2.1 Main dataset

**Data file:** `data/data-example/raw/002_customer_master_data.csv`

| **Feature** | **Description**               |
| ----------- | ----------------------------- |
| `CUSTOMER`  | Customer ID                   |
| `INDUSTRY`  | Customer's industry (ID, Key) |

**Mapping the values for `INDUSTRY`:**
- view `data/data-example/raw/004_customer_industry_mapping.csv`

#### 1.2.2 Lookup and mapping data

**Data file:** `data/data-example/raw/004_customer_industry_mapping.csv`

| **Feature**     | **Description**                                       |
| --------------- | ----------------------------------------------------- |
| `INDUSTRY`      | Customer's industry (ID, Key)                         |
| `INDUSTRY_TEXT` | Human-readable description of the customer's industry |

### 1.3 Data relationships

The following relationships are used to enrich the order-level dataset. The expected relationship cardinalities must be verified against the available extracts before joining the tables.

| **Initial dataset** | **Target dataset**   | **Join fields**                          | **Expected relationship**                  |
| ------------------- | -------------------- | ---------------------------------------- | ------------------------------------------ |
| Order-level records | Customer master      | `SOLDTOPARTY` to `CUSTOMER`              | Many orders to one customer record         |
| Order-level records | Order reason mapping | `SDDOCUMENTREASON` to `SDDOCUMENTREASON` | Many orders to one reason description      |
| Customer master     | Industry mapping     | `INDUSTRY` to `INDUSTRY`                 | Many customers to one industry description |

**Join requirements:**
- Verify the uniqueness of `CUSTOMER` in the customer master, `SDDOCUMENTREASON` in the order reason mapping, and `INDUSTRY` in the industry mapping.
- Resolve conflicting assignments before joining. Do not use arbitrary deduplication to select between different descriptions or industry assignments.
- Use left joins so that orders without a matching customer or description remain available.
- Do not match missing join keys to one another.
- Preserve identifiers and codes as strings, including leading zeros.
- Report unmatched keys and the number of affected orders.
- Verify that enrichment does not change the number of order-level records or the total net order amount within each currency.

The customer industry is obtained from the available customer master extract. Unless historical assignments are available, it represents the industry recorded in that extract and must not be interpreted as a verified historical assignment at each order date.

---

## 2 Interim datasets

### 2.1 Order: Header data

**Purpose:**
- Provide a consistent order-level basis for customer time series, grouped summaries and traceable explanations of detected changes.

**Granularity:**
- Exactly one row per uniquely identified sales order.

**Primary key:**
- `SALESORDER`.
- Missing identifiers and unresolved conflicting header values must be investigated and documented before affected records can be represented in this table.

**Coverage:**
- The table retains technically validated orders together with their document types, processing statuses and rejection statuses.
- Inclusion in this table does not establish analytical eligibility.
- Business selection rules are applied explicitly when constructing analytical measures.

**Column naming:**
- Original ERP codes retain their field names.
- Human-readable descriptions use the corresponding field name followed by `_TEXT`.

**Target schema:**
- **Data file:** `data/data-example/interim/001_order_header_data.csv`
- The data types below describe the logical types used during processing. CSV files store their textual representations.

| **Feature**                          | **Data type** | **Description**                                    |
| ------------------------------------ | ------------- | -------------------------------------------------- |
| `SALESORDER`                         | String        | Unique sales order identifier                      |
| `SALESORDERTYPE`                     | String        | Document type code                                 |
| `SALESORDERTYPE_TEXT`                | String        | Human-readable document type description           |
| `OVERALLSDPROCESSSTATUS`             | String        | Overall processing status code                     |
| `OVERALLSDPROCESSSTATUS_TEXT`        | String        | Human-readable processing status description       |
| `SDDOCUMENTREASON`                   | String        | Order reason code                                  |
| `SDDOCUMENTREASON_TEXT`              | String        | Human-readable order reason description            |
| `OVERALLSDDOCUMENTREJECTIONSTS`      | String        | Overall rejection status code                      |
| `OVERALLSDDOCUMENTREJECTIONSTS_TEXT` | String        | Human-readable rejection status description        |
| `SALESORDERDATE`                     | Date          | Sales order date                                   |
| `TOTALNETAMOUNT`                     | Decimal       | Recorded net order amount, retained once per order |
| `TRANSACTIONCURRENCY`                | String        | Currency of the recorded net order amount          |
| `SOLDTOPARTY`                        | String        | Customer identifier of the ordering party          |
| `INDUSTRY`                           | String        | Industry code obtained from the customer master    |
| `INDUSTRY_TEXT`                      | String        | Human-readable industry description                |

**Field origins:**
- Order identifiers, document codes, dates, customer identifiers, amounts and currencies originate from the raw order dataset.
- `INDUSTRY` is obtained by joining `SOLDTOPARTY` to `CUSTOMER` in the customer master.

| **Description field**                | **Source**                                                     |
| ------------------------------------ | -------------------------------------------------------------- |
| `SALESORDERTYPE_TEXT`                | Documented document-type mapping: `OR` > `Auftrag`             |
| `OVERALLSDPROCESSSTATUS_TEXT`        | Processing-status mapping documented in Section 1.1.1          |
| `SDDOCUMENTREASON_TEXT`              | `data/data-example/raw/003_order_sddocumentreason_mapping.csv` |
| `OVERALLSDDOCUMENTREJECTIONSTS_TEXT` | Rejection-status mapping documented in Section 1.1.1           |
| `INDUSTRY_TEXT`                      | `data/data-example/raw/004_customer_industry_mapping.csv`      |

Any additional document types require a verified mapping before their descriptions are assigned. An unknown code is retained even when its description is unavailable.

**Construction and validation rules:**
- Parse identifiers, dates and monetary values according to the verified source formats.
- Check consistency across repeated header values before retaining one record per `SALESORDER`.
- Retain the existing `TOTALNETAMOUNT`. Do not calculate it by summing repeated header values across items.
- Apply the join requirements defined in Section 1.3.
- Verify the uniqueness of `SALESORDER` after construction and enrichment.
- Report unresolved inconsistencies, missing required values and unmatched mappings, including their effects on analytical usability.

**Missing values and interpretation:**
- Missing customer or mapping records do not automatically remove an order. Unavailable industry assignments and descriptions remain missing and are reported. Missing monetary values are not replaced with zero.
- `TOTALNETAMOUNT` represents the recorded net order amount. It is not automatically equivalent to invoiced or realised revenue. For partially rejected orders, the meaning of the stored amount must be clarified before it is used in affected analytical measures.
- Amounts in different currencies must not be summed without a documented conversion or restriction to a common currency. The original currency remains available in this table.
- Open or in-progress orders are not considered invalid solely because processing is incomplete. The treatment of fully and partially rejected orders in analytical measures follows the documented order-eligibility rules.

**CSV representation:**
- **Encoding:** UTF-8.
- **Field separator:** `;`.
- **Dates:** `YYYY-MM-DD`.
- **Monetary values:** decimal point, no thousands separators, preserving the source precision.
- **Missing values:** empty fields.
- **Identifiers and codes:** loaded explicitly as strings to preserve leading zeros and valid code values.

After export and reloading, verify that identifiers, dates, monetary values and missing values are preserved.

---

## 3 Processed datasets

Processed datasets contain analytical measures derived from the enriched order-level interim dataset. They provide the basis for descriptive summaries, comparisons between observation periods and the subsequent detection and classification of purchasing behaviour changes.

### 3.1 Customer: Monthly profiles

**Purpose:**
- Represent each customer's monthly ordering activity and recorded net order values.
- The table supports customer-level analysis and aggregation to industry-level and overall summaries.

**Granularity:**
- One row per customer, calendar month and transaction currency.

**Composite key:**
- `CUSTOMER_ID`, `PERIODSTART`, `TRANSACTIONCURRENCY`.

Monthly aggregation defines the basic analytical representation. It does not require change detection to compare individual months; longer comparison windows can be constructed from these profiles.

**Target schema:**
- **Data file:** `data/data-example/processed/001_customer_monthly_profiles.csv`
- **Source:** `data/data-example/interim/001_order_header_data.csv`
- The data types below describe logical types used during processing. Analytical measures may contain missing values where the available data do not support their calculation.

| **Feature**           | **Data type** | **Description**                                                         |
| --------------------- | ------------- | ----------------------------------------------------------------------- |
| `CUSTOMER_ID`         | String        | Customer identifier, derived from `SOLDTOPARTY`                         |
| `INDUSTRY`            | String        | Customer industry code                                                  |
| `INDUSTRY_TEXT`       | String        | Human-readable customer industry description                            |
| `PERIODSTART`         | Date          | First calendar day of the represented month                             |
| `ORDERCOUNT`          | Integer       | Number of distinct eligible orders for the customer, month and currency |
| `TOTALORDERNETVALUE`  | Decimal       | Sum of recorded net amounts across those eligible orders                |
| `AVGORDERNETVALUE`    | Decimal       | Average recorded net amount per eligible order                          |
| `TRANSACTIONCURRENCY` | String        | Currency to which the order count and monetary measures refer           |

**Calculation rules:**
- Orders are assigned to customers using `SOLDTOPARTY` and to calendar months using `SALESORDERDATE`.
- The month is represented by its first calendar day, for example `2026-03-01`.

Apply the documented order-eligibility rules before calculating the measures. Use the same eligible order population for all three measures within each customer-month-currency combination.

| **Measure**          | **Calculation**                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------- |
| `ORDERCOUNT`         | Count distinct eligible `SALESORDER` values                                                                     |
| `TOTALORDERNETVALUE` | Sum `TOTALNETAMOUNT` once per eligible order                                                                    |
| `AVGORDERNETVALUE`   | Divide `TOTALORDERNETVALUE` by `ORDERCOUNT`, provided the total is available and the count is greater than zero |

If an eligible order has an unavailable net amount, do not silently calculate a complete total from the remaining orders. The order count may remain available, while the affected total and average are recorded as missing.

The exact eligibility settings, observation boundaries and treatment of partially rejected orders must be documented before generating the analytical dataset.

**Periods without orders and missing coverage:**
- _Construct monthly profiles for relevant customer-currency combinations within a justified observation interval:_
    - Where observation coverage is complete and no eligible orders are recorded, set `ORDERCOUNT` and `TOTALORDERNETVALUE` to zero.
    - Leave `AVGORDERNETVALUE` missing when `ORDERCOUNT` is zero.
    - Do not interpret missing extraction coverage or incomplete observation months as zero activity. Identify affected periods and document their treatment.
    - Do not end a customer's observation interval at their last recorded order merely because no later orders exist.
    - Do not require orders in every month or year as a condition for retaining a customer.

A zero count in one currency does not establish inactivity across all currencies.

**Currency and industry treatment:**
- Keep EUR and GBP separate. Monetary totals and averages may only be combined after a documented conversion to a common currency. Order counts can be summed across currencies where each order occurs in exactly one currency group.
- Industry information is inherited from the customer assignment used in the interim dataset. Missing industry assignments do not exclude customers from customer-level or overall analyses. Industry summaries must identify the contribution of customers with unknown industry assignments.
- Unless historical customer master data are available, industry assignments describe the available master-data snapshot.

**Aggregation to broader summaries:**
- The same table supports monthly overall summaries, monthly industry summaries and longer customer comparison windows.
- Sum `ORDERCOUNT` and `TOTALORDERNETVALUE` over the relevant rows, respecting currency and data-coverage requirements. Recalculate the average order value as the aggregated total order value divided by the aggregated order count. Do not use an unweighted average of customer-level or monthly averages.
- If any contributing `TOTALORDERNETVALUE` is missing, the aggregated `TOTALORDERNETVALUE` and the corresponding `AVGORDERNETVALUE` must remain missing. Do not silently omit missing amounts or replace them with zero when calculating complete totals. This rule applies to industry-level summaries, overall summaries and comparisons based on multiple months. Order counts may still be aggregated where the contributing counts are complete.
- A partial sum of available net order values may be reported separately, but it must be explicitly labelled as incomplete and accompanied by information about its coverage. It must not replace the complete aggregate or be presented as the total net order value of the entire group or period.

**Validation and interpretation:**
- Verify the uniqueness of the composite key.
- Reconcile order counts and monetary totals with the eligible interim records, separately by month and currency.
- Verify that adding zero-activity periods does not change order counts or monetary totals.
- Check formulas and missing-value handling, including zero-order periods and incomplete monetary information.
- Preserve identifiers and codes as strings, including leading zeros.

The measures describe recorded ordering activity and net order amounts. They do not establish realised revenue, purchased quantities or the causes of observed changes. `ORDERCOUNT`, `TOTALORDERNETVALUE` and `AVGORDERNETVALUE` are mathematically related and must not be treated as independent evidence of a behavioural change.

**File representation:**
- Use UTF-8 encoding, semicolon-separated fields, dates in `YYYY-MM-DD` format and decimal points for monetary values.
- Represent missing values as empty fields.
- Preserve the monetary precision used during calculation and apply presentation rounding only when displaying results.
