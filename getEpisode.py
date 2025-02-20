from playwright.sync_api import sync_playwright, playwright
import database
import episode
import export
import re

#get all the links of episodes I have not downloaded yet
bofhDB = database.database()
bofhDB.download()

def run(playwright: playwright, URL):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(URL)

    #make an episode instance for each
    epi = episode.episode(URL)

    topCol = page.query_selector("#top-col-story")
    titles = topCol.query_selector_all("h1")
    epi.setTitle(titles[0].inner_text())

    subtitles = topCol.query_selector_all("h2")
    epi.setSubtitle(subtitles[0].inner_text())

    authors = topCol.query_selector_all(".byline")
    epi.setAuthor(authors[0].inner_text())

    published = topCol.query_selector_all(".dateline")
    epi.setPubDate(published[0].inner_text())

    pageBody = page.query_selector("#body")
    episodeNumList = pageBody.query_selector_all('span.label')
    episodeNum = episodeNumList[0].inner_text()
    singleDigit = re.findall(r'\d+', episodeNum)[0]
    episodeNum = episodeNum.replace(singleDigit, singleDigit.zfill(2))
    epi.setEpisodeNum(episodeNum)

    story = pageBody.query_selector_all("p")
    epiStory = "<br />"
    for p in story:
        epiStory = epiStory + "<p>" + p.inner_text() + "</p>"
    epiStory = epiStory.replace(episodeNum, "")
    epi.setStory(epiStory)

    browser.close()

    return epi

#make a PlayWright instance for each
with sync_playwright() as playwright:
    for link in bofhDB.download():
        play = run(playwright, link[0])
        play.setPubYear()
        bofhDB.update(play)
