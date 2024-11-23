import sqlite3

class database:
    def __init__(self):
        self.dbName = "bofh.db"
        self.sqliteConnection = sqlite3.connect(self.dbName)
        self.cursor = self.sqliteConnection.cursor()

        self.createQuery = '''create table if not exists bofh(link text primary key,
            downloaded text, title text,
            subtitle text,
            author text,
            pubDate text,
            story text);'''
        self.countQuery = "select count(*) from bofh where link = ?"
        self.insertQuery = "insert into bofh (link, downloaded) values (?, 'false');"

        self.cursor.execute(self.createQuery)

    def count(self, URL):
        self.cursor.execute(self.countQuery, (URL,))
        count = self.cursor.fetchall()
        #print(count[0][0])
        return count[0][0]

    def insert(self, URL):
        self.cursor.execute(self.insertQuery, (URL,))
        self.sqliteConnection.commit()

    def close(self):
        self.sqliteConnection.close()
