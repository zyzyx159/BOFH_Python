import sqlite3
import episode

class database:
    def __init__(self):
        self.dbName = "bofh.db"
        self.sqliteConnection = sqlite3.connect(self.dbName)
        self.cursor = self.sqliteConnection.cursor()

        self.createQuery = '''CREATE table if not exists bofh(
            link TEXT primary key,
            downloaded TEXT, 
            episodeNum TEXT,
            title TEXT,
            subtitle TEXT,
            author TEXT,
            pubDate TEXT,
            story TEXT);'''
        self.countQuery = '''SELECT count(*) 
            FROM bofh 
            WHERE link = ?'''
        self.insertQuery = '''INSERT into bofh(
            link, downloaded) 
            VALUES (?, "False");'''
        self.downloadQuery = '''SELECT link 
            FROM bofh 
            WHERE downloaded = 'False' limit 1;'''
            #for testing this is limited to just the top one.
        self.updateQuery = '''UPDATE bofh
            SET downloaded = ?,
            episodeNum = ?,
            title = ?,
            subtitle = ?,
            author = ?,
            pubDate = ?,
            story = ?
            WHERE link = ?;'''
        self.episodeFromDBQuery = '''SELECT episodeNum,
            title,
            subtitle,
            author,
            pubDate,
            story
            FROM bofh
            WHERE link = ?;'''

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
            episode.getEpisodeNum(), episode.getTitle(), episode.getSubtitle(), 
            episode.getAuthor(), episode.getPubDate(), 
            episode.getStory(), episode.getURL(),))
        self.sqliteConnection.commit()

    def episodeFromDB(self, URL):
        self.cursor.execute(self.episodeFromDBQuery, (URL,))
        episodeFromDB = self.cursor.fetchall()
        return episodeFromDB

    def close(self):
        self.sqliteConnection.close()
