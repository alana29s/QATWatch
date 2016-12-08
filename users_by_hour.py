# This module will display a bar like graph of distinct users by hour
# Inputs : none
# Return : none
# Prints : A bar graph of users by hour

# import required libraries
import sqlite3
import os


os.system("clear")

def hourly_users():
	# Create database connection
	conn = sqlite3.connect("QATWatch.db")
	conn.text_factory = str #this returns output as string instead of unicode with the u
	c = conn.cursor()

	# Get Request date
	print "User Count by hour"
	print "Please select a date to display."
	request_date = raw_input ("Enter date to display in the format YYYY-MM-DD: ")
	os.system("clear")

	# Get users from a select date and get time with the hour in separate field as 24 hour time
	c.execute("select uname, strftime('%H',(datetime(timestamp,'unixepoch')))from minute_log where date(datetime(timestamp, 'unixepoch')) = date (?) ",(request_date,))
	users_by_hour = c.fetchall()

	#initialize dictionaries with 0-23 as the key
	hours = {}
	count_by_hour = {}
	for x in range(24):
		#initalize empty key for each hour with an empty list
		hours[x] = []
		#intialize empty key for each hour for count
		count_by_hour[x] = 0

	#add users per hour
	for user in users_by_hour:
		hour_num = int(user[1])
		if user[0] not in hours[hour_num]:
			# for each hour add uname only once if it was logged on in that hour
			hours[hour_num].append(user[0])

	for item in range (24):
		# get the count for each hour and add to dictionary
		hour_count = len(hours[item])
		count_by_hour[item] = hour_count

	# find max user count to set starting point for bar graph
	max_user_count = 0
	for key in count_by_hour:
		if count_by_hour[key] > max_user_count:
			max_user_count = count_by_hour[key]

	# print bar graph
	print "          Online User Count by hour"
	for line in range(max_user_count, 0, -1):
		user_count = line
		if user_count < 10:
			user_count = " " + str(user_count)
		print user_count,
		for hour in count_by_hour:
			if count_by_hour[hour] >= line:
				print chr(128),
			else:
				print " ",
		print "\r"

	print "----------------------------------------------------"
	print "   8pm     12am            8am     12pm          6pm"
	print "----------------------------------------------------"
	print " Y axis = User Count"
	print ""
