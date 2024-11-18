from playwright.sync_api import sync_playwright, playwright
import sqlite3

dbName = "bofh.db"
sqliteConnection = sqlite3.connect(dbName)
cursor = sqliteConnection.cursor()

testQuery = '''select link from bofh where downloaded = 'false' limit 1;'''

def run(playwright: playwright, startURL):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(startURL)



with sync_playwright() as playwright:
    cursor.execute(testQuery)
    url = cursor.fetchone()[0]
    current = run(playwright, url)

