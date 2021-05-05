### !!!USE WITH CAUTION!!!
Use with your own risk! I won't stop you from logging the entired 2021 but I also won't be responsible if something went wrong.

# What the hell is redmine_auto_logger?
Sick of logging work time on RedMine day by day using your finger? Introducing RedMine_auto_logger, a program that help you log your time automatically. All you need to do is to enter your username, password, start date, and duration, the logger will help you log your time without tedious BS.

# Environment setup
In order to make this work, there are some requirements that need be install on your computer:
1. Python 3.6+
2. Chromedriver
3. Selenium module (pip install selenium)
4. Pillow module (pip install pillow)

FYI: you need to install the Chromedriver to your installed python directory which is: C:\Users\<your name>\AppData\Local\Programs\Python\<Python version>\

# How this work?
This program used selenium to control web browser (In this case Chrome) to help you log your time.

# How to install requirement?
If this is the first time you run this program on this computer, you will need to install all requirments. Fortunately, you don'y have to haunt the modules individually, all you need to do is to execute "requriememt_installer.bat" and it will help you not only the required modules but also the chromedriver.

# How to use?
When you run the script in terminal, a new window will open and terminal will ask you to enter your username and password. After you entered it, the program will login to RedMine and then it will ask you what is the first day you want to log?, how many days you want to log? It will ask for the confirmation. If confirmed, it then start the log time process.

# Version History
## Version 4.0
Introduce GUI for easily entering username, password, start date, and duration.

## Version 3.0
Store usernames and national holidays in the form of JSON files separately. Now it can also differentiate the leader and non-leader by usernames stored in the JSON file. It's also possible for MY-23 team members to log time using this file, but at current stage it still need to add the url for logging time, this function should be added by version 3.1.

## Version 2.0
Want to log the rest of 2021 at once? Now you can do that since it can now differentiate not only weekend, but national holiday and make-up days. Just use it at your own risk!

## Version 1.1
You can log time more than 5 days, the program can now differentiate weekday or weekend so that is can avoid log time in weekend.
Also, it can now differentiate leader and non-leader.


