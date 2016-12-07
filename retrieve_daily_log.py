# Importing the needed modules to collect/store Data
import os
import sqlite3
import sys

# Running Linux Commands to get needed Data
## Running the 'date' command to use to filter out data that isnt in present day
fj = os.popen("date --date='yesterday' | tr -s ' ' | cut -d ' ' -f1,2,3")
date = fj.read()

## Last command to get user login activity
fi = os.popen("last -w | tr -s ' ' | cut -d ' ' -f1,2,4,5,6,7,9,10 | grep -Ev 'boot|reboot|wtmp'")
data = fi.readlines()

# Initialization of a list of the Data for just the present day
usable_data = []

# Filtering out data that is for the day of logging
for line in data:
        if date.strip() in line:
                usable_data.append(line)

# Setting up a connection to database so that data can be easily input in a table
path_name = "/home/Jennifer.Meggs/QATWatch/Source/QATWatch.db"
conn = sqlite3.connect(path_name)
c = conn.cursor()

# For loop to iterate through the rows  and make it easy to import the data of 
# of each line into a database cleanly

for line in usable_data:
    uname = line.split(' ')[0]
    terminal = line.split(' ')[1]
    login_time = line.split(' ')[5]
    logout_time = line.split(' ')[6]

# Getting the information related to date into 1 joined string
    date1 = line.split(' ')[2]
    date2 = line.split(' ')[3]
    date3 = line.split(' ')[4]
    date = [date1,date2,date3]	
    date = ' '.join(date)
    time_logged = line.split(' ')[7]	

# Initiallizing an empty list to store the 'time_logged' column without 
# the line operator of \n at the end, which would other wise be displayed
# in the final data
    time = []
    count = 0

# For loop to scan when '\n' happens within the 'time_logged' and to ignore it
# appending to the initiallized empty list and then joining the list at the end.
#(the counter is just so that the first if statement is doing something
# for some reason the 'continue' command wasn't working for me in this version
# of python, and this is basically here for learning purposes. It can function
# just as well without the if/elif but it is easier to vizualize this way)

    for i in time_logged:
        if i == '\n':
            count += 1
        elif i != '\n':
            time.append(i)
        time_logged = ''.join(time)

# Inserting all collected data in one row and inputing it into the table
#'daily_log' quickly
    c.execute("insert into daily_log(uname,terminal,date,login_time,logout_time,time_logged) values (?,?,?,?,?,?)",(str(uname),str(terminal),str(date),str(login_time),str(logout_time),str(time_logged)))
    conn.commit()
 
