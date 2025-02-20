from playwright.sync_api import sync_playwright, playwright
import database
import BOFHArchive
import datetime

bofhDB = database.database() 

def run(playwright: playwright, URL):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(URL)

    #make an episode instance for each
    epi = BOFHArchive.episode(URL)

    pTags = page.query_selector_all("p")
    title = "The Bastard Operator From Hell"
    epi.setTitle(title)
    subtitle = page.query_selector("h2").inner_text()
    #subtitle = pTags[0].inner_text()
    subtitle = subtitle.replace(title + "\n", "")
    epi.setSubtitle(subtitle)

    epiStory = "<br />"
    for i in range(1, len(pTags)):
        epiStory = epiStory + "<p>" + pTags[i].inner_text() + "</p>"
    epi.setStory(epiStory)

    browser.close()

    return epi

#make a PlayWright instance for each
with sync_playwright() as playwright:
    year = 1999
    link = 'http://www.bofharchive.com/1999/bastard99-27.html'
    #link = 'http://www.bofharchive.com/1999/bastard99-'
    linkList = []

    # for i in range(1,27):
    #     linkList.append(link + str(i).zfill(2) + '.html')

    linkList.append(link)

    for i in range(0, len(linkList)):
        bofhDB.insert(linkList[i])
        play = run(playwright, linkList[i])
        play.setEpisodeNum('EPISODE 27')# + str(i + 1).zfill(2))
        play.setAuthor("Simon Travaglia")
        date_string = 'jan 1 ' + str(year)
        datetime_object = datetime.datetime.strptime(date_string, '%b %d %Y')
        play.setPubDate(datetime_object)
        play.setPubYear(year)
        bofhDB.update(play)