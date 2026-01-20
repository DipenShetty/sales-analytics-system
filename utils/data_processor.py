# utils/data_processor.py

def calculate_total_revenue(transactions):
    return sum(t['Quantity'] * t['UnitPrice'] for t in transactions)


def region_wise_sales(transactions):
    region_stats = {}
    total_revenue = calculate_total_revenue(transactions)
    for t in transactions:
        region = t['Region']
        amount = t['Quantity'] * t['UnitPrice']
        if region not in region_stats:
            region_stats[region] = {'total_sales': 0, 'transaction_count': 0, 'percentage': 0}
        region_stats[region]['total_sales'] += amount
        region_stats[region]['transaction_count'] += 1
    for stats in region_stats.values():
        stats['percentage'] = (stats['total_sales'] / total_revenue * 100) if total_revenue else 0
    return region_stats


def top_selling_products(transactions, n=5):
    product_agg = {}
    for t in transactions:
        name = t['ProductName']
        qty = t['Quantity']
        rev = t['Quantity'] * t['UnitPrice']
        if name not in product_agg:
            product_agg[name] = {'qty': 0, 'rev': 0}
        product_agg[name]['qty'] += qty
        product_agg[name]['rev'] += rev
    top_products = sorted(product_agg.items(), key=lambda x: x[1]['qty'], reverse=True)[:n]
    return [(name, info['qty'], info['rev']) for name, info in top_products]


def customer_analysis(transactions):
    customers = {}
    for t in transactions:
        cid = t['CustomerID']
        amount = t['Quantity'] * t['UnitPrice']
        product = t['ProductName']
        if cid not in customers:
            customers[cid] = {'total_spent': 0, 'purchase_count': 0, 'products_bought': set()}
        customers[cid]['total_spent'] += amount
        customers[cid]['purchase_count'] += 1
        customers[cid]['products_bought'].add(product)
    for cid, stats in customers.items():
        stats['avg_order_value'] = stats['total_spent'] / stats['purchase_count'] if stats['purchase_count'] else 0
        stats['products_bought'] = list(stats['products_bought'])
    return dict(sorted(customers.items(), key=lambda x: x[1]['total_spent'], reverse=True))


def daily_sales_trend(transactions):
    daily = {}
    for t in transactions:
        date = t['Date']
        amount = t['Quantity'] * t['UnitPrice']
        if date not in daily:
            daily[date] = {'revenue': 0, 'transaction_count': 0, 'unique_customers': set()}
        daily[date]['revenue'] += amount
        daily[date]['transaction_count'] += 1
        daily[date]['unique_customers'].add(t['CustomerID'])
    for stats in daily.values():
        stats['unique_customers'] = len(stats['unique_customers'])
    return dict(sorted(daily.items()))


def find_peak_sales_day(transactions):
    daily = daily_sales_trend(transactions)
    if not daily:
        return None
    peak_date, stats = max(daily.items(), key=lambda x: x[1]['revenue'])
    return (peak_date, stats['revenue'], stats['transaction_count'])


def low_performing_products(transactions, threshold=10):
    products = top_selling_products(transactions, n=len(transactions))
    low_products = [(name, qty, rev) for name, qty, rev in products if qty < threshold]
    return low_products
