"""
Parse HTML files using BeautifulSoup from productreview.com.au located in '../data/staging/productreview-com-au'
and save the parsed data to '../data/processed/productreview-com-au'
"""
import json
import logging
import os
import re

import pandas as pd
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up file paths
staging_dir = os.path.join('..', 'data', 'staging', 'productreview-com-au')
processed_dir = os.path.join('..', 'data', 'processed', 'productreview-com-au')

lookup = {
    'handle': {'tag': 'a', 'selector': {'class': 'UBMNLo VhC5t9 DLanvv KtG5Lk K2NdzS'}},
    'location': {'tag': 'small', 'selector': {"class": "Jv5SYB V1KSK8 nZ6yEp SlFMms"}},
    'review_title': {'tag': 'h3', 'selector': {'class': '_MFwCB'}},
    'rating_text': {'tag': 'div', 'selector': {'class': 'YwL0z0 A5MBM1 N9bipo _3agxj Kge3uN CTa6sF'}},
    'review_text': {'tag': 'p', 'selector': {'class': '_MFwCB'}},
}


def get_html_files():
    # Get all files in staging directory, with full path
    files = [os.path.join(staging_dir, f) for f in os.listdir(staging_dir)]
    return files


def load_html_files(html_files):
    soup_list = []
    # Set up regex patterns
    filename_pattern = re.compile(r'^(.*?)-productreview-com-au-page-(\d+)')
    # Loop through files
    for file in html_files:
        # Get file name
        file_name = os.path.basename(file)

        # Open file
        with open(file, 'r', encoding='utf-8') as f:
            # Read file
            html = f.read()

            # Parse HTML
            soup = BeautifulSoup(html, 'html.parser')
            soup_list.append(soup)
    return soup_list


def get_review_divs(html_soup):
    soup = html_soup
    # Get all divs having id beginning with 'review-'
    review_divs = soup.find_all('div', id=re.compile(r'^review-'))
    return review_divs


def find_div_text(div, tag, selector):
    try:
        return div.find(tag, selector).text
    except AttributeError:
        return None


def find_div_title(div, tag, selector):
    try:
        return div.find(tag, selector).get('title')
    except AttributeError:
        return None


def strip_duplicate_whitespace(text):
    pat = re.compile(r'\s+')
    return re.sub(pat, ' ', text)


def get_review_text(div, tag, selector):
    try:
        review_body = div.find('div', {'itemprop': 'reviewBody'})
        # Get review_body children
        read_more = review_body.find('span', text='Read more')
        if read_more:
            # Get review text
            review_text = read_more.previous_sibling.text
            review_text += read_more.next_sibling.text
            return strip_duplicate_whitespace(review_text)
        else:
            return strip_duplicate_whitespace(review_body.find('p', {'class': '_MFwCB'}).text)
    except AttributeError:
        return None


def get_rating_text(div):
    try:
        # Find div that matches regex '\d out of 5 stars'
        rating_text = div.find('div', {'title': re.compile(r'^\d out of 5 stars')})
        return rating_text.get('title')
    except AttributeError:
        return None


def get_review_details(div):
    detailed_rating = {
        'value_for_money': None,
        'product_quality': None,
        'customer_service': None,
        'return_claim_made': None,
        'incentivised_review': None,
        'user_reviews_count': None,
        'store_location': None,
        'user_reviews_likes': None
    }
    uls = div.find_all('ul')
    for ul in uls:
        if ul.get('title') == 'Click to see all answers':
            for li in ul.children:
                if li.name == 'li':
                    get_rating_stars_pat = re.compile(r'(\d)/5')
                    if 'Value for Money' in li.text:
                        detailed_rating['value_for_money'] = re.search(get_rating_stars_pat,
                                                                       li.find('div').get('title')).group(1)
                    elif 'Product Quality' in li.text:
                        detailed_rating['product_quality'] = re.search(get_rating_stars_pat,
                                                                       li.find('div').get('title')).group(1)
                    elif 'Customer Service' in li.text:
                        detailed_rating['customer_service'] = re.search(get_rating_stars_pat,
                                                                        li.find('div').get('title')).group(1)
                    # elif incentivised_review contains 'Incentivised Review'
                    elif 'Incentivised Review' in li.text:
                        if 'Yes' in li.text:
                            detailed_rating['incentivised_review'] = True
                        else:
                            detailed_rating['incentivised_review'] = False
                    elif 'Return Claim Made' in li.text:
                        if 'Yes' in li.text:
                            detailed_rating['return_claim_made'] = True
                        else:
                            detailed_rating['return_claim_made'] = False
                    elif 'Store Location' in li.text:
                        store_location = re.search(r'(?<=Store Location).*', li.text).group(0)
                        detailed_rating['store_location'] = store_location.strip()
        else:
            for li in ul.children:
                if li.name == 'li':
                    if 'review' in li.text:
                        detailed_rating['user_reviews_count'] = li.find('span').text
                    elif 'like' in li.text:
                        detailed_rating['user_reviews_likes'] = li.find('span').text
    return detailed_rating


def parse_html_reviews(review_divs):
    reviews = []

    # Loop through review divs
    for div in review_divs:
        review = {'handle': find_div_text(div, lookup['handle']['tag'], lookup['handle']['selector']),
                  'location': find_div_text(div, lookup['location']['tag'], lookup['location']['selector']),
                  'review_title': find_div_text(div, lookup['review_title']['tag'], lookup['review_title']['selector']),
                  'rating_text': get_rating_text(div),
                  'review_text': get_review_text(div, lookup['review_text']['tag'], lookup['review_text']['selector']),
                  'review_date': div.find('time').get('datetime'),
                  }
        review_details = get_review_details(div)
        review.update(review_details)
        # Remove newlines and tabs from review title
        review['review_title'] = strip_duplicate_whitespace(review['review_title'])
        review['rating_value'] = re.search(r'^(\d) out of 5 stars', review['rating_text']).group(1)
        reviews.append(review)
    return reviews


def get_json_schema(soup):
    json_schema_script = soup.find('script', {'type': 'application/ld+json', 'data-bots-only': 'true',
                                              'data-react-helmet': 'true'})
    return json.loads(json_schema_script.text)


def main():
    all_reviews = []
    # Get all HTML files
    html_files = get_html_files()
    # Load HTML files
    html_soup = load_html_files(html_files)
    for soup in html_soup:
        # Get title of page and split by ' | '
        brand, website = soup.title.text.split(' | ')
        try:
            pat = re.compile(r'^(.*?) \(page (\d+)\)')
            page = re.search(pat, brand).group(2)
            brand = re.search(pat, brand).group(1)
        except AttributeError:
            page = 1
        json_schema = get_json_schema(soup)
        # Save JSON schema to file
        json_filename = os.path.join(processed_dir, f'{brand.lower()}-productreview-com-au-page-{page}.json')
        with open(json_filename, 'w') as f:
            json.dump(json_schema, f, indent=4)
        # Get all review divs
        review_divs = get_review_divs(soup)
        # Parse reviews
        parsed_reviews = parse_html_reviews(review_divs)
        for review in parsed_reviews:
            review['website'] = website
            review['brand'] = brand
            review['page'] = page

        all_reviews.extend(parsed_reviews)
    # Save to CSV
    df = pd.DataFrame(all_reviews)
    df.to_csv(os.path.join(processed_dir, 'all-reviews-productreviews-com-au.csv'), index=False)


if __name__ == '__main__':
    main()
