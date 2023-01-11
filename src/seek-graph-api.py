import requests

headers = {
    'authority': 'www.seek.com.au',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'cookie': 'sol_id=c00c353f-a376-4b96-b397-16e262dbd3d3; JobseekerSessionId=5959404e-631e-45a1-bb3b-2ae481757cf6; JobseekerVisitorId=5959404e-631e-45a1-bb3b-2ae481757cf6; __cf_bm=v7uuOWYV.rxI05Mz2YJnv_PCMGNlhkaXTCuiqIpm7oA-1673406332-0-ASQhw5tclgv3qfKiV9Z1X7HRIXHNHqO6sZepRcJNRuarU5ZoyJsdXTvsI0taXTafJTKqFzsSWwI9W8z9cf7VtQQ=; da_cdt=visid_01859eca42d7000208c170e72b8105081001807900bd0-sesid_1673406333711; da_anz_candi_sid=1673406333711; da_marketing_channel=Direct; da_marketing_channel_value=https://www.seek.com.au/; da_tracking_code=null; _gid=GA1.3.1390657242.1673406334; _schn=_q3itqlg; _scid=cf14e538-62cd-4c0e-8188-a2e58722b24f; _hjSessionUser_162402=eyJpZCI6ImRjZDMxMTFhLWIwNzItNTZkZS04MDRlLTY4YTEzZGFhYzMzMSIsImNyZWF0ZWQiOjE2NjczNDkwODEyNjksImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample=0; _hjSession_162402=eyJpZCI6IjUzZjFmYzc2LTg0NzEtNDUxNy04NjMxLTE5ZjA3ZDRkMjZiMyIsImNyZWF0ZWQiOjE2NzM0MDYzMzQyMTQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.2.1673406334319.551464953; _gcl_au=1.1.67311567.1673406334; _pin_unauth=dWlkPU5UYzJOelJqWXpjdFlURm1OQzAwTWpSaExUbGlaakl0WlRreE5HTmxPV1ZoTTJJeQ; sol_id=c00c353f-a376-4b96-b397-16e262dbd3d3; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%7D; __gads=ID=b4553f7cac71defc:T=1673406340:S=ALNI_MZCuP-GS8P4HP3cSUrtD4tmPTuXVA; __gpi=UID=00000ba26f0e0336:T=1673406340:RT=1673406340:S=ALNI_MZi8MS-Qh7KJjxOIwoZBiYLho9hnw; _ga=GA1.1.732079538.1673406334; main=V%7C2~P%7Cjobsearch~K%7CALDI~WID%7C3000~L%7C3000~OSF%7Cquick&set=1673406360204; da_searchTerm=ALDI; skl-lcid=ce0fc97d-de2d-4817-a8e2-cf9dd3e75688; utag_main=v_id:01859eca42d7000208c170e72b8105081001807900bd0$_sn:1$_se:9$_ss:0$_st:1673408166005$ses_id:1673406333711%3Bexp-session$_pn:2%3Bexp-session$dc_visit:1$dc_event:9%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; _ga_JYC9JXRYWC=GS1.1.1673406334.1.1.1673406366.28.0.0; _dd_s=rum=0&expire=1673407336596',
    'origin': 'https://www.seek.com.au',
    'pragma': 'no-cache',
    'referer': 'https://www.seek.com.au/job/59641308?type=standard',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'seek-request-brand': 'seek',
    'seek-request-country': 'AU',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
    'x-application': 'au',
    'x-seek-ec-sessionid': '5959404e-631e-45a1-bb3b-2ae481757cf6',
    'x-seek-ec-visitorid': '5959404e-631e-45a1-bb3b-2ae481757cf6',
    'x-seek-site': 'chalice',
}

json_data = {
    'operationName': 'GetJobDataAutomation',
    'variables': {
        'is_'
        'sessionId': '5959404e-631e-45a1-bb3b-2ae481757cf6',
        'zone': 'anz-1',
        'locale': 'en-AU',
    },
    'query': 'query GetJobDetails($jobId: ID!, $jobDetailsViewedCorrelationId: String!, $sessionId: String!, $zone: Zone!, $locale: Locale!) {\n  jobDetails(\n    id: $jobId\n    tracking: {channel: "WEB", jobDetailsViewedCorrelationId: $jobDetailsViewedCorrelationId, sessionId: $sessionId}\n  ) {\n    job {\n      tracking {\n        adProductType\n        classificationInfo {\n          classificationId\n          classification\n          subClassificationId\n          subClassification\n          __typename\n        }\n        hasRoleRequirements\n        isPrivateAdvertiser\n        locationInfo {\n          area\n          location\n          locationIds\n          __typename\n        }\n        __typename\n      }\n      id\n      title\n      phoneNumber\n      isExpired\n      isLinkOut\n      contactMatches {\n        type\n        value\n        __typename\n      }\n      abstract\n      content(platform: WEB)\n      status\n      listedAt {\n        shortLabel\n        __typename\n      }\n      salary {\n        currencyLabel(zone: $zone)\n        label\n        __typename\n      }\n      shareLink(platform: WEB, zone: $zone)\n      workTypes {\n        label\n        __typename\n      }\n      advertiser {\n        id\n        name\n        __typename\n      }\n      location {\n        label(locale: $locale, type: LONG)\n        __typename\n      }\n      categories {\n        label\n        __typename\n      }\n      products {\n        branding {\n          id\n          cover {\n            url\n            __typename\n          }\n          thumbnailCover: cover(isThumbnail: true) {\n            url\n            __typename\n          }\n          logo {\n            url\n            __typename\n          }\n          __typename\n        }\n        bullets\n        questionnaire {\n          questions\n          __typename\n        }\n        video {\n          url\n          position\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    companyReviews(zone: $zone) {\n      id\n      name\n      fullName\n      rating\n      reviewCount\n      reviewsUrl\n      __typename\n    }\n    companySearchUrl(zone: $zone)\n    learningInsights(platform: WEB, zone: $zone) {\n      analytics\n      content\n      __typename\n    }\n    sourcr {\n      image\n      imageMobile\n      link\n      __typename\n    }\n    __typename\n  }\n}\n',
}

response = requests.post('https://www.seek.com.au/graphql', headers=headers, json=json_data)

response_json = response.json()
...
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"operationName":"GetJobDetails","variables":{"jobId":"59641308","jobDetailsViewedCorrelationId":"788c49e9-5b4b-471a-8685-449f235f5c77","sessionId":"5959404e-631e-45a1-bb3b-2ae481757cf6","zone":"anz-1","locale":"en-AU"},"query":"query GetJobDetails($jobId: ID!, $jobDetailsViewedCorrelationId: String!, $sessionId: String!, $zone: Zone!, $locale: Locale!) {\\n  jobDetails(\\n    id: $jobId\\n    tracking: {channel: \\"WEB\\", jobDetailsViewedCorrelationId: $jobDetailsViewedCorrelationId, sessionId: $sessionId}\\n  ) {\\n    job {\\n      tracking {\\n        adProductType\\n        classificationInfo {\\n          classificationId\\n          classification\\n          subClassificationId\\n          subClassification\\n          __typename\\n        }\\n        hasRoleRequirements\\n        isPrivateAdvertiser\\n        locationInfo {\\n          area\\n          location\\n          locationIds\\n          __typename\\n        }\\n        __typename\\n      }\\n      id\\n      title\\n      phoneNumber\\n      isExpired\\n      isLinkOut\\n      contactMatches {\\n        type\\n        value\\n        __typename\\n      }\\n      abstract\\n      content(platform: WEB)\\n      status\\n      listedAt {\\n        shortLabel\\n        __typename\\n      }\\n      salary {\\n        currencyLabel(zone: $zone)\\n        label\\n        __typename\\n      }\\n      shareLink(platform: WEB, zone: $zone)\\n      workTypes {\\n        label\\n        __typename\\n      }\\n      advertiser {\\n        id\\n        name\\n        __typename\\n      }\\n      location {\\n        label(locale: $locale, type: LONG)\\n        __typename\\n      }\\n      categories {\\n        label\\n        __typename\\n      }\\n      products {\\n        branding {\\n          id\\n          cover {\\n            url\\n            __typename\\n          }\\n          thumbnailCover: cover(isThumbnail: true) {\\n            url\\n            __typename\\n          }\\n          logo {\\n            url\\n            __typename\\n          }\\n          __typename\\n        }\\n        bullets\\n        questionnaire {\\n          questions\\n          __typename\\n        }\\n        video {\\n          url\\n          position\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    companyReviews(zone: $zone) {\\n      id\\n      name\\n      fullName\\n      rating\\n      reviewCount\\n      reviewsUrl\\n      __typename\\n    }\\n    companySearchUrl(zone: $zone)\\n    learningInsights(platform: WEB, zone: $zone) {\\n      analytics\\n      content\\n      __typename\\n    }\\n    sourcr {\\n      image\\n      imageMobile\\n      link\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'
#response = requests.post('https://www.seek.com.au/graphql', headers=headers, data=data)