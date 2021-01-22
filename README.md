# What the hell is redmine_auto_logger?
Sick of logging work time on RedMine day by day using your finger? Introducing RedMine_auto_logger, a program that help you log your time automatically. All you need to do is to enter your username, password, start date, and duration, the logger will help you log your time without tedious BS.

# Environment setup
In order to make this work, there are some requirements that need be install on your computer:
1. Python 3.6+
2. Selenium module (pip install selenium)
3. Chromedriver

FYI: you need to install the Chromedriver to your installed python directory which is: C:\Users\<your name>\AppData\Local\Programs\Python\<Python version>\

# How this work?
This program used selenium to control web browser (In this case Chrome) to help you log your time.

# How to use?
When you run the script in terminal, a new window will open and terminal will ask you to enter your username and password. After you entered it, the program will login to RedMine and then it will ask you what is the first day you want to log?, how many days you want to log? It will ask for the confirmation. If confirmed, it then start the log time process.

## For version 1.1
You can log time more than 5 days, the program can now differentiate weekday or weekend so that is can avoid log time in weekend.
Also, it can now differentiate leader and non-leader.

### !!!Caution
It can only differentiate weekend, it cannot aviod national holidays. USE WITH CAUTION!


