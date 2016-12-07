#who command import code - written by Jennifer Meggs & Christianna Vasquez
#imports who command then splits the array into a list of lists
#import os python library
import os
#uses function 'popen' to pull user information from linux into python
#use .read method to read the output as a string statement
process = os.popen("who -u | tr -s ' '").read()
#timestamp entry
timestamp = os.popen("date +%s").read()
#create an empty list for user data
who_list = []
#split the data into lists
process = process.splitlines()
#split the rows into individual fields:
for row in process:
	new_row = row.split(" ")
	who_list.append(new_row)


#import SQLite3 module
import sqlite3
#connect to our QATWatch database
conn = sqlite3.connect("/home/Jennifer.Meggs/QATWatch/Source/QATWatch.db")
#activates cursor to traverse sqlite 3 database
c = conn.cursor()
#insert data into minute log
for row in who_list:
	uname = row[0]
	terminal = row[1]
	date_last_login = row[2]
	login_time = row[3]
	time_idle = row[4]
	pid = row[5]
	ip_address = row[6]
	c.execute("insert into minute_log values(?,?,?,?,?,?,?,?,?)",(None, uname, terminal, date_last_login, login_time, time_idle, pid, ip_address, timestamp))
conn.commit()
#this module is associated with a cronjob function to run once a minute on a continual basis
