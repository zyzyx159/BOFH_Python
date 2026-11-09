import episode
import os
import database
from ebooklib import epub
import ebooklib
import TOCbuilder

class export:
    def __init__(self):
        self.DB = database.database()
        self.spineCount = 2

        self.book = epub.EpubBook()
        self.book.set_identifier('BOFH Omnibus')
        self.book.set_title('The BOFH Omnibus')
        self.book.set_language('en')
        self.book.add_author('Simon Travaglia')
        self.book.set_cover("image/bofh_phone_cover.png", open('image/bofh_phone_cover.png', 'rb').read())
        
        cover = epub.EpubHtml(title='Cover', file_name='intro.xhtml',lang='en')
        cover.content='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml"><head>
            <title>The Complete BOFH Omnibus</title>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            </head><body><img src="image/bofh_phone_cover.png" alt="horned phone" />
            </body></html>'''
        self.book.add_item(cover)
        self.book.spine.insert(0,cover)
    
    def incrementSpineCount(self):
        self.spineCount = self.spineCount + 1

    def getSpineCount(self):
        return self.spineCount
    
    def buildBook(self):
        # get sorted list of years
        years = self.DB.getPubYears()
        toc = TOCbuilder.TOC()
        for year in years:
            toc.startSection(year[0])
            links = self.DB.getLinksByYear(year[0]) #links by year ordered by episodeNum ASC
            for link in links: 
                epi = episode.episode(link[0]) # build episode per link
                epi.DBInit()
                toc.addChapter(epi.getFileName(), epi.getChapterTitle())
                chap = epub.EpubHtml(title=epi.getTitle(),
                    file_name=epi.getFileName(), lang='en')
                chap.content=epi.getEpiString()
                self.book.add_item(chap)
                self.book.spine.insert(self.getSpineCount(), chap)
                self.incrementSpineCount()
            toc.endSection()
        self.book.add_item(toc.getTOC())
        self.book.spine.insert(1,toc.getTOC())
        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())

        epub.write_epub('/app/output/bofh.epub', self.book)