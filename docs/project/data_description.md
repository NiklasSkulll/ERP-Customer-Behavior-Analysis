<div align="center">

# Data description

[![Order Header Pos Data](https://img.shields.io/badge/Order-Header%20and%20Pos-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/001_order_header_pos_data.csv)
[![Product Master Data](https://img.shields.io/badge/Product-Master-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/002_product_master_data.csv)
[![Product Price Data](https://img.shields.io/badge/Product-Prices-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/003_product_price_data.csv)
[![Customer Master Data](https://img.shields.io/badge/Customer-Master-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/004_customer_master_data.csv)
[![Customer Industry Mapping Data](https://img.shields.io/badge/Customer-Industry%20Mapping-%23352898?style=flat&labelColor=%2315934E)](data/data-example/raw/005_customer_industry_mapping_data.csv)

</div>

## Table of Contents

- [Overview](#overview)
- [Order: Header and position data](#order-header-and-position-data)
- [Product: Master data](#product-master-data)
- [Product: Price data](#product-price-data)
- [Customer: Master data](#customer-master-data)
- [Customer: Industry mapping data](#customer-industry-mapping-data)

---

## Overview

...

---

## Order: Header and position data

**Data file:** `data/data-example/raw/001_order_header_pos_data.csv`

| **Feature**                     | **Description**                       |
| ------------------------------- | ------------------------------------- |
| `SALESORDER`                    | Sales order ID (number)               |
| `SALESORDERTYPE`                |                                       |
| `OVERALLSDPROCESSSTATUS`        |                                       |
| `SDDOCUMENTREASON`              |                                       |
| `OVERALLSDDOCUMENTREJECTIONSTS` |                                       |
| `SALESORDERDATE`                |                                       |
| `SOLDTOPARTY`                   | Customer ID                           |
| `TOTALNETAMOUNT`                |                                       |
| `TRANSACTIONCURRENCY`           |                                       |
| `SALESORDERITEM`                | Position number, of the ordered items |
| `MATERIAL`                      | Product ID (number)                   |
| `CONFDDELIVQTYINORDERQTYUNIT`   |                                       |

---

## Product: Master data

**Data file:** `data/data-example/raw/002_product_master_data.csv`

| **Feature**                    | **Description**     |
| ------------------------------ | ------------------- |
| `PRODUCT`                      | Product ID (number) |
| `PRODUCTGROUP`                 |                     |
| `TO_PLANT_BASEUNIT`            |                     |
| `TO_PRODUCTBASICTEXT_LONGTEXT` |                     |

---

## Product: Price data

**Data file:** `data/data-example/raw/003_product_price_data.csv`

| **Feature**                  | **Description**     |
| ---------------------------- | ------------------- |
| `MATERIAL`                   | Product ID (number) |
| `CONDITIONVALIDITYSTARTDATE` |                     |
| `CONDITIONVALIDITYENDDATE`   |                     |
| `CUSTOMERPRICEGROUP`         |                     |
| `CUSTOMER`                   | Customer ID         |
| `CONDITIONTYPE`              |                     |
| `CONDITIONRATEVALUE`         |                     |
| `CONDITIONRATEVALUEUNIT`     |                     |

---

## Customer: Master data

**Data file:** `data/data-example/raw/004_customer_master_data.csv`

| **Feature**          | **Description**             |
| -------------------- | --------------------------- |
| `CUSTOMER`           | Customer ID                 |
| `CUSTOMERFULLNAME`   | Full name of the customer   |
| `POSTALCODE`         | Postal code of the customer |
| `INDUSTRY`           |                             |
| `CUSTOMERPRICEGROUP` |                             |

---

## Customer: Industry mapping data

**Data file:** `data/data-example/raw/005_customer_industry_mapping_data.csv`

| **Feature**    | **Description** |
| -------------- | --------------- |
| `INDUSTRY`     |                 |
| `INDUSTRYNAME` |                 |
