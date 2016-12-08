# This module will determine the current offline users.
# Offline users are determined by taking the list of users and subtracting
# any users listed in the latest minute_log group(logged in users).
# Inputs : none
# Return : none
# Prints : list of offline users

# ** Last Login information is expiremental
# The last login date and time is taken from the minute_log if there is an entry for the current date, else
# it is taken from daily_log, else returns n/a.

# import required libraries
import sqlite3
import datetime
import calendar

def offline_users():
	# Create database connection
	conn = sqlite3.connect("QATWatch.db")
	conn.text_factory = str #this returns output as string instead of unicode with the u
	c = conn.cursor()

	# Get current offline users
	c.execute("select uname from users where uname not in (select uname from minute_log where timestamp = (select max(timestamp) from minute_log))")
	offline_users = c.fetchall()

	# Create empty list for data with uname and last login info
	offline_user_data = []

	# Look for users last login data
	for user in offline_users:
		# First select from minute_log table any users matching the Offline users and retreive the lastest record
		c.execute("select uname, date_last_login, login_time, timestamp from minute_log where uname = ? order by timestamp desc", (user[0],))
		login_time = c.fetchone()

		# If we get a login record from minute table only keep it if it's from the current day
		if login_time :
			# Python date/time is UTC subtract 4 hours to get local time
			# Remove localization for now. Application will be developed using UTC time
			# Possible future enhancement add localization
			now = datetime.datetime.now()# - datetime.timedelta(hours=4)
			local_now = now.strftime('%Y-%m-%d')
			login_record_date = datetime.datetime.fromtimestamp(int(login_time[3])).strftime('%Y-%m-%d')

			if local_now != login_record_date:
				# Record not from current date so change to None to flow to rest of logic
				login_time = None

		# If no data in the minute_log now check the daily_log
		if login_time == None:
			c.execute("select uname, date, login_time, logout_time from daily_log where uname = ? order by id desc ",(user[0],))
			daily_log_time = c.fetchone()
			if daily_log_time == None:
				# no last login info available
				user_item = {'uname':user[0],'last_login_date':'n/a','login_time':'n/a'}
				offline_user_data.append(user_item)
			else:
				# add user info from daily_log
				user_item = {'uname':user[0],'last_login_date':daily_log_time[1],'login_time':daily_log_time[2]}
				offline_user_data.append(user_item)
		else:
			# add user info from minute_log
			# parse date from minut_log to match daily_log format
			my_date_month = int(login_time[1][5:7])
			my_date_day = int(login_time[1][8:])
			my_date_year = int(login_time[1][0:4])

			# convert to Python date format, get weekday name index #
			mydate = datetime.datetime(my_date_year, my_date_month, my_date_day)
			day_number  = mydate.weekday()

			# get abbreviations to match indexes
			new_day =  calendar.day_abbr[day_number]
			new_month = calendar.month_abbr[my_date_month]

			# create new formated date string
			parsed_date = str(new_day) + ' ' + str(new_month) + ' ' + str(my_date_day)

			user_item = {'uname':user[0],'last_login_date':parsed_date,'login_time':login_time[2]}
			offline_user_data.append(user_item)

	############ Print Output ############################
	# format and print output to screen
	header =  "Username                        Last Login   Time"
	header_length = len(header)
	print ("-") * header_length
	print ("Offline Users Report")
	print ("-" *  header_length)
	print (header)
	print ("-" *  header_length)
	#uname_length = 30
	#login_date_length = 10
	#login_time = 5
	#space = 3
	spacer = " " * 2
	for user in offline_user_data:
		# configure spacing for uname
		uname_length = len( user['uname'])
		name_pad = 30 - uname_length
		name_pad = " " * name_pad

		# configure spacing for date
		date_length = len( user['last_login_date'])
		date_pad = 10 - date_length
		date_pad = " " * date_pad


		# configure spacing for time
		time_length = len( user['login_time'])
		time_pad = 5 - time_length
		time_pad = " " * time_pad


		print (user['uname'] + name_pad + spacer + date_pad + user['last_login_date'] + spacer + time_pad +  user['login_time'])

	offline_user_count = len(offline_user_data)
	print ("-" * header_length)
	print ("There are %d users offline" %(offline_user_count))
	print ("-" * header_length)
	print ("")
	######## End Print output  ##############
