import time

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright, listing="aldi", page_num=1) -> None:
    if page_num == 1:
        url = f"https://www.productreview.com.au/listings/{listing}#reviews-list"
    else:
        url = f"https://www.productreview.com.au/listings/{listing}?page={page_num}#reviews-list"
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(java_script_enabled=True,
                                  user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
    page = context.new_page()
    page.goto(url)
    for i in range(1, 10):
        page.mouse.wheel(0, 1500)
        time.sleep(0.5)
    time.sleep(2)
    content = page.content()
    with open(f'{listing}-productreview-com-au-page-{page_num}.html', 'w', encoding='utf-8') as f:
        f.write(content)
    context.close()
    browser.close()


with sync_playwright() as p:
    for listing in ["woolworths-physical-store"]:
        for _ in range(10, 11):
            run(p, listing=listing, page_num=_)
