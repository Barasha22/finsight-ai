-- Use correct context
USE DATABASE FINSIGHT_DB;
USE SCHEMA PUBLIC;

-- Table 1: Superstore Sales
CREATE OR REPLACE TABLE SUPERSTORE_SALES (
    ROW_ID          INTEGER,
    ORDER_ID        VARCHAR(50),
    ORDER_DATE      DATE,
    SHIP_DATE       DATE,
    SHIP_MODE       VARCHAR(50),
    CUSTOMER_ID     VARCHAR(50),
    CUSTOMER_NAME   VARCHAR(100),
    SEGMENT         VARCHAR(50),
    COUNTRY         VARCHAR(50),
    CITY            VARCHAR(100),
    STATE           VARCHAR(100),
    POSTAL_CODE     VARCHAR(20),
    REGION          VARCHAR(50),
    PRODUCT_ID      VARCHAR(50),
    CATEGORY        VARCHAR(50),
    SUB_CATEGORY    VARCHAR(50),
    PRODUCT_NAME    VARCHAR(255),
    SALES           FLOAT,
    QUANTITY        INTEGER,
    DISCOUNT        FLOAT,
    PROFIT          FLOAT
);

-- Table 2: Financial Sample
CREATE OR REPLACE TABLE FINANCIAL_SAMPLE (
    SEGMENT             VARCHAR(50),
    COUNTRY             VARCHAR(100),
    PRODUCT             VARCHAR(100),
    DISCOUNT_BAND       VARCHAR(50),
    UNITS_SOLD          FLOAT,
    MANUFACTURING_PRICE FLOAT,
    SALE_PRICE          FLOAT,
    GROSS_SALES         FLOAT,
    DISCOUNTS           FLOAT,
    SALES               FLOAT,
    COGS                FLOAT,
    PROFIT              FLOAT,
    DATE                DATE,
    MONTH_NUMBER        INTEGER,
    MONTH_NAME          VARCHAR(20),
    YEAR                INTEGER
);
