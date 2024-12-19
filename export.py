import episode
import os

class export:
    def __init__(self, epi: episode):
        self.epi = epi
    
    def getPath(self):
        path = os.path.join(os.path.dirname(__file__), "output", self.epi.formatPubDate('year'))
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def getFileName(self):
        fileName = self.epi.getEpisodeNum() + "_" + self.epi.getTitle() + ".html"
        return fileName

    def getEpiString(self):
        epiString = '''<html>
            <head>
            <title> ''' + self.epi.getEpisodeNum() + ''' - ''' + self.epi.getTitle() + '''</title>
            </head>
            <body>
            <h1>''' + self.epi.getTitle() + ''' </h1> 
            <h2>''' + self.epi.getSubtitle() + ''' </h2>
            <h3>''' + self.epi.getEpisodeNum() + ''' </h3>
            ''' + self.epi.getStory() + '''
            Written by: ''' + self.epi.getAuthor() + '''
            <br> Posted to: <a href="''' + self.epi.getURL() + '''"> ''' + self.epi.getURL() + '''</a> </br>
            Posted on: ''' + self.epi.formatPubDate('long') + '''
            </body> </html>'''
        return epiString
    
    def writeFile(self):
        with open(os.path.join(self.getPath(), self.getFileName()), "w") as f:
            f.write(self.getEpiString())
