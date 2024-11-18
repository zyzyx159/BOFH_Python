from playwright.sync_api import sync_playwright, playwright
import sqlite3

dbName = "bofh.db"
urlBase = 'https://www.theregister.com'

sqliteConnection = sqlite3.connect(dbName)
cursor = sqliteConnection.cursor()

createQuery = '''create table if not exists bofh(link text primary key,
    downloaded text, title text,
    subtitle text,
    author text,
    pubDate text,
    story text);'''
countQuery = "select count(*) from bofh where link = ?"
insertQuery = "insert into bofh (link, downloaded) values (?, 'false');"

cursor.execute(createQuery)

def run(playwright: playwright, startURL):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(startURL)

    bofhLink = 0
    newLink = 0
        
    for link in page.locator("a[class=story_link]").all():
        url = link.get_attribute("href")
        if "bofh" in url:
            bofhLink += 1
            cursor.execute(countQuery, (urlBase + url,))
            count = cursor.fetchall()
            if count[0][0] == 0:
                newLink += 1
                cursor.execute(insertQuery, (urlBase + url,))
    sqliteConnection.commit()
    if bofhLink > newLink:
        nextPage = False
    elif bofhLink == 0:
        nextPage = False
    else:
        nextPage = True
    return nextPage

with sync_playwright() as playwright:
    current = run(playwright, startURL="https://www.theregister.com/offbeat/bofh/")
    earlier = 1
    if current == True:
        archive = True
        while archive == True:
            archive = run(playwright, startURL="https://www.theregister.com/offbeat/bofh/earlier/" + str(earlier) + "/")
            earlier += 1
    sqliteConnection.close()