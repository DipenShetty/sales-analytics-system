from utils.report_generator import generate_sales_report
from utils.api_handler import fetch_all_products, create_product_mapping, enrich_sales_data, save_enriched_data

# Example cleaned transactions
transactions = [
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

# Enrich transactions using API
api_products = fetch_all_products()
product_mapping = create_product_mapping(api_products)
enriched_transactions = enrich_sales_data(transactions, product_mapping)
save_enriched_data(enriched_transactions)

# Generate report
generate_sales_report(transactions, enriched_transactions)
print("Report generated successfully in output/sales_report.txt")
