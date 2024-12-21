import episode
import os
import database
from ebooklib import epub
import ebooklib

class export:
    def __init__(self):
        #self.epi = epi
        self.DB = database.database()
    
    def getPath(self):
        path = os.path.join(os.path.dirname(__file__), "output", self.epi.formatPubDate('year'))
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def writeHTML(self):
        with open(os.path.join(self.getPath(), self.getFileName()), "w") as f:
            f.write(self.getEpiString())

    def buildBook(self):
        book = epub.EpubBook()

        #base set up
        book.set_identifier('BOFH Omnibus')
        book.set_title('The BOFH Omnibus')
        book.set_language('en')
        book.add_author('Simon Travaglia')

        chapters = self.DB.getLinks()
        book.spine.insert(1, 'nav')
        i=2 #counter to add chapters with
        toc = [] #list of chapters for Table of Contents
        for chapter in chapters:
            epi = episode.episode(chapter[0])
            epi.DBInit()
            chap = epub.EpubHtml(title=epi.getTitle(), 
                file_name=epi.getFileName(),
                lang='en')
            chap.content=epi.getEpiString()
            book.add_item(chap)
            book.spine.insert(i, chap)
            toc.append(epub.Link(chap.file_name, chap.title, 'chapter'))
            i=i+1
        book.toc = (epub.Link('nav.xhtml', 'Table of Contents', 'toc'),
            (epub.Section('Chapters'),toc),)
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        epub.write_epub('bofh.epub', book)
