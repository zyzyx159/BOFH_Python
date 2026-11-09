import database
import getLinks
import getEpisode
from export import export
from playwright.sync_api import sync_playwright

def main():
    # 1. Scraping Phase
    with sync_playwright() as p:
        getLinks.run(p, startURL="https://www.theregister.com/bofh/")

    # 2. Database Check
    db = database.database()
    if db.newLinks() > 0:
        getEpisode.run()

    # 3. Export Phase
    book = export()
    book.buildBook()

if __name__ == "__main__":
    main()

