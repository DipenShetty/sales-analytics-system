def calculate_total_revenue(transactions):
    return sum(t['Quantity'] * t['UnitPrice'] for t in transactions)


def revenue_by_product(transactions):
    revenue = {}
    for t in transactions:
        product = t['ProductName']
        amount = t['Quantity'] * t['UnitPrice']
        revenue[product] = revenue.get(product, 0) + amount
    return revenue


def revenue_by_region(transactions):
    revenue = {}
    for t in transactions:
        region = t['Region']
        amount = t['Quantity'] * t['UnitPrice']
        revenue[region] = revenue.get(region, 0) + amount
    return revenue


def top_selling_products(transactions, top_n=5):
    revenue = revenue_by_product(transactions)
    sorted_products = sorted(
        revenue.items(),
        key=lambda x: x[1],
        reverse=True
    )
    return sorted_products[:top_n]
