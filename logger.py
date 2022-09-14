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

national_holiday = ['2022-' + day for day in exception['holiday']]
make_up = ['2022-' + day for day in exception['make_up']]

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
            print(
                '!!![ERROR] Fail to open Chrome! Please check the Chromedriver version')
            driver.close()

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
                r'/html/body/div/div[2]/div[1]/div[3]/div[2]/div[1]/form/input[6]')
            loggin_but.send_keys(Keys.RETURN)
        except:
            print('Fail to log in, please check your username and password')

        print('--> Log in to Redmine successfully!')

        if self.username in ['jeter.lin', 'logan.chang']:
            self.ai_team_4_the_win(self.first_date, self.duration, url, driver)
            print(' --> Log time completed!, directing to overview!')
            self.overview(driver, first_name)

        else:
            print('Who the fuck are you?')

    def logging(self, start_date, duration, url, driver):
        start_date = date_validation(start_date)
        for i in range(int(duration)):
            entered_date = start_date + dt.timedelta(days=i)
            self.enter_info(entered_date, duration, url, i, driver)

    def ai_team_4_the_win(self, driver):
        print('''
        ***********************************
        |                                 |
        |<--- Welcome! AI Team Member --->|
        |                                 |
        *********************************** 
        ''')
        current_date = date_validation(self.start_date)
        end_date = date_validation(self.end_date)

        while current_date < end_date + dt.timedelta(days=1):
            if (current_date.weekday() == 5 or current_date.weekday() == 6) and str(entered_date) not in make_up:
                print('{} is weekend, Pass'.format(date))
                print('---------------------------------------')

            # determine the date is national holiday or not
            elif str(date) in national_holiday:
                print('{} is national_holiday, Pass'.format(date))
                print('---------------------------------------')

            else:
                weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
                current_weekday = weekday[current_date.weekday()]

                usr_log_info = name_list[self.username][current_weekday]

                for detail in usr_log_info:
                    type_ = detail['type']
                    model_year = detail['model_year']
                    hour = detail['hour']
                    url = link_list["task"][type_]

                    enter_info(date=current_date, url=url, model_year=model_year, entry_hour=hour, driver=driver)
            
            current_date += dt.timedelta(days=1)

    def enter_info(self, date, url, model_year, entry_hour, driver):
        # go to the logging page
        driver.get(url)

        # Entering the date
        print('Enter date -> {}'.format(date))
        driver.find_element_by_id('time_entry_spent_on').clear()
        driver.find_element_by_id(
            'time_entry_spent_on').send_keys(str(date))

        # Entering the working time
        driver.find_element_by_id('time_entry_hours').send_keys(str(entry_hour))

        # Entering the work type: MY22
        select_activity = Select(driver.find_element_by_id('time_entry_activity_id'))
        if model_year == 'my22':
            select_activity.select_by_index(19)
        elif model_year == 'my23':
            select_activity.select_by_index(13)

        # submit the log
        driver.find_element_by_id(
            'time_entry_spent_on').send_keys(Keys.ENTER)

        # Output the logging progress
        print('complete logging day {}'.format(date))
        print('---------------------------------------')

    def overview(self, driver, first_name):
        driver.get(overview_url)
        time.sleep(3)
        driver.find_element_by_id('firstname').send_keys(first_name)
        select_period = Select(driver.find_element_by_id('period'))
        select_period.select_by_index(1)


if __name__ == '__main__':
    Logger(username='', password='', first_date='', end_date='').start_log_time()
