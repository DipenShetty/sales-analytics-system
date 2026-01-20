from utils.file_handler import read_sales_data, parse_transactions, validate_and_filter
from utils.data_processor import (
    calculate_total_revenue, region_wise_sales, top_selling_products,
    customer_analysis, daily_sales_trend, find_peak_sales_day,
    low_performing_products
)
from utils.api_handler import fetch_all_products, create_product_mapping, enrich_sales_data, save_enriched_data
from utils.report_generator import generate_sales_report
from utils.exporter import save_clean_transactions, save_metrics

def main():
    print("="*40)
    print("SALES ANALYTICS SYSTEM")
    print("="*40)

    # Step 1: Read and clean data
    print("[1/6] Reading and cleaning sales data...")
    raw_lines = read_sales_data('data/sales_data.txt')
    transactions = parse_transactions(raw_lines)

    # Step 2: Validate transactions
    print("[2/6] Validating transactions...")
    valid, invalid_count, summary = validate_and_filter(transactions)
    print(f"Validation Summary: {summary}")

    # Step 3: Save cleaned transactions and metrics
    save_clean_transactions(valid)
    save_metrics({
        "total_transactions": len(valid),
        "invalid_transactions": invalid_count
    })
    print("[3/6] Cleaned transactions saved.")

    # Step 4: Fetch API products and enrich
    print("[4/6] Fetching products from API...")
    api_products = fetch_all_products()
    product_mapping = create_product_mapping(api_products)

    print("[5/6] Enriching sales data...")
    enriched_transactions = enrich_sales_data(valid, product_mapping)
    save_enriched_data(enriched_transactions)
    print("Enriched data saved to data/enriched_sales_data.txt")

    # Step 5: Generate report
    print("[6/6] Generating final sales report...")
    generate_sales_report(valid, enriched_transactions)
    print("Report saved to output/sales_report.txt")
    print("="*40)
    print("PROCESS COMPLETE!")
    print("="*40)

if __name__ == "__main__":
    main()
