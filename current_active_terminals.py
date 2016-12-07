#This function retrieves data from the minute_log and pulls it out in a column format for the client.
#Written by Christie Vasquez and Takara Larsen.

#we were focused on which users were active.

def current_active_users():
	#<<GENERAL>>
	#import SQLite3 Libraries
	import sqlite3
	import datetime
	import time
	from datetime import date 
	#POSIX
	#Connect to SQLite3 Database, "QATWatch.db"
	conn = sqlite3.connect("/home/Jennifer.Meggs/QATWatch/Source/QATWatch.db")
	conn.text_factory = str 
	#Gain editing power
	c = conn.cursor()

	#<<GET TIMESTAMP AT TOP>>
        c.execute("select max(timestamp) from minute_log")
	maxtimestamp=c.fetchone()
	timestamp = date.fromtimestamp(maxtimestamp[0])
	print("User Data Retrieved from " + time.ctime(maxtimestamp[0]))
	
	#<CURRENT ACTIVE USERS> --> need to make sure users are not idle
	c.execute("SELECT uname,terminal,login_time from minute_log WHERE time_idle = '.' AND timestamp = (select max(timestamp) from minute_log) ORDER BY uname")
	active_unames = c.fetchall()
	print "\n\nCURRENT ACTIVE USERS\n--------------------\n"
	print "Username                      Terminal       Login Time          \n-------------------------------------------------------\n"
        for user in active_unames:
   		spaceuname= 30-len(user[0])
        	spaceterminal = 15-len(user[1])
		print(user[0] + (spaceuname*" ") + user[1]+(spaceterminal*" ") + user[2])
	print"\n-------------------------------------------------------\n"

	#<<UNAME>> --> make sure users are not idle.#execute query asking to count unique uname inputs from minute log
	c.execute("SELECT COUNT(DISTINCT uname) from minute_log WHERE time_idle = '.' AND timestamp = (select max(timestamp) from minute_log)")
	#fetch number and print it
	distinct_uname = c.fetchone()
	print "There are %s Total Distinct Active Users" %(distinct_uname[0])

	#<<TERMINALS>> --> where timestamp = maxtimestamp #execute query asking for all terminals from minute log
	c.execute("SELECT COUNT (terminal) from minute_log WHERE time_idle = '.' AND timestamp = (select max(timestamp) from minute_log)")
	terminalnum = c.fetchone()
	print "There are %s Total Active Terminals" %(terminalnum[0])
	print"\n-------------------------------------------------------\n"

