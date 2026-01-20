import csv
import json
import os

def save_clean_transactions(transactions, filename="output/clean_transactions.csv"):
    os.makedirs("output", exist_ok=True)

    if not transactions:
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions)


def save_metrics(metrics, filename="output/metrics_summary.json"):
    os.makedirs("output", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4)
