import psycopg2
# -*- coding: utf-8 -*-
# Connect Module
try:
	conn = psycopg2.connect("dbname='mydb' user='chenpy' host='localhost'")
	print "connect successful"
	cur = conn.cursor()
except:
	print "I am unable to connect to the database"

cur.execute("select * from isd_inventory")
for record in cur:
	print record;

