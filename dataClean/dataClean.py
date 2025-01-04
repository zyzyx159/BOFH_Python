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

def twoDigitEpisode():
    select = '''select link, episodeNum from bofh;'''
    update = '''update bofh set episodeNum = ? where link = ?;'''
    cursor.execute(select)
    linkList = cursor.fetchall()

    count = len(linkList)
    for i in range(count):
        link = linkList[i][0]
        num = linkList[i][1]
        num = num.replace("EPISODE ", "")
        num = "EPISODE " + str(num).zfill(2)
        cursor.execute(update, (num, link))

#pubYear()
#removeEmptyP()
twoDigitEpisode()

sqliteConnection.commit()
sqliteConnection.close()

#maybe remove <br> in story
#stop them from being added