import pymysql
import csv

conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "NFLDB")


cur = conn.cursor()

stmt = "INSERT INTO League (league_name) VALUES (%s)"


cur = conn.cursor()

data = [
  ('AFC East'),
  ('AFC North'),
  ('AFC South'),
  ('AFC West'),
  ('NFC East'),
  ('NFC North'),
  ('NFC South'),
  ('NFC West'),

]

cur.executemany(stmt, data)

conn.commit()


cur.close()
conn.close()
