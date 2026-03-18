from playwright.sync_api import sync_playwright

def run_scraper():
    print("Starting the browser....")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        print("Navigating to the test site...")
        page.goto("http://quotes.toscrape.com/")
        page_title = page.title()
        print(f"Success! The website tilte is : {page_title}")
        page.wait_for_timeout(3000)
        browser.close()
        print("Browser closed.")

if __name__ == "__main__":
    run_scraper()