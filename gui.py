from logger import Logger
import time
import datetime as dt
from date_format_validation import date_validation
import json
import tkinter as tk

def username_password():
    '''
        Get the username, password, first_date, and duration from the gui
    '''
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
                        text="Yes, bring it on"
                        )               
        
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

