# 🚀 Mastering PySpark in Databricks

Welcome to my dedicated repository for learning and mastering **PySpark** within the **Databricks** environment. This repository serves as a portfolio of my hands-on practice, data engineering notebooks, and implementations of core Apache Spark concepts.

The goal of this project is to build production-grade skills in distributed data processing, data manipulation, and building scalable ETL/ELT pipelines.

---

## 🧠 Key Concepts & Skills Covered

This repository documents my practical execution of the following core areas:

- **PySpark Core & DataFrames:** Reading/writing diverse formats (CSV, JSON, Parquet, Delta), schema definitions (`StructType`, `StructField`), and data cleaning.
- **Data Transformations:** Using built-in functions (`pyspark.sql.functions`), conditional operations (`when`, `otherwise`), aggregations, joins, and window functions.
- **Spark SQL Integration:** Querying distributed datasets using ANSI-compliant SQL syntax inside Databricks notebooks.
- **Delta Lake Architecture:** Working with Delta tables, ACID transactions, time travel queries, and optimizations like `OPTIMIZE` and `Z-ORDER`.
- **Performance & Tuning:** Understanding caching strategies (`.cache()`, `.persist()`), data partitioning vs. bucketing, and diagnosing bottlenecks.

---

## 📂 Repository Structure

*Feel free to adapt this structure as you commit your notebooks!*

```text
├── 01_Basics/
│   ├── 01_Spark_Session_and_Data_Reading.ipynb
│   └── 02_DataFrame_Essentials.ipynb
├── 02_Transformations/
│   ├── 01_Filtering_and_Aggregations.ipynb
│   ├── 02_Joins_and_Window_Functions.ipynb
│   └── 03_UDFs_and_Advanced_Built_Ins.ipynb
├── 03_Delta_Lake/
│   ├── 01_Delta_Table_Basics.ipynb
│   └── 02_Time_Travel_and_Optimization.ipynb
├── 04_Projects/
│   └── ETL_Pipeline_Example.ipynb
└── README.md
