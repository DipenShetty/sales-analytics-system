# utils/file_handler.py
import os

def read_sales_data(filename):
    """
    Reads sales data from file handling different encodings.
    Returns a list of non-empty lines (skips header).
    """
    encodings = ['utf-8', 'latin-1', 'cp1252']
    lines = []

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found!")
        return []

    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]
            break
        except UnicodeDecodeError:
            continue
    else:
        print("Error: Unable to read file due to encoding issues.")
        return []

    # Skip header row if present
    if lines and 'TransactionID' in lines[0]:
        lines = lines[1:]

    return lines


def parse_transactions(raw_lines):
    """
    Parses raw sales data lines into a clean list of dictionaries.
    """
    transactions = []

    for line in raw_lines:
        parts = line.split('|')

        # Skip rows with incorrect number of fields
        if len(parts) != 8:
            continue

        transaction_id, date, product_id, product_name, quantity, unit_price, customer_id, region = parts

        # Clean product name (remove commas)
        product_name = product_name.replace(',', '').strip()

        # Clean and convert quantity
        try:
            quantity = int(quantity.replace(',', '').strip())
        except ValueError:
            continue

        # Clean and convert unit price
        try:
            unit_price = float(unit_price.replace(',', '').strip())
        except ValueError:
            continue

        transaction = {
            'TransactionID': transaction_id.strip(),
            'Date': date.strip(),
            'ProductID': product_id.strip(),
            'ProductName': product_name,
            'Quantity': quantity,
            'UnitPrice': unit_price,
            'CustomerID': customer_id.strip(),
            'Region': region.strip()
        }

        transactions.append(transaction)

    return transactions


def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters.
    """
    valid_transactions = []
    invalid_count = 0

    # Display available regions
    regions = sorted(set(t['Region'] for t in transactions if t.get('Region')))
    print("Available Regions:", ", ".join(regions))

    # Calculate transaction amounts
    amounts = [t['Quantity'] * t['UnitPrice'] for t in transactions]
    if amounts:
        print(f"Transaction Amount Range: ₹{min(amounts):,.2f} - ₹{max(amounts):,.2f}")

    for t in transactions:
        # Validation rules
        if (
            t['Quantity'] <= 0 or
            t['UnitPrice'] <= 0 or
            not t['TransactionID'].startswith('T') or
            not t['ProductID'].startswith('P') or
            not t['CustomerID'].startswith('C') or
            not t['Region']
        ):
            invalid_count += 1
            continue

        amount = t['Quantity'] * t['UnitPrice']

        # Apply optional filters
        if region and t['Region'] != region:
            continue

        if min_amount and amount < min_amount:
            continue

        if max_amount and amount > max_amount:
            continue

        valid_transactions.append(t)

    filter_summary = {
        'total_input': len(transactions),
        'invalid': invalid_count,
        'final_count': len(valid_transactions)
    }

    return valid_transactions, invalid_count, filter_summary

