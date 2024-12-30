import sqlite3

dbName = "bofh.db"
sqliteConnection = sqlite3.connect(dbName)
cursor = sqliteConnection.cursor()

#add pubyear
def pubYear():
    select = "select link, pubDate from bofh;"
    update = "update bofh set pubYear = ? where link = ?;"
    cursor.execute(select)
    linkList = cursor.fetchall()

    count = len(linkList)
    for i in range(count):
        link = linkList[i][0]
        pubDate = linkList[i][1]
        pubYear = pubDate[:4]
        cursor.execute(update, (pubYear, link))

#remove empty <p>
def removeEmptyP():
    select = "select link, story from bofh;"
    update = "update bofh set story = ? where link = ?;"
    cursor.execute(select)
    linkList = cursor.fetchall()

    count = len(linkList)
    for i in range(count):
        link = linkList[i][0]
        story = linkList[i][1]
        #fixedStory = story.replace("BOFH 2004", "")
        fixedStory = story.replace("<p> </p>", "")
        cursor.execute(update, (fixedStory, link))

#Fix episode numbers
def twoDigitEpisode():
    print('not yet')

#pubYear()
removeEmptyP()
#twoDigitEpisode()

sqliteConnection.commit()
sqliteConnection.close()

#maybe remove <br> in story
#stop them from being added