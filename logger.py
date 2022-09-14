from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import datetime as dt
import json
import tkinter as tk
from func.connect_to_GM5G import Connect_to_GM5G
from func.date_format_validation import date_validation

def list_of_name():
    with open('json\\name.json', 'r') as f:
        name_list = json.load(f)
    return name_list


def exception_list():
    with open('json\\national_holiday.json', 'r') as w:
        exception = json.load(w)

    national_holiday = ['2022-' + day for day in exception['holiday']]
    make_up = ['2022-' + day for day in exception['make_up']]

    return national_holiday, make_up


class Logger:
    def __init__(self, username, password, first_date, duration):
        self.username = username
        self.password = password
        self.first_date = first_date
        self.duration = duration


    def start_log_time(self):
        # tell python to open Chrome
        driver = webdriver.Chrome()

        # Open the Redmine using Chrome
        try:
            print('-> Directing to Redmine login page')
            driver.get(r'https://redmine.mdtc.cienet.com.cn/login?back_url=http%3A%2F%2F127.0.0.1%3A3000%2F')

        except:
            print('!!! [ERR] Fail to open Chrome !!!')
            driver.close()

        # For enter the username and password in terminal
        print('-> Entering username and password')
        username, password, url = self.un_pw()
        first_name = username.split('.')[0]

        try:
            print('-> Entering the user info...')
            user_field = driver.find_element_by_id('username')
            user_field.send_keys(username)
            pw_field = driver.find_element_by_id('password')
            pw_field.send_keys(password)
            loggin_but = driver.find_element_by_xpath(
                r'/html/body/div/div[2]/div[1]/div[3]/div[2]/div[1]/form/input[6]')
            loggin_but.send_keys(Keys.RETURN)
        except:
            print('Fail to log in, please check your username and password')
            self.un_pw()

        print('--> Log in to Redmine successfully!')

        if self.username == 'jeter.lin' or self.username == 'logan.chang':
            self.ai_team_4_the_win(self.first_date, self.duration, url, driver)
            print('Log time completed!, directing to overview!')
            self.overview(driver, first_name)
        
        else:
            print('Who the fuck are you?')


    def un_pw(self):
        url = ''
        username = self.username
        password = self.password

        if username == 'jeter.lin':
            url_maintenance = r'http://redmine.mdtc.cienet.com.cn:3000/issues/32587/time_entries/new'
            url_creation = r'http://redmine.mdtc.cienet.com.cn:3000/issues/32586/time_entries/new'
            url_leader = r'http://redmine.mdtc.cienet.com.cn:3000/issues/32590/time_entries/new'
            url = [url_creation, url_maintenance, url_leader]

        elif username == 'logan.chang':
            url_maintenance = r'http://redmine.mdtc.cienet.com.cn:3000/issues/32587/time_entries/new'
            url_creation = r'http://redmine.mdtc.cienet.com.cn:3000/issues/32586/time_entries/new'
            url_lab_maintenance = r'http://redmine.mdtc.cienet.com.cn:3000/issues/32584/time_entries/new'
            url = [url_creation, url_maintenance, url_lab_maintenance]

        return username, password, url


    def logging(self, start_date, duration, url, driver):
        start_date = date_validation(start_date)
        for i in range(int(duration)):
            entered_date = start_date + dt.timedelta(days=i)
            self.enter_info(entered_date, duration, url, i, driver)


    def ai_team_4_the_win(self, start_date, duration, urls, driver):
        print('''
        ***********************************
        |                                 |
        |<--- Welcome! AI Team Member --->|
        |                                 |
        *********************************** 
        ''')
        start_date = date_validation(start_date)
        for i in range(int(duration)):
            entered_date = start_date + dt.timedelta(days=i)
            if entered_date.weekday() == 0 or entered_date.weekday() == 1:
                self.enter_info(entered_date, duration, urls[0], i, driver)
            elif entered_date.weekday() == 2 or entered_date.weekday() == 3:
                self.enter_info(entered_date, duration, urls[1], i, driver)
            else:
                self.enter_info(entered_date, duration, urls[2], i, driver)


    def enter_info(self, date, duration, url, day_i, driver):
        # go to the logging page
        driver.get(url)

        # get the lists of exception
        national_holiday, make_up = exception_list()

        # determine the date is weekend and not a make up day
        if (date.weekday() == 5 or date.weekday() == 6) and str(date) not in make_up:
            print('{} is weekend, Pass'.format(date))
            print('---------------------------------------')

        # determine the date is national holiday or not
        elif str(date) in national_holiday:
            print('{} is national_holiday, Pass'.format(date))
            print('---------------------------------------')

        # determine if the date is weekday or make up day
        # if so, log the day
        else:
            print('Enter date -> {}'.format(date))
            driver.find_element_by_id('time_entry_spent_on').clear()
            driver.find_element_by_id(
                'time_entry_spent_on').send_keys(str(date))

            # Entering the working time: 8 hours
            driver.find_element_by_id('time_entry_hours').send_keys('8')

            # Entering the work location: Taipei
            driver.find_element_by_id(
                'time_entry_working_city').send_keys('Taipei')

            # Entering the work type: MY22
            select_activity = Select(
                driver.find_element_by_id('time_entry_activity_id'))
            select_activity.select_by_index(8)

            # submit the log
            driver.find_element_by_id(
                'time_entry_spent_on').send_keys(Keys.ENTER)

            # Output the logging progress
            print('complete logging day {}/{}'.format(day_i + 1, duration))
            print('---------------------------------------')


    def overview(self, driver, first_name):
        driver.get(
                'http://redmine.mdtc.cienet.com.cn:3000/projects/timesheet/time_entries')
        time.sleep(3)
        driver.find_element_by_id('firstname').send_keys(first_name)
        select_period = Select(driver.find_element_by_id('period'))
        select_period.select_by_index(1)


if __name__ == '__main__':
    Logger('jeter.lin', 'sD4T1pDTZp', '20220912', '2').start_log_time()