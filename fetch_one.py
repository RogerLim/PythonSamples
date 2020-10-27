#!/usr/bin/python

import sqlite3

con = sqlite3.connect('nzbdrone.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM MovieFiles")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        print(f"{row[0]} {row[1]} {row[2]}")
