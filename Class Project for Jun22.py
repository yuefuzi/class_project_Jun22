# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 00:33:55 2016

@author: Chang
"""
from __future__ import print_function
import sqlite3 as lite
import pandas as pd
con = lite.connect('/Users/Chang/getting_started.db')

cities = (('New York City','NY'),
    ('Boston','MA'),
    ('Chicago','IL'),
    ('Miami','FL'),
    ('Dallas','TX'),
    ('Seattle','WA'),
    ('Portland','OR'),
    ('San Francisco','CA'),
    ('Los Angeles','CA'))

with con:
    cur = con.cursor()
    
    cur.execute("DROP TABLE IF EXISTS cities1")
    cur.execute("DROP TABLE IF EXISTS weather1")
    
    cur.execute("CREATE TABLE cities1 (name text, state text)")
    
    cur.execute("CREATE TABLE weather1 (city text,year integer,warm_month text,cold_month text,average_high integer)")
    cur.execute("INSERT INTO weather1 VALUES('Boston',2013,'July','January',59)")
    cur.execute("INSERT INTO weather1 VALUES('Chicago',2013,'July','January',59)")
    cur.execute("INSERT INTO weather1 VALUES('Miami',2013,'August','January',84)")
    cur.execute("INSERT INTO weather1 VALUES('Dallas',2013,'July','January',77)")
    cur.execute("INSERT INTO weather1 VALUES('Seattle',2013,'July','January',61)")
    cur.execute("INSERT INTO weather1 VALUES('Portland',2013,'July','December',63)")
    cur.execute("INSERT INTO weather1 VALUES('San Francisco',2013,'September','December',64)")
    cur.execute("INSERT INTO weather1 VALUES('Los Angeles',2013,'September','December',75)")
    
    cur.executemany("INSERT INTO cities1 VALUES(?,?)",cities)
    
    
    cur.execute("""SELECT name, state, year, warm_month, cold_month, average_high 
    FROM cities1
    INNER JOIN weather1
        ON name = city""")
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)  

    print("The cities that are warmest in July are: ",end='')
    for i in range(0,8):
        if df.get_value(i,'warm_month') == 'July':
            print(df.get_value(i,'name'),end='')
    print(".")
        

        
        
    
''' rows = cur.fetchall()
    for row in rows:
        print(row)
'''    
    
'''    
    cur.execute("SELECT * FROM cities1")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    print("------------")    
    cur.execute("SELECT * FROM weather1")
    rows = cur.fetchall()
    for row in rows:
        print(row)
'''