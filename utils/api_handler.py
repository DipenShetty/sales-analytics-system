import requests

def fetch_all_products():
    """Fetch all products from DummyJSON API"""
    try:
        response = requests.get('https://dummyjson.com/products?limit=100')
        response.raise_for_status()
        data = response.json()
        print(f"✓ Fetched {len(data['products'])} products from API")
        return data['products']
    except Exception as e:
        print(f"⚠ Failed to fetch products: {e}")
        return []

def create_product_mapping(api_products):
    """Create a mapping of numeric ProductID to product info safely"""
    mapping = {}
    for p in api_products:
        mapping[p['id']] = {
            'title': p.get('title', None),
            'category': p.get('category', None),
            'brand': p.get('brand', None),
            'rating': p.get('rating', None)
        }
    return mapping


def enrich_sales_data(transactions, product_mapping):
    """Add API info to each transaction"""
    enriched = []

    for t in transactions:
        try:
            # Extract numeric ID (P101 -> 101)
            numeric_id = int(t['ProductID'][1:])
            product_info = product_mapping.get(numeric_id)

            # Add API fields
            t['API_Category'] = product_info['category'] if product_info else None
            t['API_Brand'] = product_info['brand'] if product_info else None
            t['API_Rating'] = product_info['rating'] if product_info else None
            t['API_Match'] = True if product_info else False

        except Exception:
            t['API_Category'] = None
            t['API_Brand'] = None
            t['API_Rating'] = None
            t['API_Match'] = False

        enriched.append(t)

    return enriched

def save_enriched_data(enriched_transactions, filename='data/enriched_sales_data.txt'):
    """Save enriched transactions to a pipe-delimited file"""
    import os
    os.makedirs('data', exist_ok=True)

    if not enriched_transactions:
        print("⚠ No transactions to save")
        return

    headers = list(enriched_transactions[0].keys())
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('|'.join(headers) + '\n')
        for t in enriched_transactions:
            row = '|'.join([str(t[h]) if t[h] is not None else '' for h in headers])
            f.write(row + '\n')

    print(f"✓ Enriched data saved to {filename}")




