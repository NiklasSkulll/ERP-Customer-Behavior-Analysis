<div align="center">

# Data description

[![Order Header Pos Data](https://img.shields.io/badge/Order-Header%20and%20Pos-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/001_order_header_pos_data_eg.csv)
[![Product Master Data](https://img.shields.io/badge/Product-Master-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/002_product_master_data_eg.csv)
[![Product Price Data](https://img.shields.io/badge/Product-Prices-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/003_product_price_data_eg.csv)
[![Customer Master Data](https://img.shields.io/badge/Customer-Master-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/004_customer_master_data_eg.csv)

[![Order SDDOCUMENTREASON Mapping](https://img.shields.io/badge/Order-SDDOCUMENTREASON%20Mapping-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/005_order_sddocumentreason_mapping_eg.csv)
[![Product PRODUCTGROUP Mapping](https://img.shields.io/badge/Product-PRODUCTGROUP%20Mapping-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/006_product_productgroup_mapping_eg.csv)
[![Product CONDITIONTYPE Mapping](https://img.shields.io/badge/Order-CONDITIONTYPE%20Mapping-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/007_product_conditiontype_mapping_eg.csv)
[![Customer INDUSTRY Mapping](https://img.shields.io/badge/Customer-INDUSTRY%20Mapping-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/008_customer_industry_mapping_eg.csv)

</div>

## Table of Contents

- [Overview](#overview)
- [Documentation background](#documentation-background)
- [1 Order: Header and item data](#1-order-header-and-item-data)
    - [1.1 Main data set](#11-main-data-set)
    - [1.2 Lookup and mapping data](#12-lookup-and-mapping-data)
- [2 Product: Master data](#2-product-master-data)
    - [2.1 Main data set](#21-main-data-set)
    - [2.2 Lookup and mapping data](#22-lookup-and-mapping-data)
- [3 Product: Price data](#3-product-price-data)
    - [3.1 Main data set](#31-main-data-set)
    - [3.2 Lookup and mapping data](#32-lookup-and-mapping-data)
- [4 Customer: Master data](#4-customer-master-data)
    - [4.1 Main data set](#41-main-data-set)
    - [4.2 Lookup and mapping data](#42-lookup-and-mapping-data)
- [Data relationships](#data-relationships)

---

## Overview

This document provides an overview of the datasets extracted from the ERP system for this data analytics project. It describes the structure, technical fields, and business meaning of the data, including relevant value mappings and data interpretation rules.

**The documentation covers four main datasets:**
- **Sales order header and item data:** Sales order header and item information, including customers, products, quantities, order values, and processing statuses.
- **Product master data:** Product identifiers, product groups, units of measure, and product descriptions.
- **Product price data:** Pricing conditions, prices, customer-specific pricing information, and validity periods.
- **Customer master data:** Customer identifiers, names, postal codes, industries, and customer price groups.

Additional **lookup and mapping datasets** provide human-readable descriptions for selected ERP codes, such as order reasons, product groups, pricing condition types, and customer industries.

Each section documents the available fields, their meanings, and relevant considerations for data processing and analysis. The referenced CSV files contain example data corresponding to the documented structures. Textual values and descriptions are provided in German.

---

## Documentation background

This documentation was compiled as part of the bachelor's thesis project. The field descriptions, value mappings, and business definitions are based on the ERP system's technical documentation and configuration settings. The relevant information was collected, consolidated, and documented to provide a consistent basis for understanding and analyzing the extracted datasets.

---

## 1 Order: Header and item data

### 1.1 Main data set

**Data file:** `data/data-example/raw/001_order_header_pos_data_eg.csv`

| **Feature**                     | **Description**                                              |
| ------------------------------- | ------------------------------------------------------------ |
| `SALESORDER`                    | Sales order ID                                               |
| `SALESORDERTYPE`                | Document Type (OR = Order)                                   |
| `OVERALLSDPROCESSSTATUS`        | Overall processing status of the sales order                 |
| `SDDOCUMENTREASON`              | Reason for the order (ID, Key)                               |
| `OVERALLSDDOCUMENTREJECTIONSTS` | Overall rejection status of the sales order                  |
| `SALESORDERDATE`                | Sales order date                                             |
| `SOLDTOPARTY`                   | Customer ID                                                  |
| `TOTALNETAMOUNT`                | Total net value of the order                                 |
| `TRANSACTIONCURRENCY`           | Currency of the document                                     |
| `SALESORDERITEM`                | Sales order item number (position)                           |
| `MATERIAL`                      | Product ID                                                   |
| `CONFDDELIVQTYINORDERQTYUNIT`   | Confirmed delivery quantity in the sales order quantity unit |

**Mapping the values for `OVERALLSDPROCESSSTATUS`:**
- `A` : "Offen" (Open)
- `B` : "In Bearbeitung" (In progress)
- `C` : "Erledigt" (Completed)

**Mapping the values for `SDDOCUMENTREASON`:**
- view `data/data-example/raw/005_order_sddocumentreason_mapping_eg.csv`

**Mapping the values for `OVERALLSDDOCUMENTREJECTIONSTS`:**
- `A` : "Nichts abgesagt" (Nothing rejected)
- `B` : "Teilweise abgesagt" (Partially rejected)
- `C` : "Alles abgesagt" (Fully rejected)

**Mapping the values for `TRANSACTIONCURRENCY`:**
- `EUR` : Euros
- `GBP` : British pounds sterling

> **Important to note!**
>- **Data Granularity and Structure:** This dataset combines sales order header information with item-level information. Header-level attributes, such as the customer, order status, and total net amount, may be repeated across multiple rows belonging to the same sales order.
>- `TOTALNETAMOUNT` is located at the order level (order header) and may appear multiple times in the line items within this data record.

**Important:** When aggregating header-level values, repeated information must be considered to avoid double-counting.

### 1.2 Lookup and mapping data

**Data file:** `data/data-example/raw/005_order_sddocumentreason_mapping_eg.csv`

| **Feature**            | **Description**                                |
| ---------------------- | ---------------------------------------------- |
| `SDDOCUMENTREASON`     | Reason for the order (ID, Key)                 |
| `SDDOCUMENTREASONTEXT` | Human-readable description of the order reason |

---

## 2 Product: Master data

### 2.1 Main data set

**Data file:** `data/data-example/raw/002_product_master_data_eg.csv`

| **Feature**                    | **Description**                     |
| ------------------------------ | ----------------------------------- |
| `PRODUCT`                      | Product ID                          |
| `PRODUCTGROUP`                 | Product category or group (ID, Key) |
| `TO_PLANT_BASEUNIT`            | Base unit of measure                |
| `TO_PRODUCTBASICTEXT_LONGTEXT` | Long product description            |

**Mapping the values for `PRODUCTGROUP`:**
- view `data/data-example/raw/006_product_productgroup_mapping_eg.csv`

**Mapping the values for `TO_PLANT_BASEUNIT`:**
- `M`  : "Meter"
- `PC` : "Stück" (Pieces)
- `ROL`: "Rolle" (Roll)
- `ZBU`: "Bund" (Bundle)

### 2.2 Lookup and mapping data

**Data file:** `data/data-example/raw/006_product_productgroup_mapping_eg.csv`

| **Feature**        | **Description**                                             |
| ------------------ | ----------------------------------------------------------- |
| `PRODUCTGROUP`     | Product category or group (ID, Key)                         |
| `PRODUCTGROUPTEXT` | Human-readable description of the product category or group |

---

## 3 Product: Price data

### 3.1 Main data set

**Data file:** `data/data-example/raw/003_product_price_data_eg.csv`

| **Feature**                  | **Description**                                              |
| ---------------------------- | ------------------------------------------------------------ |
| `MATERIAL`                   | Product ID                                                   |
| `CONDITIONVALIDITYSTARTDATE` | Start date for the validity of the catalog price or discount |
| `CONDITIONVALIDITYENDDATE`   | End date for the validity of the catalog price or discount   |
| `CUSTOMERPRICEGROUP`         | Customer price group or category                             |
| `CUSTOMER`                   | Customer ID                                                  |
| `CONDITIONTYPE`              | Pricing condition type (ID, Key)                             |
| `CONDITIONRATEVALUE`         | Condition rate value                                         |
| `CONDITIONRATEVALUEUNIT`     | Currency or unit of the condition rate                       |

**Mapping the values for `CONDITIONTYPE`:**
- view `data/data-example/raw/007_product_conditiontype_mapping_eg.csv`

**Mapping the values for `CONDITIONRATEVALUEUNIT`:**
- `EUR` : Euros

> **Important to note!**
>- For the **"Price per item before discount"**, `CONDITIONTYPE` is filtered to "List price" (`"Price per item before discount" = "List price"`).
>- For the **"Discount (Percentage)"**, the "Price per item after discount" is subtracted from the "List price" and divided by the "List price" (`"Discount (Percentage)" = ("List price" - "Price per item after discount") / "List price" * 100`).
>- For the **"Discount (Amount)"**, the "Price per item after discount" is subtracted from the "List price" (`"Discount (Amount)" = "List price" - "Price per item after discount"`).
>- If `CONDITIONRATEVALUE` has the default value of `999999` or `999999,00`, this means that the price has not been maintained. This is a placeholder for a missing price.
>- Pay attention to the validity of the values. The validity period is between `CONDITIONVALIDITYSTARTDATE` and `CONDITIONVALIDITYENDDATE`.
>- If **"List price" is null or `0`**, the "Discount (Amount)" and "Discount (Percentage)" cannot be calculated.

### 3.2 Lookup and mapping data

**Data file:** `data/data-example/raw/007_product_conditiontype_mapping_eg.csv`

| **Feature**         | **Description**                                          |
| ------------------- | -------------------------------------------------------- |
| `CONDITIONTYPE`     | Pricing condition type (ID, Key)                         |
| `CONDITIONTYPETEXT` | Human-readable description of the pricing condition type |

---

## 4 Customer: Master data

### 4.1 Main data set

**Data file:** `data/data-example/raw/004_customer_master_data_eg.csv`

| **Feature**          | **Description**                  |
| -------------------- | -------------------------------- |
| `CUSTOMER`           | Customer ID                      |
| `CUSTOMERFULLNAME`   | Full name of the customer        |
| `POSTALCODE`         | Postal code of the customer      |
| `INDUSTRY`           | Customer's industry (ID, Key)    |
| `CUSTOMERPRICEGROUP` | Customer price group or category |

**Mapping the values for `INDUSTRY`:**
- view `data/data-example/raw/008_customer_industry_mapping_eg.csv`

### 4.2 Lookup and mapping data

**Data file:** `data/data-example/raw/008_customer_industry_mapping_eg.csv`

| **Feature**    | **Description**                                       |
| -------------- | ----------------------------------------------------- |
| `INDUSTRY`     | Customer's industry (ID, Key)                         |
| `INDUSTRYTEXT` | Human-readable description of the customer's industry |

---

## Data relationships

The following table summarizes the identified field relationships between the datasets. The uniqueness of the join keys and the corresponding relationship cardinalities will be examined during the subsequent data analysis.

| **Initial dataset**         | **Target dataset**     | **Feature mapping**                      |
| --------------------------- | ---------------------- | ---------------------------------------- |
| Sales order header and item | Product master         | `MATERIAL` to `PRODUCT`                  |
| Sales order header and item | Customer Master        | `SOLDTOPARTY` to `CUSTOMER`              |
| Product price               | Product master         | `MATERIAL` to `PRODUCT`                  |
| Product price               | Customer master        | `CUSTOMER` to `CUSTOMER`                 |
| Sales order header and item | Order reason mapping   | `SDDOCUMENTREASON` to `SDDOCUMENTREASON` |
| Product master              | Product group mapping  | `PRODUCTGROUP` to `PRODUCTGROUP`         |
| Product price               | Condition type mapping | `CONDITIONTYPE` to `CONDITIONTYPE`       |
| Customer master             | Industry mapping       | `INDUSTRY` to `INDUSTRY`                 |
