import json

import pandas as pd

json_file = r"..\data\act-liquor-stores-page-2.json"

with open(json_file, "r") as f:
    liquor_stores = json.load(f)
    license_str = liquor_stores['actions'][0]['returnValue']['returnValue']
    license_json = json.loads(license_str)
    df = pd.json_normalize(license_json)
    df.to_csv(r"..\data\act-liquor-stores.csv", index=False)
    ...


