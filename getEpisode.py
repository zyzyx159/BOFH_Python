from playwright.sync_api import sync_playwright, playwright
import database
import episode

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
    episodeNum = pageBody.query_selector_all('span.label');
    epi.setEpisodeNum(episodeNum[0].inner_text())

    story = pageBody.query_selector_all("p:not(:has(span))")
    epiStory = "\n"
    for p in story:
        epiStory = epiStory + p.inner_text() + "\n"
    epi.setStory(epiStory)

    return epi

#make a PlayWright instance for each
with sync_playwright() as playwright:
    for link in bofhDB.download():
        play = run(playwright, link[0])
        bofhDB.update(play)