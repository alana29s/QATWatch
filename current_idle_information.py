def idle_users():

#using sqlite3 to display idle users as the second view of our main menu
#need to display uname, terminals, login time, and idle time as view fields
#these will be extracted from the minute log of our QATWatch database
#first thing we need is to import
	import os
	import sqlite3
	from datetime import date
	import time	

	conn = sqlite3.connect("/home/Jennifer.Meggs/QATWatch/Source/QATWatch.db")
	c = conn.cursor()
	conn.text_factory = str

# Timestamp before we show the idle users from the minute_log table
	c.execute("select max(timestamp) from minute_log")
	maxtimestamp = c.fetchone()
	timestamp = date.fromtimestamp(maxtimestamp[0])
#	print ("User Data Retrieved from %s" %(timestamp))
	print("User Data Retrieved From: " + time.ctime(maxtimestamp[0]))
# Retrieves and displays the idle users from the minute_log table 
	c.execute("select uname, terminal, login_time, time_idle from minute_log where time_idle != '.' and timestamp=(select max(timestamp) from minute_log) order by uname");
	data = c.fetchall()

	idle_users = []
	uname_title = 'CURRENT IDLE USERS'

	collected_data = []
 	for row in data:
		new_list = []
   		uname = str(row[0])
   		terminal = str(row[1])
   		login = str(row[2])
   		idle = str(row[3])
   		new_list = [uname,terminal,login,idle]
		' '.join(new_list)
   		collected_data.append(new_list)
	

	print('\n\nCURRENT IDLE USERS\n-------------------')
	print('\nUsername                     Terminal   Login  Idle Time')
	print('--------------------------------------------------------')
	
	
	for row in collected_data:
		pad1 = (30-len(row[0]))*' ' 
		pad2 = (10-len(row[1]))*' '
		pad3 = (7-len(row[2]))*' '
		col1 = [row[0],pad1]
		col1 = ''.join(col1)
		col2 = [row[1],pad2]
		col2 = ''.join(col2)
		col3 = [row[2],pad3]
		col3 = ''.join(col3)
		total = [col1,col2,col3,row[3]]
		total = ''.join(total)
		print(total)
	print('--------------------------------------------------------\n')


# Displays Summary Statement of all idle users
	c.execute("select count(distinct uname) from minute_log where time_idle != '.' and timestamp=(select max(timestamp)from minute_log)")
	idle_users_result = c.fetchall()
	print ("Total Number of Idle Users: %s" %idle_users_result[0])
	
# Displays Summary Statement of all idle terminals
	c.execute("select count(terminal) from minute_log where time_idle != '.' and timestamp=(select max(timestamp) from minute_log)")
	idle_terminals_result = c.fetchall()
	print ("Total Number of Idle Terminals: %s" %idle_terminals_result[0])
	

	print('\n--------------------------------------------------------')
	return()
