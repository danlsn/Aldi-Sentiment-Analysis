"""
Parse json from each row in csv file "../data/aldi-trustpilot.csv"
"""

import csv
import json


FILE = "../data/woolworths-trustpilot-reviews.csv"

# Read CSV excluding header, parse json rows
with open(FILE, "r", encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    rows = [json.loads(row[0]) for row in reader]

# Print first row
print(rows[0])

# Get all items in list '@graph' if '@type' == 'Review'
reviews = [item for row in rows for item in row["@graph"] if item["@type"] == "Review"]

# Write reviews to json file
with open("../data/woolworths-trustpilot-reviews.json", "w") as f:
    json.dump(reviews, f, indent=4)


...

