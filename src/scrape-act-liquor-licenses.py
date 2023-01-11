import json

import requests

cookies = {
    'renderCtx': '%7B%22pageId%22%3A%22584d606a-f1fb-451f-8aab-98107cf01a54%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%227c53851b-99bd-43df-951b-83f206b53f3f%22%2C%22audienceIds%22%3A%22%22%7D',
    'CookieConsentPolicy': '0:1', 'LSKey-c$CookieConsentPolicy': '0:1', '_gid': 'GA1.3.1152701296.1673409112',
    'pctrk': 'ceb51e96-a435-4c36-a4ff-2ab41171452e', '_ga': 'GA1.1.2051582812.1673409112',
    '_ga_HFXVTB2JW7': 'GS1.1.1673409112.1.1.1673409183.0.0.0', }

headers = {'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache',
    'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'renderCtx=%7B%22pageId%22%3A%22584d606a-f1fb-451f-8aab-98107cf01a54%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%227c53851b-99bd-43df-951b-83f206b53f3f%22%2C%22audienceIds%22%3A%22%22%7D; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; _gid=GA1.3.1152701296.1673409112; pctrk=ceb51e96-a435-4c36-a4ff-2ab41171452e; _ga=GA1.1.2051582812.1673409112; _ga_HFXVTB2JW7=GS1.1.1673409112.1.1.1673409183.0.0.0',
    'Origin': 'https://www.accesscanberra.act.gov.au', 'Pragma': 'no-cache',
    'Referer': 'https://www.accesscanberra.act.gov.au/s/public-registers/occupational-register?registerid=liquor-off-public-register',
    'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
    'X-SFDC-Page-Cache': '42e2138b2f022bbf', 'X-SFDC-Page-Scope-Id': '3618b84b-244c-463a-9bbb-b477c32d6318',
    'X-SFDC-Request-Id': '19666900008cf89118',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"', 'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"', }

params = {'r': '1', 'aura.ApexAction.execute': '1', }

data = {
    'message': '{"actions":[{"id":"115;a","descriptor":"aura://ApexActionController/ACTION$execute","callingDescriptor":"UNKNOWN","params":{"namespace":"","classname":"cxsWebContentController","method":"getDatasetConfigById","params":{"dataset_URL":"liquor-off-public-register"},"cacheable":false,"isContinuation":false}}]}',
    'aura.context': '{"mode":"PROD","fwuid":"tr2UlkrAHzi37ijzEeD2UA","app":"siteforce:communityApp","loaded":{"APPLICATION@markup://siteforce:communityApp":"K0V8802f_xC9u_ipYQN2Rg","COMPONENT@markup://instrumentation:o11yCoreCollector":"8giBLfYbOC17LwOopJh9VQ"},"dn":[],"globals":{},"uad":false}',
    'aura.pageURI': '/s/public-registers/occupational-register?registerid=liquor-off-public-register',
    'aura.token': 'null', }


def get_liquor_stores():
    response = requests.post('https://www.accesscanberra.act.gov.au/s/sfsites/aura', params=params, cookies=cookies,
        headers=headers, data=data)

    response_json = response.json()

    liquor_stores = json.loads(response_json['actions'][0]['returnValue']['returnValue']['DataConfig'])
...
