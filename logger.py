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
        try:
            driver.get(
                'http://redmine.mdtc.cienet.com.cn:3000/projects/timesheet/issues')
            time.sleep(3)
        except:
            print(
                'Please check your WiFi setting, you need to connect your WiFi to tpeap-11F-GM-5G')
            raise SystemExit()

        try:
            self.un_pw()
        except:
            print('Fail to log in, please check your username and password')
            self.un_pw()

        start_date = input('The first day you want to log: ')

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

        conformation = input('Are you sure (y/n)? ')

        if conformation == 'y':
            self.logging(start_date, duration)

        else:
            print('Goodbye!')

    def un_pw(self):
        username = input('Enter your username: ')
        password = input('and your password: ')

        print('Entering the user info...')

        user_field = driver.find_element_by_id('username')
        user_field.send_keys(username)
        pw_field = driver.find_element_by_id('password')
        pw_field.send_keys(password)
        loggin_but = driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/div[2]/div/form/table/tbody/tr[4]/td[2]/input')
        loggin_but.send_keys(Keys.RETURN)

    def logging(self, start_date, duration):
        for i in range(int(duration)):
            driver.get(
                'http://redmine.mdtc.cienet.com.cn:3000/issues/32609/time_entries/new')
            ed = start_date + dt.timedelta(days=i)
            print('Enter date -> {}'.format(ed))
            driver.find_element_by_id('time_entry_spent_on').clear()
            driver.find_element_by_id('time_entry_spent_on').send_keys(str(ed))

            driver.find_element_by_id('time_entry_hours').send_keys('8')

            driver.find_element_by_id(
                'time_entry_working_city').send_keys('Taipei')

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
