from playwright.sync_api import sync_playwright, playwright
import database

urlBase = 'https://www.theregister.com'
bofhDB = database.database()

def run(playwright: playwright, startURL):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(startURL)

    for link in page.locator("a[class=story_link]").all():
        url = link.get_attribute("href")
        if bofhDB.count(urlBase + url) == 0:
            bofhDB.insert(urlBase + url,)

def deleteJunkLinks():
    #there is no good way for the computer to spot these, easier to do manually
    junkLinks = [''] * 17
    junkLinks[0] = 'https://www.theregister.com/2002/05/11/2001_a_bofh_odyssey/'
    junkLinks[1] = 'https://www.theregister.com/2003/01/27/bofh_2002_a_readers_digest/'
    junkLinks[2] = 'https://www.theregister.com/2004/02/11/bofh_2003_year_book/'
    junkLinks[3] = 'https://www.theregister.com/2004/09/27/bofh_2004_archive/'
    junkLinks[4] = 'https://www.theregister.com/2005/08/02/bofh_2005_archive/'
    junkLinks[5] = 'https://www.theregister.com/2007/01/02/bofh_2006_archive/'
    junkLinks[6] = 'https://www.theregister.com/2008/01/14/bofh_2007_archive/'
    junkLinks[7] = 'https://www.theregister.com/2002/01/29/bofh_ii_son/'
    junkLinks[8] = 'https://www.theregister.com/2002/01/08/salmon_days_is_spawned/'
    junkLinks[9] = 'https://www.theregister.com/2001/12/21/salmon_days_goes_live/'
    junkLinks[10] = 'https://www.theregister.com/2001/12/18/salmon_days_are_here_again/'
    junkLinks[11] = 'https://www.theregister.com/2001/12/18/salmon_days_declaration_of_principles/'
    junkLinks[12] = 'https://www.theregister.com/2001/12/17/salmon_days_is_go/'
    junkLinks[13] = 'https://www.theregister.com/2001/11/15/salmon_days_trailer_trash/'
    junkLinks[14] = 'https://www.theregister.com/2002/02/18/salmon_days_goes_live/'
    junkLinks[15] = 'https://www.theregister.com/2001/10/11/who_is_the_bastard/'
    junkLinks[16] = 'https://www.theregister.com/2004/03/11/bofh_protecting_our_backs/'
    
    for i in range(0,17):
        bofhDB.delete(junkLinks[i])

with sync_playwright() as playwright:
    for i in range(1,8): #may need to expand this some day
        archive = run(playwright, startURL="https://www.theregister.com/offbeat/bofh/earlier/" + str(i) + "/")
    deleteJunkLinks()
    bofhDB.close()