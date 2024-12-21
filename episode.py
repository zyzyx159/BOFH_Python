from datetime import datetime
import pytz
import database
import string

class episode:
#region init
    def __init__(self, URL):
        self.url = URL
        self.downloaded = "True"

    def DBInit(self):
        bofhDB = database.database()
        row = bofhDB.episodeFromDB(self.getURL())
        self.episodeNum = row[0][0]
        self.title = row[0][1]
        self.subtitle = row[0][2]
        self.author = row[0][3]
        self.pubDate = row[0][4]
        self.story = row[0][5]
        bofhDB.close
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

    def setPubDate(self, pubDate): #demo pubDate: "Fri 22 Nov 2024 // 09:25 UTC"
        importFormat = ("%a %d %b %Y // %H:%M %Z")
        dt = datetime.strptime(pubDate, importFormat)
        self.pubDate = dt
        #self.pubDate = dt.astimezone(pytz.timezone('UTC'))
        
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

    def getStory(self):
        return self.story
#endregion

#region methods
    def formatPubDate(self, format):
        dbFormat = ("%Y-%m-%d %H:%M:%S")
        strDate = datetime.strptime(self.pubDate, dbFormat)
        forYear = ("%Y") #2024
        forShort = ("%Y-%m-%d") #2024-11-22
        forLong = ("%A, %B %d, %Y at %H:%M %Z") #Friday, November 22 2024 at 09:25 UTC
        if format == 'year':
            return strDate.strftime(forYear)
        elif format == 'short':
            return strDate.strftime(forShort)
        elif format == 'long':
            return strDate.strftime(forLong) + 'UTC'

    def printShort(self):
        print(self.episodeNum)
        print("Title = " + self.title)
        print("Subtitle = " + self.subtitle)
        print("Author = " + self.author)
        print("Published on (short) = "+ self.formatPubDate('short'))
        print("Published on (long) = " + self.formatPubDate('long'))

    def printStory(self):
        print("Story = " + self.story)

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