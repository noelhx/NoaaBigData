import psycopg2
import sys
import os
# -*- coding: utf-8 -*-
# Connect Module
try:
	conn = psycopg2.connect("dbname='mydb' user='chenpy' host='localhost'")
	conn.autocommit= True
	print "connect successful"
	cur = conn.cursor()
except:
	print "I am unable to connect to the database"


# File Open Module
#name = sys.argv[1]
#print(sys.argv[1]


for nums in range(1901,2014):
	for root, dirs, files in 
		os.walk('/Users/chenpy/NoaaBigData/%s'%nums):
		print root
		for f in files:
			print os.path.join(root, f)
			name=os.path.join(root, f)
			file = open(name,'r')
			while True:
				line=file.readline()
				if not line: break
				USAF = line[4:10]
				WBAN = line[10:15]
				observDate = line[15:23]
				observTime = line[23:27]
				geoLat = line[28:34]
				geoLon = line[34:41]
				windSpeed = line[65:69]
				airTemp = line[87:92]
				atmoPressure= line[99:104]
	#	print(line[105:110])
	#	print(line)
				if line[105:110]== "ADDAA":
					preciHours=line[121:123]
					preciDepth=line[123:127]
				else:
					preciHours=-1
					preciDepth=-1
	# insert into database
				try:
					cur.execute("INSERT INTO year_1901 (USAF,WBAN,GDATE,GTIME,LAT,LON,WINDRATE,AIRTEMP,PRESSURE,PRECIPITATION_TIME,PRECIPITATION_DEPTH) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(USAF,WBAN,observDate,observTime,geoLat,geoLon,windSpeed,airTemp,atmoPressure,preciHours,preciDepth))
				except:
					print "cant insert"
#	print("""INSERT INTO year_1901 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",(USAF,WBAN,observDate,observTime,geoLat,geoLon,windSpeed,airTemp,atmoPressure,preciHours,preciDepth))
			file.close()
