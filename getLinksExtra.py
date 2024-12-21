from playwright.sync_api import sync_playwright, playwright
import database

urlBase = 'https://www.theregister.com'
bofhDB = database.database()

def run(playwright: playwright, startURL):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(startURL)

    for link in page.locator('#body').locator('p').locator('a').all():
        url = link.get_attribute("href")
        print(url)
        if bofhDB.count(url) == 0:
            bofhDB.insert(url,)

def deleteJunkLinks():
    #there is no good way for the computer to spot these, easier to do manually
    junkLinks = [''] * 17
    junkLinks[0] = 'https://www.theregister.com/2002/05/11/2001_a_bofh_odyssey/'
    
    for i in range(0,17):
        bofhDB.delete(junkLinks[i])

with sync_playwright() as playwright:
    extra = ['https://www.theregister.com/2002/05/11/2001_a_bofh_odyssey/',
        'https://www.theregister.com/2003/01/27/bofh_2002_a_readers_digest/',
        'https://www.theregister.com/2004/02/11/bofh_2003_year_book/',
        'https://www.theregister.com/2004/09/27/bofh_2004_archive/',
        'https://www.theregister.com/2005/08/02/bofh_2005_archive/',
        'https://www.theregister.com/2007/01/02/bofh_2006_archive/',
        'https://www.theregister.com/2008/01/14/bofh_2007_archive/']

    for link in extra:
        run(playwright, startURL=link)
    bofhDB.close()