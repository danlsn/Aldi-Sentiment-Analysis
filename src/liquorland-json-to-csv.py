import json
import csv
import os
import glob

import pandas as pd

JSON_FILES = glob.glob('../data/liquorland_near_store_*.json')

flat_data = []
for json_file in JSON_FILES:
    with open(json_file) as f:
        data = json.load(f)
        for _ in data:
            flat_data.append(_)


# Deduplicate list of dictionaries by locationID
flat_data = {i['locationID']:i for i in flat_data}
flat_data_list = list(flat_data.values())

# Write flat_data list of dictionaries to CSV
with open('../data/liquorland_near_store.csv', 'w', newline='') as f:
    df = pd.DataFrame(flat_data_list)
    df.to_csv(f, index=False)




...
