 Sales Analytics System

 Overview
This project is a **Sales Analytics System** built in Python. It performs the following workflow:

1. Reads raw sales data from `data/sales_data.txt`.
2. Cleans and validates transactions.
3. Generates summary metrics.
4. Enriches transactions with product information via API.
5. Saves cleaned and enriched data.
6. Generates a comprehensive sales report (`output/sales_report.txt`).

 Repository Structure

├── data/
│   ├── enriched_sales_data.txt
│   └── sales_data.txt
│
├── output/
│   ├── clean_transactions.csv
│   ├── metrics_summary.json
│   └── sales_report.txt
│
├── utils/
│   ├── __pycache__/
│   ├── api_handler.py
│   ├── data_processor.py
│   ├── exporter.py
│   ├── file_handler.py
│   ├── metrics.py
│   └── report_generator.py
│
├── main.py
├── README.md
├── requirements.txt
├── test_enrichment.py
├── test_exporter.py
└── test_report.py

## How to Run

1. Clone the repository:

```bash
git clone <your_repo_url>
cd sales-analytics-system

2. Install dependencies:

pip install -r requirements.txt

3. Run the full workflow:

python main.py

4. Check outputs in the output/ folder.

Notes

The API used is a dummy product API for enrichment purposes.

All Python scripts are located inside the utils/ folder.

3. Save the file (**Ctrl + S**).  

---

# **Step 3: Push to GitHub**

### **A. Initialize Git (if not already done)**

1. Open terminal at project root:

```powershell
git init

2. Add all files:

git add .

3. Commit changes:

git commit -m "Final submission: complete sales analytics system"



