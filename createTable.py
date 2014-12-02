import psycopg2
# Connect Module
try:
	conn = psycopg2.connect("dbname='mydb' user='chenpy' host='localhost'")
	conn.autocommit= True
	print "connect successful"
	cur = conn.cursor()
except:     
	print "I am unable to connect to the database"


# Create Table Module
for num in range(1902,2015):
	try:
		str=cur.mogrify('CREATE TABLE year_%s(USAF char(6),WBAN char(5),GDATE char(8),GTIME char(8),LAT char(8),LON char(8),WINDRATE char(4),AIRTEMP char(5),PRESSURE char(5),PRECIPITATION_TIME char(2),PRECIPITATION_DEPTH char(4));'%(num))
		print(str)
		cur.execute('CREATE TABLE year_%s(USAF char(6),WBAN char(5),GDATE char(8),GTIME char(8),LAT char(8),LON char(8),WINDRATE char(4),AIRTEMP char(5),PRESSURE char(5),PRECIPITATION_TIME char(2),PRECIPITATION_DEPTH char(4));'%(num))
	except:
		print "unable to create table"
