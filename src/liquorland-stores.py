"""
Get Liquorland store data from api
"""

import csv
import json
import os.path

ALDI_STORES = r"C:\Users\DanielLawson\IdeaProjects\Aldi-Sentiment-Analysis\data\processed\Store and DC List.csv"

with open(ALDI_STORES, 'r') as f:
    aldi_stores = csv.DictReader(f)
    aldi_qld_stores = [store for store in aldi_stores if "QLD" in store['Suburb']]

import requests

cookies = {
    '__uzma': 'f986a2e6-014f-4e81-b1f1-4f8161fb0008',
    '__uzmb': '1673412655',
    'SSID': 'CQDJfh0OAAAAAAA_QL5jcxLAMC9AvmMBAAAAAAAAAAAAL0C-YwBuOm4BAAMBOwAAL0C-YwEA',
    'SSSC': '6.G7187252695474901619.1|366.15105',
    'SSRT': 'MEC-YwADAA',
    'AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg': '1',
    '_gcl_au': '1.1.1310888303.1673412657',
    '_ga_MZBX8BWCCN': 'GS1.1.1673412657.1.0.1673412657.60.0.0',
    '_uetsid': '89822c30916b11eda9a5059b8fccf764',
    '_uetvid': '89826e30916b11edbc9a612b39253765',
    'CL_LL_02_UBT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjX3JvbGUiOiJBbm9ueW1vdXMiLCJjX2lkIjoiezMxNTU2MDYyLTVjYjktNDJhMy1hMDdhLWE1OWM1NDgxYmRjMH0iLCJjX2JyYW5kIjoibGwiLCJjX2F4X2lkIjoiIiwibmJmIjoxNjczNDEyNjU2LCJleHAiOjE2NzM0NDE0NTYsImlhdCI6MTY3MzQxMjY1NiwiaXNzIjoic2VsZiIsImF1ZCI6Imh0dHBzOi8vd3d3LmNvbGVzbGlxdW9yLmNvbS5hdSJ9.Xy7lCeislsRUsLPcEbRpnnbdAaTLk8UN59VgNBTv7pM',
    'CL_LL_02_ULN': '',
    'CL_LL_02_UFN': '',
    'CL_LL_02_UAID': '',
    'CL_LL_02_UPOA': 'false',
    'CL_LL_02_UDP': 'false',
    'AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg': '1075005958%7CMCIDTS%7C19369%7CMCMID%7C53398075994871008160608390494856219232%7CMCAAMLH-1674017456%7C8%7CMCAAMB-1674017456%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1673419856s%7CNONE%7CMCSYNCSOP%7C411-19376%7CvVersion%7C4.4.1',
    '_fbp': 'fb.2.1673412657843.17207655',
    's_cc': 'true',
    '_hjSessionUser_2820108': 'eyJpZCI6IjA1NGE3NDU1LThhMzAtNThjMS1hOWZjLTczYmM5YzIxMzM2YiIsImNyZWF0ZWQiOjE2NzM0MTI2NTg0MjIsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_2820108': 'eyJpZCI6IjY4Y2FmY2M0LTgyNGUtNDA3NS1hMzZjLTY3MTI1OWVmOWMwNCIsImNyZWF0ZWQiOjE2NzM0MTI2NTg1NTksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'cto_bundle': '0JizTF8lMkY1dUJHZ1VaZk1BSEYwMzQyRERyVzd1TzduVzNnNmw0YlVTVzJYVmZoMzVnbGFqOHF6N3YlMkJYSWtrJTJGUDRST29PdkFTVm1SRDZNU0FTWW1BZllFdUoxeHlZNmRhNEFheSUyQlcwck5ocVIybWRIQzlDV0F2VVRlc0NYNkYwQWx4UUJaSXk3Z2dzcmxKWEM0QyUyRmtlRTVKaEV3JTNEJTNE',
    '_ga': 'GA1.3.687958715.1673412657',
    '_gid': 'GA1.3.1850760977.1673412659',
    '_gat_gtag_UA_38224966_1': '1',
    'ORA_FPC': 'id=2039d73cbbb84d054ae1673373060141',
    'WTPERSIST': '',
    'rmStore': 'dmid:9145',
    'ADRUM': 's=1673412666568&r=https%3A%2F%2Fwww.liquorland.com.au%2Fstores',
    '__uzmd': '1673412667',
    'KP_UIDz-ssn': '02C8QcyHlqPxEbXBsAD0PtoqOibIlv05anLR0EOIIwMVXibDBX3e53aQMvKc0zVlpPGX9LTZCLCbBstdBR0Gsx1CPDk3GfSo3ceKRndSNZdWWVFsNXrydkdulV3tz0kjD8iLXxnDYyU5noHgqZoOQiCGhkn',
    'KP_UIDz': '02C8QcyHlqPxEbXBsAD0PtoqOibIlv05anLR0EOIIwMVXibDBX3e53aQMvKc0zVlpPGX9LTZCLCbBstdBR0Gsx1CPDk3GfSo3ceKRndSNZdWWVFsNXrydkdulV3tz0kjD8iLXxnDYyU5noHgqZoOQiCGhkn',
    '__uzmc': '228113487924',
}

headers = {
    'authority': 'www.liquorland.com.au',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'adrum': 'isAjax:true',
    'cache-control': 'no-cache',
    # 'cookie': '__uzma=f986a2e6-014f-4e81-b1f1-4f8161fb0008; __uzmb=1673412655; SSID=CQDJfh0OAAAAAAA_QL5jcxLAMC9AvmMBAAAAAAAAAAAAL0C-YwBuOm4BAAMBOwAAL0C-YwEA; SSSC=6.G7187252695474901619.1|366.15105; SSRT=MEC-YwADAA; AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg=1; _gcl_au=1.1.1310888303.1673412657; _ga_MZBX8BWCCN=GS1.1.1673412657.1.0.1673412657.60.0.0; _uetsid=89822c30916b11eda9a5059b8fccf764; _uetvid=89826e30916b11edbc9a612b39253765; CL_LL_02_UBT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjX3JvbGUiOiJBbm9ueW1vdXMiLCJjX2lkIjoiezMxNTU2MDYyLTVjYjktNDJhMy1hMDdhLWE1OWM1NDgxYmRjMH0iLCJjX2JyYW5kIjoibGwiLCJjX2F4X2lkIjoiIiwibmJmIjoxNjczNDEyNjU2LCJleHAiOjE2NzM0NDE0NTYsImlhdCI6MTY3MzQxMjY1NiwiaXNzIjoic2VsZiIsImF1ZCI6Imh0dHBzOi8vd3d3LmNvbGVzbGlxdW9yLmNvbS5hdSJ9.Xy7lCeislsRUsLPcEbRpnnbdAaTLk8UN59VgNBTv7pM; CL_LL_02_ULN=; CL_LL_02_UFN=; CL_LL_02_UAID=; CL_LL_02_UPOA=false; CL_LL_02_UDP=false; AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg=1075005958%7CMCIDTS%7C19369%7CMCMID%7C53398075994871008160608390494856219232%7CMCAAMLH-1674017456%7C8%7CMCAAMB-1674017456%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1673419856s%7CNONE%7CMCSYNCSOP%7C411-19376%7CvVersion%7C4.4.1; _fbp=fb.2.1673412657843.17207655; s_cc=true; _hjSessionUser_2820108=eyJpZCI6IjA1NGE3NDU1LThhMzAtNThjMS1hOWZjLTczYmM5YzIxMzM2YiIsImNyZWF0ZWQiOjE2NzM0MTI2NTg0MjIsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2820108=eyJpZCI6IjY4Y2FmY2M0LTgyNGUtNDA3NS1hMzZjLTY3MTI1OWVmOWMwNCIsImNyZWF0ZWQiOjE2NzM0MTI2NTg1NTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; cto_bundle=0JizTF8lMkY1dUJHZ1VaZk1BSEYwMzQyRERyVzd1TzduVzNnNmw0YlVTVzJYVmZoMzVnbGFqOHF6N3YlMkJYSWtrJTJGUDRST29PdkFTVm1SRDZNU0FTWW1BZllFdUoxeHlZNmRhNEFheSUyQlcwck5ocVIybWRIQzlDV0F2VVRlc0NYNkYwQWx4UUJaSXk3Z2dzcmxKWEM0QyUyRmtlRTVKaEV3JTNEJTNE; _ga=GA1.3.687958715.1673412657; _gid=GA1.3.1850760977.1673412659; _gat_gtag_UA_38224966_1=1; ORA_FPC=id=2039d73cbbb84d054ae1673373060141; WTPERSIST=; rmStore=dmid:9145; ADRUM=s=1673412666568&r=https%3A%2F%2Fwww.liquorland.com.au%2Fstores; __uzmd=1673412667; KP_UIDz-ssn=02C8QcyHlqPxEbXBsAD0PtoqOibIlv05anLR0EOIIwMVXibDBX3e53aQMvKc0zVlpPGX9LTZCLCbBstdBR0Gsx1CPDk3GfSo3ceKRndSNZdWWVFsNXrydkdulV3tz0kjD8iLXxnDYyU5noHgqZoOQiCGhkn; KP_UIDz=02C8QcyHlqPxEbXBsAD0PtoqOibIlv05anLR0EOIIwMVXibDBX3e53aQMvKc0zVlpPGX9LTZCLCbBstdBR0Gsx1CPDk3GfSo3ceKRndSNZdWWVFsNXrydkdulV3tz0kjD8iLXxnDYyU5noHgqZoOQiCGhkn; __uzmc=228113487924',
    'pragma': 'no-cache',
    'referer': 'https://www.liquorland.com.au/stores',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
}

params = {
    'lat': '-37.813907',
    'lon': '144.96324',
}

stores_responses = []
for store in aldi_qld_stores:
    params['lat'] = store['Lat']
    params['lon'] = store['Lon']

    response = requests.get('https://www.liquorland.com.au/api/FindClosest/ll', params=params, cookies=cookies,
                            headers=headers)

    response_json = response.json()
    # Insert response into store_responses
    stores_responses.append(response_json)


# Flatten the list of stores_responses
stores_responses = [item for sublist in stores_responses for item in sublist]
out_file = os.path.join("../data", f"liquorland_stores_qld.json")

# Write the response to a file
with open(out_file, 'w') as f:
    json.dump(stores_responses, f)

# Write list of stores_responses to a csv with DictWriter
out_file = os.path.join("../data", f"liquorland_stores_qld.csv")
with open(out_file, 'w') as f:
    writer = csv.DictWriter(f, fieldnames=stores_responses[0].keys())
    writer.writeheader()
    writer.writerows(stores_responses)
