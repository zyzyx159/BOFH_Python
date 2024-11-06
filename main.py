from playwright.sync_api import sync_playwright, playwright
import sqlite3

sqliteConnection = sqlite3.connect('bofh')
cursor = sqliteConnection.cursor()

def run(playwright: playwright):
    start_url = "https://www.theregister.com/offbeat/bofh/"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(start_url)

    for link in page.locator("a[class=story_link]").all():
        url = link.get_attribute("href")
        if "bofh" in url:
            cursor.execute('select count ')

with sync_playwright() as playwright:
    run(playwright)