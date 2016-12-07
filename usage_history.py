def usage_history():
#Importing all the neeeded modules
	import os
	import sqlite3
	import string

# Connecting to the database 
	path_name = '/home/Jennifer.Meggs/QATWatch/Source/QATWatch.db'
	conn = sqlite3.connect(path_name)
	c = conn.cursor()
	fj = os.popen('date --date="1 days ago" | cut -d " " -f1,2,3')
	date = fj.read()
	query = 'select * from daily_log order by uname'
	data  = c.execute(query)
# Initializing an empty list to put sorted data into
# Each value was stored as being as string to make sure they were being utilized as one
	sorted_data = []
	print('This data was collected on:  %s' %date)
	for line in data:
		if date.strip() in line:
			new_list = []
			ID = str(line[0])
			uname = str(line[1])
			terminal = str(line[2])
			login_time = str(line[4])
			logout_time = str(line[5])
			amount_time_logged = str(line[6])
			new_list = [ID,uname,terminal,login_time,logout_time,amount_time_logged]
			' '.join(new_list)
			sorted_data.append(new_list)
	headers = ['Terminal |','Login |','Logout |','Logged']
	headers = '  '.join(headers)
	uname = '@!in@ pasd123 sdf3%$@ !*!^@^*(!@^!@%!#^%#FYAVSYATDES^%%!UIHASG2312364asdassdf62IY%!'
	user_count = 0
# Initializing the total amount of time that was logged during a day
	total_hours = 0
	total_minutes = 0
	hours_tlist = []
	hours_olist = []
	minutes_tlist = []
	minutes_olist = []
	for line in sorted_data:
		user_hours = 0
		user_minutes = 0
# Life could've gone easier with SQL commands
# Essentially writing code for the 'group by' statement that is used in SQL
		if uname not in line[1]:
			uname = line[1]
			user_count += 1
			title = ['      ','******',uname,'******']
			title = ''.join(title)
			breakline = ('-----------------------------------------')
			if len(breakline) > len(title):
				line_pad = ((len(breakline)-len(title))/2)*' '
				title = [line_pad,title,line_pad]
				title = ''.join(title)
				print (title)
				print (breakline)	
				print (headers)
				print (breakline)
			for i in sorted_data:
				ID = str(i[0])
				terminal = str(i[2])
				login_time = str(i[3])
				logout_time =str(i[4])
				amount_time_logged = str(i[5])
				if 'in' in amount_time_logged:
					amount_time_logged = ' --:--'
					hourt = '-'
					houro = '-'
					minutet = '-'
					minuteo = ' '
				if 'logged' in logout_time:
					logout_time = ' --:--'
				hourt =  amount_time_logged[1]
				hourtcheck = str.isdigit(hourt)
				houro = amount_time_logged[2]
				hourocheck = str.isdigit(houro)
				minutet = amount_time_logged[4]
				minutetcheck = str.isdigit(minutet)
				minuteo = amount_time_logged[5]
				minuteocheck = str.isdigit(minuteo)
				if i[1] == uname:
					if hourtcheck == True and hourocheck == True and minutetcheck == True and minuteocheck == True:
						minutes = (int(minutet)*10)+int(minuteo)
						hours = (int(hourt)*10)+int(houro)	
						user_hours += hours
						user_minutes += minutes
						total_hours += user_hours
						total_minutes += user_minutes
					else:
						user_hours += 0
						user_minutes += 0
					if len(login_time) < len('Login |'):
						pad = (len('Login |')-len(login_time))*' '
						pad_login = [login_time,pad]
						pad_login = ''.join(pad_login)
					else:
						pad_ID = ID
					if len(terminal) < len('Terminal |'):
						pad = (len('Terminal |')-len(terminal))*' ' 
						pad_term = [terminal,pad]
						pad_term = ''.join(pad_term)
					else:
						pad_term = terminal
					if len(logout_time) < len('Logout |'):
						pad = (len('Logout |')-len(logout_time))*' '
						pad_out = [logout_time,pad]
						pad_out = ''.join(pad_out)
					hours_tlist.append(str(hourt))
					hours_olist.append(str(houro))
					minutes_tlist.append(str(minutet))
					minutes_olist.append(str(minuteo))
					amount_time_logged = [hourt,houro,'h',' ',minutet,minuteo,'m']
					amount_time_logged = ''.join(amount_time_logged)
					temp_list = [pad_term,pad_login,pad_out,amount_time_logged]
					temp_list = '  '.join(temp_list)	
					print(temp_list)
				h = 0
				while user_minutes > 60:
					user_minutes -= 60
					h += 1
					user_hours = user_hours + h
	
			print (' ')
			print ('-----------------------------------------')
			print ("Total User Login Time: %dh %dm" %(user_hours,user_minutes))	
			print (' ')
			print (' ')
	sum_of_hourst = []
	for i in hours_tlist:
		if str.isdigit(i) == True:
			sum_of_hourst.append(int(i))
			
	sum_of_hourso = []
	for i in hours_olist:
		if str.isdigit(i) == True:
			sum_of_hourso.append(int(i))
		
	sum_minutest = []
	for i in minutes_tlist:
		if str.isdigit(i) == True:
			sum_minutest.append(int(i))
	
	sum_minuteso = []
	for i in minutes_olist:
		if str.isdigit(i) == True:
			sum_minuteso.append(int(i))
	
	
	sum_ht = sum(sum_of_hourst)
	sum_ho = sum(sum_of_hourso)
	sum_mt = sum(sum_minutest)
	sum_mo = sum(sum_minuteso)
		

	total_hours = (sum_ht*10) + sum_ho
	total_minutes = (sum_mt*10) + sum_mo
	totes = 0
	while total_minutes > 60:
		totes += 1
		total_minutes -= 60
	
	total_hours = totes + total_hours
	
	
	avg = ((total_hours*60)+total_minutes)/user_count
	avg_h = 0
	while avg > 60:
		avg -= 60
		avg_h += 1
	print ('=========================================')
	print ('Total Time Logged In:           %dh %dm' %(total_hours,total_minutes))
	print ('Average Time Logged per User:   %dh %dm' %(avg_h,avg))
	print ('Total Distinct Users:           %d' %user_count)
	print (' ')
	print (' ')
	total_time = [total_hours,total_minutes]


	return(total_time)


