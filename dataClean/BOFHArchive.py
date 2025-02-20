class episode:
#region init
    def __init__(self, URL):
        self.url = URL
        self.downloaded = "True"
#endregion

#region set
    def setEpisodeNum(self, episodeNum):
        self.episodeNum = episodeNum

    def setTitle(self, title):
        self.title = title

    def setSubtitle(self, subtitle):
        self.subtitle = subtitle

    def setAuthor(self, author):
        self.author = author

    def setPubDate(self, pubDate): 
        self.pubDate = pubDate
    
    def setPubYear(self, pubYear):
        self.pubYear = pubYear
    def setStory(self, story):
        self.story = story
#endregion

#region get
    def getURL(self):
        return self.url

    def getDownloaded(self):
        return "True"

    def getEpisodeNum(self):
        return self.episodeNum

    def getTitle(self):
        return self.title

    def getSubtitle(self):
        return self.subtitle

    def getAuthor(self):
        return self.author

    def getPubDate(self):
        return self.pubDate

    def getPubYear(self):
        return self.pubYear

    def getStory(self):
        return self.story
#endregion

#region methods
    def getFileName(self):
        formatEpiNum = str(self.getEpisodeNum()).translate(str.maketrans('','',string.punctuation))
        formatEpiNum = formatEpiNum.replace(" ", "_")
        formatEpiTitle = str(self.getTitle()).translate(str.maketrans('','',string.punctuation))
        formatEpiTitle = formatEpiTitle.replace(" ", "_")
        fileName = formatEpiNum + "-" + formatEpiTitle + ".xhtml"
        return fileName

    def getChapterTitle(self):
        chapterTitle = self.getEpisodeNum() + " - " + self.getTitle()
        return chapterTitle

    def getEpiString(self):
        epiString = '''<html>
            <head>
            <title> ''' + self.getEpisodeNum() + ''' - ''' + self.getTitle() + '''</title>
            </head>
            <body>
            <h1>''' + self.getTitle() + ''' </h1> 
            <h2>''' + self.getSubtitle() + ''' </h2>
            <h3>''' + self.getEpisodeNum() + ''' </h3>
            ''' + self.getStory() + '''
            Written by: ''' + self.getAuthor() + '''
            <br> Posted to: <a href="''' + self.getURL() + '''"> ''' + self.getURL() + '''</a> </br>
            Posted on: ''' + self.formatPubDate('long') + '''
            </body> </html>'''
        return epiString
#endregion