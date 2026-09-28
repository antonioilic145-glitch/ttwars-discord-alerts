from playwright.sync_api import sync_playwright

url = "https://www.ttwars.com/international/calendar"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(url, wait_until="networkidle", timeout=60000)

    print("STATUS:", page.url)
    print("TITLE:", page.title())
    print("TEXT:")
    print(page.locator("body").inner_text())

    browser.close()
