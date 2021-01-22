from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import datetime as dt

driver = webdriver.Chrome()


class Logger:
    def __init__(self):
        pass

    def date_validation(self, first_date):
        y = int(first_date[:4])
        m = int(first_date[4:6])
        d = int(first_date[6:])
        return dt.date(year=y, month=m, day=d)

    def enter(self):
        # Open the Redmine using Chrome
        try:
            driver.get(
                'http://redmine.mdtc.cienet.com.cn:3000/projects/timesheet/issues')
            time.sleep(3)

        # If the wifi connection is wrong, raise the error message
        except:
            print("I'm offline so I can't do that!, Please check your WiFi setting!")
            raise SystemExit()

        # For enter the username and password in terminal
        username, password, url = self.un_pw()
        try:
            print('Entering the user info...')
            user_field = driver.find_element_by_id('username')
            user_field.send_keys(username)
            pw_field = driver.find_element_by_id('password')
            pw_field.send_keys(password)
            loggin_but = driver.find_element_by_xpath(
                '/html/body/div/div/div[3]/div[2]/div/form/table/tbody/tr[4]/td[2]/input')
            loggin_but.send_keys(Keys.RETURN)
        except:
            print('Fail to log in, please check your username and password')
            self.un_pw()

        start_date = input(
            'The first day you want to log (format: 20201019): ')

        # Checking the entered date format
        try:
            self.date_validation(start_date)
        except:
            print('please enter the valid date')
            start_date = input('please intput the correct date: ')
            self.date_validation(start_date)

        duration = input('How many days you want to log? ')

        start_date = self.date_validation(start_date)

        end_date = start_date + dt.timedelta(days=int(duration)-1)

        print("So you want to log {} days started from {} to {}?".format(
            duration, start_date, end_date))

        # Asking the conformation
        conformation = input('Are you sure (y/n)? ')

        if conformation == 'y':
            self.logging(start_date, duration, url)

        else:
            print('Goodbye!')

    def un_pw(self):
        url = ''
        username = input('Enter your username: ')
        password = input('and your password: ')

        if username == 'maggie.chang':
            url = 'http://redmine.mdtc.cienet.com.cn:3000/issues/32612/time_entries/new'
        else:
            url = 'http://redmine.mdtc.cienet.com.cn:3000/issues/32609/time_entries/new'

        return username, password, url


    def logging(self, start_date, duration, url):
        for i in range(int(duration)):
            driver.get(url)

            # Entering the date
            ed = start_date + dt.timedelta(days=i)

            if ed.weekday() == 5 or ed.weekday() == 6:
                print('{} is weekend, Pass'.format(ed))
                print('---------------------------------------')

            else:
                print('Enter date -> {}'.format(ed))
                driver.find_element_by_id('time_entry_spent_on').clear()
                driver.find_element_by_id(
                    'time_entry_spent_on').send_keys(str(ed))

                # Entering the working time: 8 hours
                driver.find_element_by_id('time_entry_hours').send_keys('8')

                # Entering the work location: Taipei
                driver.find_element_by_id(
                    'time_entry_working_city').send_keys('Taipei')

                # Entering the work type: MY22
                select_activity = Select(
                    driver.find_element_by_id('time_entry_activity_id'))
                select_activity.select_by_index(8)

                driver.find_element_by_id(
                    'time_entry_spent_on').send_keys(Keys.ENTER)

                print('complete logging day {}/{}'.format(i+1, duration))
                print('---------------------------------------')

        print('Log time completed.')


log = Logger()
log.enter()
