from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import datetime as dt
import json
import tkinter as tk
# from PIL import ImageTk, Image


with open('name.json', 'r') as f:
    name_list = json.load(f)

with open('national_holiday.json', 'r') as w:
    exception = json.load(w)

national_holiday = ['2021-' + day for day in exception['holiday_2021']]
make_up = ['2021-' + day for day in exception['make_up']]

def date_validation(first_date):
    # if date format is 20210101
    if len(first_date) == 8:
        y = int(first_date[:4])
        m = int(first_date[4:6])
        d = int(first_date[6:])
    # if data format is something like 2021-01-01 or 2021.01.01 or 2021/01/01
    elif len(first_date) == 10:
        y = int(first_date[:4])
        m = int(first_date[5:7])
        d = int(first_date[-2:])
    return dt.date(year=y, month=m, day=d)


def username_password():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    username = username_entry.get()
    password = password_entry.get()
    first_date = first_date_entry.get()
    duration = duration_entry.get()
    if username == '':
        check['text'] = 'Please enter your username'
    elif password == '':
        check['text'] = 'Where is your password'
    elif first_date == '':
        check['text'] = 'Enter the first day you want to log motherfucker'
    elif duration == '':
        check['text'] = 'Are you kidding me?'
    else:
        confirmation_window = tk.Tk()
        confirmation_window.title('Confirmation')

        confirmation_msg = tk.Label(master=confirmation_window)

        start_date = date_validation(first_date)
        end_date = start_date + dt.timedelta(days=int(duration)-1)

        confirmation_msg['text'] = "So you want to log {} days started from {} to {}?".format(
            duration, start_date, end_date)

        confirm_btm = tk.Button(
                        master=confirmation_window,
                        text="Yes, bring it on",
                        command = Logger(username, password, start_date, duration).enter())
        
        cancel_btm = tk.Button(
                        master=confirmation_window,
                        text="No, I want my mommy")
        
        confirmation_msg.grid(row=0, column=0)
        confirm_btm.grid(row=1, column=0)
        cancel_btm.grid(row=2, column=0)
        
        confirmation_window.mainloop()


window = tk.Tk()
window.title("Redmine Auto time logger")

tk.Label(window, text='Username').grid(row=0)
tk.Label(window, text='Password').grid(row=1)
tk.Label(window, text='First_date').grid(row=2)
tk.Label(window, text='Duration').grid(row=3)

username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show='*')
first_date_entry = tk.Entry(window)
duration_entry = tk.Entry(window)

# img = ImageTk.PhotoImage(Image.open('dog_meme.jpg'))
# imglabel = tk.Label(window, image=img).grid(row=0, column=1)

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
first_date_entry.grid(row=2, column=1)
duration_entry.grid(row=3, column=1)

btn = tk.Button(
    master=window,
    text="Enter",
    command=username_password
)

check = tk.Label(master=window)

btn.grid(row=3, column=2)
check.grid(row=5, column=1)

window.mainloop()