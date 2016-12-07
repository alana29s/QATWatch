# This module collects all people users from the /etc/passwd file and
# inserts them into the users table in the database
# This module should have an associated cron job that runs it periodically
# created by Alana Martin 2016-10-26

# import required libraries
import os
import sqlite3

def get_linux_users():
	# This function takes no arguments and returns a list of people users

	# Get list of users and user ID from the passwd file
	all_users = os.popen('cat /etc/passwd | cut -d ":" -f 1,3').read()

	# Split large string file into rows
	all_users = all_users.splitlines()

	# Create empty list for all people users
	all_people_users = []

	# Separate each row by the delimiter and add only people and non-disabled users
	for row in all_users:
		new_row  = row.split(':')
		# a first character of # indicates a disabled user
		user_check = new_row[0][0]
		user_id = int(new_row[1])
		if user_check != "#" and user_id >= 1000:
			# Item passed validation now add to the array
			all_people_users.append(new_row[0])
	return all_people_users

def add_users(users):
	# This functions takes 1 input, a list containing user names.
	# All existing user names are delete from the table.
	# All user names from the argument user are inserted into the table.
	
	# Create database connection
	conn = sqlite3.connect("/home/Jennifer.Meggs/QATWatch/Source/QATWatch.db")
	c = conn.cursor()

	# TODO: Question about referential inegrity?
	# if users existed in the past but no longer does what will happen? How to handle orphans?


	# First clear table of old users
	conn.execute("delete from users")

	# Insert users into table
	for user in users:
		c.execute("insert into users values(?)",(user,))
	conn.commit()

linux_users = get_linux_users()
add_users(linux_users)
