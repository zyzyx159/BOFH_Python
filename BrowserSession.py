from playwright.sync_api import sync_playwright, Playwright

class BrowserSession:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()

    def Navigate_to(self, url):
        self.page.goto(url)
    
    def close(self, url):
        self.browser.close()