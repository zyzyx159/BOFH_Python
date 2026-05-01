import getLinks
import database
import getEpisode
import getExport
from playwright.sync_api import sync_playwright

db = database.database()
if db.newLinks() > 0:
    getEpisode()
    getExport()
#need to build a distribution system

if __name__ == "__main__":
    with sync_playwright() as p:
        # Call the function from your imported module
        getLinks.run(p, startURL="https://www.theregister.com/offbeat/bofh/")
