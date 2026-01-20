from utils.exporter import save_clean_transactions, save_metrics

# Sample data to test
valid_transactions = [
    {
        'TransactionID': 'T001',
        'Date': '2024-12-01',
        'ProductID': 'P101',
        'ProductName': 'Laptop',
        'Quantity': 2,
        'UnitPrice': 45000,
        'CustomerID': 'C001',
        'Region': 'North'
    },
    {
        'TransactionID': 'T002',
        'Date': '2024-12-02',
        'ProductID': 'P102',
        'ProductName': 'Mouse',
        'Quantity': 5,
        'UnitPrice': 500,
        'CustomerID': 'C002',
        'Region': 'South'
    }
]

metrics_summary = {
    "total_revenue": 100000,
    "revenue_by_region": {"North": 90000, "South": 10000},
    "top_products": [("Laptop", 2, 90000), ("Mouse", 5, 10000)]
}

# Save files
save_clean_transactions(valid_transactions)
save_metrics(metrics_summary)

