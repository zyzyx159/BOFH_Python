from playwright.sync_api import sync_playwright, playwright
import database
import bjashEpisode
import datetime
# import export

#get all the links of episodes I have not downloaded yet
bofhDB = database.database() #TODO: May need a custom db object
# bofhDB.download()

def run(playwright: playwright, URL):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(URL)

    #make an episode instance for each
    epi = bjashEpisode.episode(URL)

    # topCol = page.query_selector("#top-col-story")
    # titles = topCol.query_selector_all("h1")
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
        "https://bofh.bjash.com/bofh/genesis1.html"
    ]
    for i in range(0, len(linkList)):
        bofhDB.insert(linkList[i])
        play = run(playwright, linkList[i])
        singleDigit = re.findall(r'(?<!\S)\d(?!\S)',str(i+1))
        episodeNum = episodeNum.replace(singleDigit, singleDigit.zfill(2))
        play.setEpisodeNum("EPISODE " + episodeNum)
        play.setAuthor("Simon Travaglia")
        play.setPubDate(datetime.datetime(1994,1,1))
        play.setPubYear('1994')
        bofhDB.update(play)
