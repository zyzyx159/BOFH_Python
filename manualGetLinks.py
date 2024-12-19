from playwright.sync_api import sync_playwright, playwright
import database

urlBase = 'https://www.theregister.com'
bofhDB = database.database()

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
            if bofhDB.count(urlBase + url) == 0:
                newLink += 1
                bofhDB.insert(urlBase + url,)
    if bofhLink > newLink:
        nextPage = False
    elif bofhLink == 0:
        nextPage = False
    else:
        nextPage = True
    return nextPage

with sync_playwright() as playwright:
    current = run(playwright, startURL="https://www.theregister.com/offbeat/bofh/earlier/8/")
    bofhDB.close()