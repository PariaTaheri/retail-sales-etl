# 🛒 Retail Sales ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Project-Complete-success)

---

## 📌 Project Overview

This project implements a complete ETL (Extract, Transform, Load) pipeline for retail sales data.

The goal of this project is to simulate a real-world data engineering workflow, including data ingestion, data cleaning, and storing structured data in a database.

---
## 🧱 Architecture Diagram

```mermaid
graph LR
A[Raw CSV Data] --> B[Extract]
B --> C[Transform (Pandas)]
C --> D[Clean Data]
D --> E[Load to SQLite]
E --> F[Validation Query]

---

# ✅ 🧩 قسمت 3 (Tech Stack)

```markdown
## ⚙️ Tech Stack

- Python  
- Pandas  
- SQLite  
- Git & GitHub  
- VS Code  

---
## 📂 Project Structure

retail-sales-etl/
│
├── data/                # Ignored (raw & processed data)
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── requirements.txt
├── .gitignore
└── README.md

---
## 🔄 ETL Pipeline Steps

### 1. Extract
Load raw CSV data

### 2. Transform
- Handle missing values  
- Convert data types  
- Clean dataset  

### 3. Load
Store processed data in SQLite database

### 4. Validate
Query database to verify results  

---
## 🚀 How to Run

pip install -r requirements.txt  
python src/pipeline.py  

---

## 📸 Sample Output

Data loaded into database  
[5 rows x 21 columns]  
Pipeline completed successfully  

---
## 🧠 Key Learnings

- Building modular ETL pipelines  
- Data transformation with Pandas  
- Working with SQLite  
- Version control using Git  
- Structuring real-world data projects  

---

## 🔮 Future Improvements

- Add logging system  
- Add configuration file (YAML/JSON)  
- Integrate Apache Airflow  
- Add unit tests  

---

## 👩‍💻 Author

Paria Taheri 