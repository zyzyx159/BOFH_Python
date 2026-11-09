import ebooklib
from ebooklib import epub

class TOC:
    def __init__(self):
        self.chapter = epub.EpubHtml(title='Table of Contents', file_name='TOC.xhtml', lang='en')
        self.table = self.getHeader()
        # self.table = ''

    def getChapter(self):
        return self.chapter

    def getTable(self):
        return self.table

    def startSection(self, header):
        self.table = self.getTable() + '''<li>''' + header + '''</li><ul>'''

    def addChapter(self, fileName, chapTitle):
        self.table = self.getTable() + '''<li><a href="''' + fileName + '''">
            ''' + chapTitle + '''</a></li>'''

    def endSection(self):
        self.table = self.getTable() + '''</ul>'''

    def getTOC(self):
        #finishedTable = self.getHeader() + self.getTable() + self.getFooter()
        finishedTable = self.getTable() + self.getFooter()
        chapter = self.getChapter()
        chapter.content = finishedTable
        return chapter

    def getHeader(self):
        header = '''
            <?xml version="1.0" encoding="UTF-8"?>
                <html xmlns="http://www.w3.org/1999/xhtml">
                    <body>
                        <nav epub:type="toc">
                            <h1>Table of Contents</h1>
                                <ul>'''
        return header
    
    def getFooter(self):
        footer = '''
                        </ul>
                    </nav>
                </body>
            </html>'''
        return footer