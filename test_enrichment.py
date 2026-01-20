from utils.api_handler import fetch_all_products, create_product_mapping, enrich_sales_data, save_enriched_data

# Your cleaned transactions
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

# 1️⃣ Fetch products from API
api_products = fetch_all_products()

# 2️⃣ Create mapping dictionary
product_mapping = create_product_mapping(api_products)

# 3️⃣ Enrich transactions
enriched = enrich_sales_data(valid_transactions, product_mapping)

# 4️⃣ Save enriched data
save_enriched_data(enriched)
