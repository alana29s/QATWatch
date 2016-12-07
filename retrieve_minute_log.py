#Minute_log retrieval document. Written by Christianna Vasquez and Jennifer Meggs
#The purpose of this document is to retrieve data from minute_log and print it on the screen.
#import sqlite3 library
import sqlite3
#connect to the database
conn = sqlite3.connect("/home/Jennifer.Meggs/QATWatch/Source/QATWatch.db")
#cursor
c = conn.cursor()
#connect to the table in the database
c.execute("select * from minute_log")
#fetch complete data
all_data = c.fetchall()
#print complete data
print(all_data)

#This module serves to establish how to retrieve data from our minute_log table using select statements.
#The next step is to build upon this and retrieve data for both the current_active_users client view
#and the idle_users client view. These views will then be displayed in the Main Menu as options 1 & 2.

