from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import datetime as dt


class Logger:
    def __init__(self, username, password, start_date, duration):
        self.username = str(username)
        self.password = str(password)
        self.start_date = str(start_date)
        self.duration = int(duration)

    def date_formater(self):
        try:
            s = self.start_date
            return dt.date(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
        except:
            print('please enter a valid date or correct date format ')
        
    def connection(self):
        try:
            driver = webdriver.Chrome()
            driver.get(
                'http://redmine.mdtc.cienet.com.cn:3000/projects/timesheet/issues')
        except:
            print('Please check your WiFi setting, you need to connect your WiFi to tpeap-11F-GM-5G')

    def logging(self):
        sd = self.date_formater()
        print('date format checked')

        # Open Chrome and go to RedMine
        print('Opening the RedMine via Chrome...')
        driver = webdriver.Chrome()
        driver.get(
            'http://redmine.mdtc.cienet.com.cn:3000/projects/timesheet/issues')

        # Enter Username and password to log into Redmine
        print('Entering the user info...')
        user_field = driver.find_element_by_id('username')
        user_field.send_keys(self.username)
        pw_field = driver.find_element_by_id('password')
        pw_field.send_keys(self.password)
        loggin_but = driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/div[2]/div/form/table/tbody/tr[4]/td[2]/input')
        loggin_but.send_keys(Keys.RETURN)

        # Go to the log-time directory
        print('heading to the directory...')
        step_1 = driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/div[1]/a[18]')
        step_1.send_keys(Keys.RETURN)

        step_2 = driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/div[2]/form[2]/div[2]/table/tbody/tr[8]/td[5]/a')
        step_2.send_keys(Keys.RETURN)

        print("click the Log-time button")
        logtime = driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/div[2]/div[1]/a[2]')
        logtime.send_keys(Keys.RETURN)

        # Enter detail
        print('Enter Hours -> 8 hours')
        hour = driver.find_element_by_id('time_entry_hours')
        hour.send_keys('8')

        print('Enter Working City -> Taipei')
        city = driver.find_element_by_id('time_entry_working_city')
        city.send_keys('Taipei')

        print('Select the activity -> MY22')
        select_activity = Select(
            driver.find_element_by_id('time_entry_activity_id'))
        select_activity.select_by_index(8)

        for i in range(self.duration):
            sd = sd + dt.timedelta(days=i)
            print('Enter date -> {}'.format(sd))
            driver.find_element_by_id('time_entry_spent_on').clear()
            driver.find_element_by_id('time_entry_spent_on').send_keys(str(sd))

            save_but = driver.find_elements_by_xpath('/html/body/div/div/div[3]/div[2]/form/input[2]')
            save_but.send_keys(Keys.RETURN)


log = Logger('jeter.lin', '3qqLogan', '20201214', 5)
log.logging()