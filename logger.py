from selenium import webdriver
import time
from datetime import datetime


driver = webdriver.Chrome()
driver.get('http://redmine.mdtc.cienet.com.cn:3000/projects/timesheet/issues')

user_name = 'jeter.lin'
password = '3qqLogan'

user_field = driver.find_element_by_id('username').text
pw_field = driver.find_element_by_id('password').text
