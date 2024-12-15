from datetime import datetime
import pytz
import database

class episode:
#region init
    def __init__(self, URL):
        self.url = URL
        self.downloaded = "True"

    def DBInit(self):
        bofhDB = database.database()
        row = bofhDB.episodeFromDB(self.getURL())
        self.episodeNum = row[0]
        self.title = row[1]
        self.subtitle = row[2]
        self.author = row[3]
        self.pubDate = row[4]
        self.story = row[5]
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
        forShort = ("%Y-%m-%d") #2024-11-22
        forLong = ("%A, %B %d, %Y at %H:%M %Z") #Friday, November 22 2024 at 09:25 UTC
        if format == 'short':
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
#endregion