# QATWatch
## Terminal Monitoring System

This program was written for the Akamai Technical Academy in October 2016.

### About
The QATWatch Terminal Monitoring System is an app written to run in a Linux Console. QATWatch gathers information about Linux users periodically through the use of Cron jobs and adds that information to a database. QATWatch has a menu system that is used to select reports about the Linux Users to be displayed on screen.

### Technology Stack
* GNU/Linux
* SQLite3
* Python

### Report Options
* Current Active Users
* Idle Users
* Offline Users
* Usage History
* Graph
* Summary Report
* Help

### Installation
This program was created as a group project to run in a specific environment. To run this locally several changes will have to be made.

1. Download Repository
2. Create CRON Jobs
3. Create QATWatch db using SQLlite3
4. Change all absolute file paths to relative paths
5. run menu.py from the command line

### Future Enhancements
* Refactor code for efficiency
* Add time localization
* Add messaging capability
* Add kill user process(pid) capability
* Create application on web GUI
* Search functions
    * Name
    * Date
* Add more error handling and logs


### Written by
* David Avila
* Cassie Jeon
* Takara Larsen
* Alana Martin
* Jennifer Meggs
* Christianna Vasquez
