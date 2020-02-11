import sqlite3

def sqlite_init():
    sqliteConnection = sqlite3.connect('sqlite.db')
    with sqliteConnection:
        cur = sqliteConnection.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='node';")
        if not cur.fetchone():
            cur.execute("CREATE TABLE node(id INT, name TEXT, iduser INT, node TEXT)")
        return cur
