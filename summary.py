def summary():

	import os 
	import sqlite3
	import string
	import offline_user_count 

	path_name = '/home/Jennifer.Meggs/QATWatch/Source/QATWatch.db'
	conn = sqlite3.connect(path_name)
	c = conn.cursor()

	query1 = 'select * from minute_log'
	query2 = 'select max(timestamp) from minute_log'
	query3 = 'select count(distinct uname) from users'
	data = c.execute(query1)
	data = data.fetchall()

	time_stamp = c.execute(query2)
	time_stamp = time_stamp.fetchall()
	time_stamp = str(time_stamp)
	
	all_users = c.execute(query3)
	all_users = all_users.fetchall()
	all_users = int(all_users[0][0])

	last_time = []
	for i in time_stamp:
		if str.isdigit(i) == True:
			last_time.append(i)	
	last_time = ''.join(last_time)
	
	idle_check = '.'
	idle_count = 0
	active_count = 0
	for line in data:
		if last_time in str(line[8]):
			if idle_check not in line:
				idle_count += 1
			else:
				active_count += 1


############# PRINT STATEMENT #############
	Table_bars = '='*30
	row_bars = '-'*30
	title_pad = ' ' *12
	title_pad = [title_pad,'-SUMMARY-']
	title_pad = ''.join(title_pad)
	count = offline_user_count.offline_user_count()
	term_count = active_count + idle_count
	user_count = all_users-count  
	print (title_pad)
	print ('Terminal Summary')
	print (Table_bars)
	
	print ('Active Terminals:         %d' %active_count)
	print (' ')
	print ('Idle Terminals:           %d' %idle_count)
	print (row_bars)
	print ('Total Online Terminals:   %d ' %term_count)
	print (Table_bars)
	print (' ')
	print (' ')
	print ('User Summary')
	print (Table_bars)
	print ('Online Users:             %d' %user_count)
	print (' ')
	print ('Offline Users:            %d' %count)
	print (row_bars)
	print ('Total Users:              %d' %all_users)
	print (Table_bars )
	print (' ')
########### END PRINT STATEMENT ###########


	return()
