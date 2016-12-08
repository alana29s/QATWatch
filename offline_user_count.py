# This module will determine the current count offline users.
# Offline users are determined by taking the list of users and subtracting
# any users listed in the latest minute_log group(logged in users).
# Inputs : none
# Return : count of offline users

# import required libraries
import sqlite3

def offline_user_count():
	# Create database connection
	conn = sqlite3.connect("QATWatch.db")
	conn.text_factory = str #this returns output as string instead of unicode with the u
	c = conn.cursor()

	# Get current offline users
	c.execute("select uname from users where uname not in (select uname from minute_log where timestamp = (select max(timestamp) from minute_log))")
	offline_users = c.fetchall()

	count_of_offline_users = len(offline_users)
	return count_of_offline_users
