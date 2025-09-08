import sqlite3 as sql

def listListing():
  con = sql.connect("database/data_source.db")
  cur = con.cursor()
  data = cur.execute('SELECT * FROM Listings').fetchall()
  con.close()
  return data