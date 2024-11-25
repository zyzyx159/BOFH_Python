import sqlite3

testQuery = '''select link from bofh where downloaded = 'false' limit 1;'''

class story:
    def __init__(self):
            self.somecode() 
    
    def testQuery(self):
        dbName = "bofh.db"
        sqliteConnection = sqlite3.connect(dbName)
        cursor = sqliteConnection.cursor()
        cursor.execute(testQuery):
        self.url = cursor.fetchone()[0]

