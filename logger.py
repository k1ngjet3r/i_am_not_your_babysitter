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
from func.chromedriver_updater import update_chromedriver

def read_json(json_dir):
    with open(json_dir) as f:
        return json.load(f)


try:
    name_list = read_json('json/names.json')
    exception_ = read_json('json/national_holiday.json')
    link_list = read_json('json/links.json')

except FileNotFoundError:
    name_list = read_json(r'json\names.json')
    exception_ = read_json(r'json\national_holiday.json')
    link_list = read_json(r'json\links.json')

national_holiday = ['2022-' + day for day in exception_['holiday']]
make_up = ['2022-' + day for day in exception_['make_up']]

login_url = link_list['page']['login']
overview_url = link_list['page']['overview']


class Logger:
    def __init__(self, username, password, first_date, end_date):
        self.username = username
        self.password = password
        self.first_date = first_date
        self.end_date = end_date

    def start_log_time(self):
        # tell python to open Chrome
        driver = webdriver.Chrome()

        # Open the Redmine using Chrome
        try:
            print('-> Directing to Redmine login page')
            driver.get(login_url)

        except:
            print('Fail to open Chrome! Updating the Chromedriver')
            update_chromedriver()

        # For enter the username and password in terminal
        print('-> Entering username and password')
        first_name = self.username.split('.')[0]

        try:
            print('-> Entering the user info...')
            user_field = driver.find_element_by_id('username')
            user_field.send_keys(self.username)
            pw_field = driver.find_element_by_id('password')
            pw_field.send_keys(self.password)
            loggin_but = driver.find_element_by_xpath(
                r'/html/body/div/div[2]/div[1]/div[3]/div[2]/div[1]/form/input[5]')
            loggin_but.send_keys(Keys.RETURN)
        except:
            print('Fail to log in, please check your username and password')
            driver.close()

        print('--> Log in to Redmine successfully!')

        if self.username in ['jeter.lin', 'logan.chang']:
            self.ai_team_4_the_win(driver)
            print(' --> Log time completed!, directing to overview!')
            self.overview(driver, first_name)

        else:
            print('Who the fuck are you?')


    def ai_team_4_the_win(self, driver):
        print('''
        ***********************************
        |                                 |
        |<--- Welcome! AI Team Member --->|
        |                                 |
        *********************************** 
        ''')
        current_date = date_validation(self.first_date)
        end_date = date_validation(self.end_date)

        while current_date < end_date + dt.timedelta(days=1):
            if (current_date.weekday() == 5 or current_date.weekday() == 6) and str(current_date) not in make_up:
                print('{} is weekend, Pass'.format(current_date))
                print('---------------------------------------')

            # determine the date is national holiday or not
            elif str(current_date) in national_holiday:
                print('{} is national_holiday, Pass'.format(current_date))
                print('---------------------------------------')

            else:
                weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
                current_weekday = weekday[current_date.weekday()]

                usr_log_info = name_list[self.username][current_weekday]

                for detail in usr_log_info:
                    type_ = detail['type']
                    model_year = detail['model_year']
                    hour = detail['hour']
                    

                    self.enter_info(date=current_date, type_=type_, model_year=model_year, entry_hour=hour, driver=driver)
            
            current_date += dt.timedelta(days=1)

    def enter_info(self, date, type_, model_year, entry_hour, driver):
        # go to the logging page
        url = link_list["task"][type_]
        driver.get(url)

        year, month, day = str(date).split('-')
        entered_date = month + day + year

        # Entering the date
        print('Enter date -> {}'.format(date))
        print(f'Type: {type_}')
        print(f'Model: {model_year}')
        print(f'Entry Hour: {entry_hour}')
        driver.find_element_by_id('time_entry_spent_on').clear()
        driver.find_element_by_id(
            'time_entry_spent_on').send_keys(entered_date)

        # Entering the working time
        driver.find_element_by_id('time_entry_hours').send_keys(str(entry_hour))

        # Entering the work type: MY22
        select_activity = Select(driver.find_element_by_id('time_entry_activity_id'))
        if model_year == 'my22':
            select_activity.select_by_value('19')
        elif model_year == 'my23':
            select_activity.select_by_value('13')

        # submit the log
        driver.find_element_by_id(
            'time_entry_spent_on').send_keys(Keys.ENTER)

        # Output the logging progress
        print('complete logging day {}'.format(date))
        print('---------------------------------------')

    def overview(self, driver, first_name):
        driver.get(overview_url)


if __name__ == '__main__':
    Logger(username='', password='', first_date='', end_date='').start_log_time()
