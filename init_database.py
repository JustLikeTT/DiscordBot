import sqlite3

if __name__ == '__main__':
    connect = sqlite3.connect("main.db")

    c = connect.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS Article
        (ID INTEGER PRIMARY KEY ,
        timesOfAppearance INTEGER NOT NULL DEFAULT 1,
        dataOfAppended TEXT NOT NULL);'''
        )
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS User
        (articleID INTEGER not null,
        numberOfArticle INTEGER NOT NULL DEFAULT 0,
        ID TEXT PRIMARY KEY ,
        FOREIGN KEY(articleID) REFERENCES Article(ID));
        '''
        )
    c.execute(
        '''CREATE TABLE IF NOT EXISTS Text
        (ID INTEGER PRIMARY KEY ,
        content TEXT NOT NULL unique,
        FOREIGN KEY(ID) REFERENCES Article(ID));'''
        )
    c.execute(
        '''CREATE TABLE IF NOT EXISTS Image
        (ID INTEGER PRIMARY KEY , 
        path TEXT NOT NULL unique,
        FOREIGN KEY(ID) REFERENCES Article(ID));'''
        )