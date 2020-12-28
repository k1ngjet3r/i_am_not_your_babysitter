from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from datetime import datetime

# Open Chrome and go to RedMine
print('Opening the RedMine...')
driver = webdriver.Chrome()
driver.get('http://redmine.mdtc.cienet.com.cn:3000/projects/timesheet/issues')

# Enter Username and password to log into Redmine
print('Entering the user info...')
user_name = 'jeter.lin'
password = '3qqLogan'

user_field = driver.find_element_by_id('username')
user_field.send_keys(user_name)
pw_field = driver.find_element_by_id('password')
pw_field.send_keys(password)
loggin_but = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div/form/table/tbody/tr[4]/td[2]/input')
loggin_but.send_keys(Keys.RETURN)

# Go to the log-time directory

step_1 = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/a[18]')
step_1.send_keys(Keys.RETURN)

step_2 = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/form[2]/div[2]/table/tbody/tr[8]/td[5]/a')
step_2.send_keys(Keys.RETURN)

print("click the Log-time button")
logtime = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div[1]/a[2]')
logtime.send_keys(Keys.RETURN)

# Enter detail
print('Enter Hours -> 8 hours')
hour = driver.find_element_by_id('time_entry_hours')
hour.send_keys('8')

print('Enter Working City -> Taipei')
city = driver.find_element_by_id('time_entry_working_city')
city.send_keys('Taipei')

print('Select the activity -> MY22')
select_activity = Select(driver.find_element_by_id('time_entry_activity_id'))
select_activity.select_by_index(8)

print('Enter date -> 2020-12-14')
driver.find_element_by_id('time_entry_spent_on').clear()
driver.find_element_by_id('time_entry_spent_on').send_keys('2020-12-14')


# print('pressing the Save buttom')
# save_but = driver.find_elements_by_id('commit')
# save_but.send_keys(Keys.RETURN)-