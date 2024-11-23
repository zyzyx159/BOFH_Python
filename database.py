import sqlite3
import episode

class database:
    def __init__(self):
        self.dbName = "bofh.db"
        self.sqliteConnection = sqlite3.connect(self.dbName)
        self.cursor = self.sqliteConnection.cursor()

        self.createQuery = '''create table if not exists bofh(link text primary key,
            downloaded text, 
            title text,
            subtitle text,
            author text,
            pubDate text,
            story text);'''
        self.countQuery = "select count(*) from bofh where link = ?"
        self.insertQuery = "insert into bofh (link, downloaded) values (?, 'False');"
        self.downloadQuery = "select link from bofh where downloaded = 'False' limit 1;"
        self.updateQuery = '''update bofh
            set downloaded = ?,
            title = ?,
            author = ?,
            pubDate = ?,
            story = ?
            where link = ?;'''

        self.cursor.execute(self.createQuery)

    def count(self, URL):
        self.cursor.execute(self.countQuery, (URL,))
        count = self.cursor.fetchall()
        return count[0][0]

    def insert(self, URL):
        self.cursor.execute(self.insertQuery, (URL,))
        self.sqliteConnection.commit()

    def download(self):
        self.cursor.execute(self.downloadQuery)
        downloadList = self.cursor.fetchall()
        return downloadList

    def update(self, episode):
        self.cursor.execute(self.updateQuery, (episode.getDownloaded(),
            episode.getTitle(), episode.getAuthor(), episode.getPubDate(), 
            episode.getStory(), episode.getURL(),))
        self.sqliteConnection.commit()

    def close(self):
        self.sqliteConnection.close()
