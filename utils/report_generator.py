import os
from datetime import datetime
from utils.data_processor import (
    calculate_total_revenue, region_wise_sales, top_selling_products,
    customer_analysis, daily_sales_trend, find_peak_sales_day,
    low_performing_products
)

def generate_sales_report(transactions, enriched_transactions, output_file='output/sales_report.txt'):
    os.makedirs('output', exist_ok=True)

    total_revenue = calculate_total_revenue(transactions)
    total_transactions = len(transactions)
    avg_order_value = total_revenue / total_transactions if total_transactions else 0

    # Get date range
    dates = [t['Date'] for t in transactions]
    date_range = f"{min(dates)} to {max(dates)}" if dates else "N/A"

    region_stats = region_wise_sales(transactions)
    top_products = top_selling_products(transactions, n=5)
    customer_stats = customer_analysis(transactions)
    daily_trends = daily_sales_trend(transactions)
    peak_day = find_peak_sales_day(transactions)
    low_products = low_performing_products(transactions, threshold=10)

    # API enrichment summary
    enriched_count = sum(1 for t in enriched_transactions if t.get('API_Match'))
    total_enriched = len(enriched_transactions)
    enrichment_success_rate = (enriched_count / total_enriched * 100) if total_enriched else 0
    failed_products = [t['ProductID'] for t in enriched_transactions if not t.get('API_Match')]

    with open(output_file, 'w', encoding='utf-8') as f:
        # ================= HEADER =================
        f.write("="*50 + "\n")
        f.write("SALES ANALYTICS REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Records Processed: {total_transactions}\n")
        f.write("="*50 + "\n\n")

        # ================ OVERALL SUMMARY =================
        f.write("OVERALL SUMMARY\n")
        f.write("-"*50 + "\n")
        f.write(f"Total Revenue: ₹{total_revenue:,.2f}\n")
        f.write(f"Total Transactions: {total_transactions}\n")
        f.write(f"Average Order Value: ₹{avg_order_value:,.2f}\n")
        f.write(f"Date Range: {date_range}\n\n")

        # ================ REGION-WISE PERFORMANCE =================
        f.write("REGION-WISE PERFORMANCE\n")
        f.write("-"*50 + "\n")
        f.write(f"{'Region':<10}{'Sales':>15}{'% of Total':>15}{'Transactions':>15}\n")
        for region, stats in sorted(region_stats.items(), key=lambda x: x[1]['total_sales'], reverse=True):
            f.write(f"{region:<10}₹{stats['total_sales']:>14,.2f}{stats['percentage']:>14.2f}%{stats['transaction_count']:>15}\n")
        f.write("\n")

        # ================ TOP 5 PRODUCTS =================
        f.write("TOP 5 PRODUCTS\n")
        f.write("-"*50 + "\n")
        f.write(f"{'Rank':<5}{'Product Name':<20}{'Quantity':>10}{'Revenue':>15}\n")
        for i, (name, qty, rev) in enumerate(top_products, 1):
            f.write(f"{i:<5}{name:<20}{qty:>10}{rev:>15,.2f}\n")
        f.write("\n")

        # ================ TOP 5 CUSTOMERS =================
        f.write("TOP 5 CUSTOMERS\n")
        f.write("-"*50 + "\n")
        f.write(f"{'Rank':<5}{'CustomerID':<15}{'Total Spent':>15}{'Order Count':>15}\n")
        top_customers = sorted(customer_stats.items(), key=lambda x: x[1]['total_spent'], reverse=True)[:5]
        for i, (cid, stats) in enumerate(top_customers, 1):
            f.write(f"{i:<5}{cid:<15}₹{stats['total_spent']:>14,.2f}{stats['purchase_count']:>15}\n")
        f.write("\n")

        # ================ DAILY SALES TREND =================
        f.write("DAILY SALES TREND\n")
        f.write("-"*50 + "\n")
        f.write(f"{'Date':<12}{'Revenue':>15}{'Transactions':>15}{'Unique Customers':>20}\n")
        for date, stats in sorted(daily_trends.items()):
            f.write(f"{date:<12}₹{stats['revenue']:>14,.2f}{stats['transaction_count']:>15}{stats['unique_customers']:>20}\n")
        f.write("\n")

        # ================ PRODUCT PERFORMANCE ANALYSIS =================
        f.write("PRODUCT PERFORMANCE ANALYSIS\n")
        f.write("-"*50 + "\n")
        if peak_day:
            f.write(f"Best Selling Day: {peak_day[0]} | Revenue: ₹{peak_day[1]:,.2f} | Transactions: {peak_day[2]}\n")
        if low_products:
            f.write("Low Performing Products:\n")
            for name, qty, rev in low_products:
                f.write(f"- {name}: Quantity={qty}, Revenue=₹{rev:,.2f}\n")
        f.write("\n")

        # ================ API ENRICHMENT SUMMARY =================
        f.write("API ENRICHMENT SUMMARY\n")
        f.write("-"*50 + "\n")
        f.write(f"Total products enriched: {enriched_count}/{total_enriched}\n")
        f.write(f"Success rate: {enrichment_success_rate:.2f}%\n")
        if failed_products:
            f.write(f"Products not enriched: {', '.join(failed_products)}\n")
        f.write("\n")

        f.write("="*50 + "\n")
        f.write("END OF REPORT\n")
        f.write("="*50 + "\n")


