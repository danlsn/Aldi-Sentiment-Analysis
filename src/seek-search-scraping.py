import json

import requests

headers = {
    'authority': 'www.seek.com.au',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'sol_id=c00c353f-a376-4b96-b397-16e262dbd3d3; JobseekerSessionId=5959404e-631e-45a1-bb3b-2ae481757cf6; JobseekerVisitorId=5959404e-631e-45a1-bb3b-2ae481757cf6; da_cdt=visid_01859eca42d7000208c170e72b8105081001807900bd0-sesid_1673406333711; da_anz_candi_sid=1673406333711; da_marketing_channel=Direct; da_marketing_channel_value=https://www.seek.com.au/; da_tracking_code=null; _gid=GA1.3.1390657242.1673406334; _schn=_q3itqlg; _scid=cf14e538-62cd-4c0e-8188-a2e58722b24f; _hjSessionUser_162402=eyJpZCI6ImRjZDMxMTFhLWIwNzItNTZkZS04MDRlLTY4YTEzZGFhYzMzMSIsImNyZWF0ZWQiOjE2NjczNDkwODEyNjksImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample=0; _hjSession_162402=eyJpZCI6IjUzZjFmYzc2LTg0NzEtNDUxNy04NjMxLTE5ZjA3ZDRkMjZiMyIsImNyZWF0ZWQiOjE2NzM0MDYzMzQyMTQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.2.1673406334319.551464953; _gcl_au=1.1.67311567.1673406334; _pin_unauth=dWlkPU5UYzJOelJqWXpjdFlURm1OQzAwTWpSaExUbGlaakl0WlRreE5HTmxPV1ZoTTJJeQ; sol_id=c00c353f-a376-4b96-b397-16e262dbd3d3; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%7D; __gads=ID=b4553f7cac71defc:T=1673406340:S=ALNI_MZCuP-GS8P4HP3cSUrtD4tmPTuXVA; __gpi=UID=00000ba26f0e0336:T=1673406340:RT=1673406340:S=ALNI_MZi8MS-Qh7KJjxOIwoZBiYLho9hnw; _ga=GA1.1.732079538.1673406334; da_searchTerm=ALDI; __cf_bm=t5NjK4cG6acTEnIXoHWoXyzvbgXqohpk1_0X2UJYApQ-1673407328-0-AcEYcf7B1Dzv98DQRAWGBQheUwgCP8xuS2tNCPWzfEfsevsDBeKHASPVDs1yAR4B6ro1jsNf9c2m6qZxYjgykHM=; _gat_tealium_0=1; skl-lcid=1e56d4b7-1e2d-457d-b6b1-a325efbd3c69; _ga_JYC9JXRYWC=GS1.1.1673406334.1.1.1673407329.60.0.0; _dd_s=rum=0&expire=1673408234016; utag_main=v_id:01859eca42d7000208c170e72b8105081001807900bd0$_sn:1$_se:21$_ss:0$_st:1673409134022$ses_id:1673406333711%3Bexp-session$_pn:2%3Bexp-session$dc_visit:1$dc_event:21%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; main=V%7C2~P%7Cjobsearch~K%7CALDI~WID%7C3000~N%7C4~L%7C3000~OSF%7Cquick&set=1673407335045',
    'pragma': 'no-cache',
    'referer': 'https://www.seek.com.au/ALDI-jobs/at-this-company?page=4',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
    'x-seek-checksum': '1298345d',
    'x-seek-site': 'Chalice',
}

params = {
    'siteKey': 'AU-Main',
    'sourcesystem': 'houston',
    'userqueryid': 'a3f7e6f85be73fd8fe2e3d5ea92001b7-7335003',
    'userid': '5959404e-631e-45a1-bb3b-2ae481757cf6',
    'usersessionid': '5959404e-631e-45a1-bb3b-2ae481757cf6',
    'eventCaptureSessionId': '5959404e-631e-45a1-bb3b-2ae481757cf6',
    'where': 'All Australia',
    'page': '1',
    'seekSelectAllPages': 'true',
    'companyname': 'ALDI',
    'include': 'seodata',
    'solId': 'c00c353f-a376-4b96-b397-16e262dbd3d3',
}

for page in range(6, 30):
    params['page'] = str(page)
    response = requests.get('https://www.seek.com.au/api/chalice-search/v4/search', params=params, headers=headers)
    data = response.json()
    # Save the data to a file
    with open(f'../data/seek-job-listings-page-{page}.json', 'w') as f:
        json.dump(data, f)

