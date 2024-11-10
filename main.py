from playwright.sync_api import sync_playwright, playwright
import sqlite3
import os

dbExists = os.path.exists('bofh.db')

sqliteConnection = sqlite3.connect('bofh.db')
cursor = sqliteConnection.cursor()

if not dbExists:
    cursor.execute('create table links(link varchar(255), downloaded varchar(5));')

def run(playwright: playwright):
    start_url = "https://www.theregister.com/offbeat/bofh/"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(start_url)

    for link in page.locator("a[class=story_link]").all():
        url = link.get_attribute("href")
        #print(url)
        countQuery = "select count(*) from links where link = ?"
        insertQuery = "insert into links (link, downloaded) values (?, 'false');"
        urlBase = 'www.theregister.com'
        if "bofh" in url:
            cursor.execute(countQuery, (url,))
            count = cursor.fetchall()
            #Fetch all returns a tuple in a tuple and this is the only way I can convert to an int
            i = count[0]
            k = i[0]
            if k == 0:
                cursor.execute(insertQuery, (urlBase + url,))
                sqliteConnection.commit()
    sqliteConnection.close()

with sync_playwright() as playwright:
    run(playwright)