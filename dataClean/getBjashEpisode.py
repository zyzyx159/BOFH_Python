from playwright.sync_api import sync_playwright, playwright
import database
import bjashEpisode
import datetime

bofhDB = database.database() 

def run(playwright: playwright, URL):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(URL)

    #make an episode instance for each
    epi = bjashEpisode.episode(URL)

    pTags = page.query_selector_all("p")
    title = "The Bastard Operator From Hell"
    epi.setTitle(title)
    subtitle = pTags[0].inner_text()
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
    linkList = [
        "https://bofh.bjash.com/bofh/genesis1.html",
        "https://bofh.bjash.com/bofh/genesis2.html", 
        "https://bofh.bjash.com/bofh/genesis3.html",
        "https://bofh.bjash.com/bofh/bofh1.html",
        "https://bofh.bjash.com/bofh/bofh2.html", 
        "https://bofh.bjash.com/bofh/bofh3.html", 
        "https://bofh.bjash.com/bofh/bofh4.html", 
        "https://bofh.bjash.com/bofh/bofh5.html", 
        "https://bofh.bjash.com/bofh/bofh6.html", 
        "https://bofh.bjash.com/bofh/bofh7.html", 
        "https://bofh.bjash.com/bofh/bofh8.html", 
        "https://bofh.bjash.com/bofh/bofh9.html", 
        "https://bofh.bjash.com/bofh/bofh10.html", 
        "https://bofh.bjash.com/bofh/bofh11.html", 
        "https://bofh.bjash.com/bofh/bofh12.html", 
        "https://bofh.bjash.com/bofh/bofh13.html", 
        "https://bofh.bjash.com/bofh/bsmh1.html", 
        "https://bofh.bjash.com/bofh/bsmh2.html", 
        "https://bofh.bjash.com/bofh/bofh14.html", 
        "https://bofh.bjash.com/bofh/bofh15.html", 
        "https://bofh.bjash.com/bofh/bofb1.html", 
        "https://bofh.bjash.com/bofh/bofb2.html", 
        "https://bofh.bjash.com/bofh/lastbofh.html", 
        "https://bofh.bjash.com/bofh/brb.html", 
        "https://bofh.bjash.com/bofh/bib.html", 
        "https://bofh.bjash.com/bofh/tradeshow.html", 
        "https://bofh.bjash.com/bofh/bsa.html", 
        "https://bofh.bjash.com/bofh/xmas95.html", 
        "https://bofh.bjash.com/bofh/bofhfaq.html" # the text of this episode will not import correct. You will need to manually edit the database
    ]

    for i in range(0, len(linkList)):
        bofhDB.insert(linkList[i])
        play = run(playwright, linkList[i])
        play.setEpisodeNum("EPISODE " + str(i+1).zfill(2))
        play.setAuthor("Simon Travaglia")
        play.setPubDate(datetime.datetime(1994,1,1))
        play.setPubYear('1994')
        bofhDB.update(play)