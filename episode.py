class episode:
    def __init__(self, URL):
        self.url = URL
        self.downloaded = "True"

    def setTitle(self, title):
        self.title = title

    def setSubtitle(self, subtitle):
        self.subtitle = subtitle

    def setAuthor(self, author):
        self.author = author

    def setPubDate(self, pubDate):
        self.pubDate = pubDate

    def setStory(self, story):
        self.story = story

    def getURL(self):
        return self.url

    def getDownloaded(self):
        return "True"

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

    def printShort(self):
        print("Title = " + self.title)
        print("Subtitle = " + self.subtitle)
        print("Author = " + self.author)
        print("Published on = "+ self.pubDate)

    def printStory(self):
        print("Story = " + self.story)