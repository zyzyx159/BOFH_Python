from datetime import datetime
import pytz

class episode:
    def __init__(self, URL):
        self.url = URL
        self.downloaded = "True"

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
        self.pubDate = dt.replace(tzinfo=pytz.utc)
        
    def setStory(self, story):
        self.story = story

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

    def getPubDate(self, format, TZ):
        forShort = ("%Y-%m-%d") #2024-11-22
        forLong = ("%A, %B %d %Y at %H:%M %Z") #Friday, November 22 2024 at 09:25 UTC
        if format == 'short':
            return self.pubDate.strftime(forShort)
        elif format == 'long' and TZ == None:
            return self.pubDate.strftime(forLong)
        elif format == 'long' and TZ != None:
            return self.pubDate.astimezone(pytz.timezone(TZ)).strftime(forLong)

    def getStory(self):
        return self.story

    def printShort(self):
        print(self.episodeNum)
        print("Title = " + self.title)
        print("Subtitle = " + self.subtitle)
        print("Author = " + self.author)
        print("Published on (short) = "+ self.pubDate, 'short')
        print("Published on (long) = " + self.pubDate, 'long')
        print("Published on (long, central) = " + self.pubDate, 'long', 'US/Central')

    def printStory(self):
        print("Story = " + self.story)