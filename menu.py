#This is a menu for our tables. Made by Christianna Vasquez

#import libraries
import os
import sys
sys.path.append('home/Jennifer.Meggs/QATWatch/Source')
#import QATWatch Group created modules:
import offline_users
import usage_history
import summary
import current_active_terminals
import current_idle_information
import help_option
import users_by_hour

#Define functions:

#Create clearscreen function, for use in transitions.
def clearScreen():
	os.system('clear');
clearScreen()

#<<MENU>>

choice = None
while choice != 8 or choice == 42:
	print("\n QATS Terminal Monitoring System \n--------------------------------- \n")
	print("1. Current Active Users")
	print("2. Idle Users")
	print("3. Offline Users")
	print("4. Usage History")
	print("5. Graph")
	print("6. Summary Data")
	print("7. Help")
	print("8. Exit \n\n---------------------------------\n")

	#Limits inputs to numerical values
	while True:
		try:
			choice = int(raw_input("Select an Option: "))
		except ValueError:
			print("Input must be numeric, please reenter: ")
			continue
		else:
			break

	if choice == 1:
		clearScreen()
		current_active_terminals.current_active_users()
		raw_input("PRESS ENTER TO CONTINUE")
		clearScreen()
	elif choice == 2:
		clearScreen()
		current_idle_information.idle_users()
		raw_input("PRESS ENTER TO CONTINUE")
		clearScreen()
	elif choice == 3:
		clearScreen()
		offline_users.offline_users()
		raw_input("PRESS ENTER TO CONTINUE")
		clearScreen()
	elif choice == 4:
		clearScreen()
		usage_history.usage_history()
		raw_input("PRESS ENTER TO CONTINUE")
		clearScreen()
	elif choice == 6:
		clearScreen()
		summary.summary()
		raw_input("PRESS ENTER TO CONTINUE")
		clearScreen()
	elif choice == 7:
		clearScreen()
		help_option.help_option()
		raw_input("PRESS ENTER TO CONTINUE")
		clearScreen()
	elif choice == 5:
		clearScreen()
		users_by_hour.hourly_users()
		raw_input("PRESS ENTER TO CONTINUE")
		clearScreen()
	elif choice == 8:
		break
	elif choice == 42:
		clearScreen()
		print("DON'T PANIC!")
		print("But...")
		print("DON'T FORGET... WE ARE ALWAYS WATCHING YOU!")
		print(' ')
		print(' \   /\  ')
		print("  ) ( ') ")
		print('  ( /  ) ')
		print('  \(__)| ')
		print(' ')
		raw_input("PRESS ENTER TO CONTINUE")
		clearScreen()
	else:
		clearScreen()
		print("Error, please input value between 1 and 7.")
		raw_input("PRESS ENTER TO CONTINUE")
		clearScreen()
clearScreen()
print("Thank you for using QATWatch!\n")
