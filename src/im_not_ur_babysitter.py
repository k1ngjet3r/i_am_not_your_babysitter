import tkinter as tk
from PIL import Image, ImageTk
from func.date_format_validation import date_validation, first_date_and_end_date_validation
import datetime as dt
from src.logger import Logger
import random

window = tk.Tk()
window.title("I'm Not Your babysitter!")
rick_img = str(random.choice(range(1, 43))) + '.jpg'


def logging_time():
    username = username_entry.get()
    password = password_entry.get()
    first_date = first_day_entry.get()
    end_date = end_date_entry.get()
    logging = Logger(username, password, first_date, end_date)
    logging.start_log_time()


def confirmation():
    '''
        Get the username, password, first_date, and end_date from the gui
    '''
    username = username_entry.get()
    password = password_entry.get()
    first_date = first_day_entry.get()
    end_date = end_date_entry.get()

    if username == '':
        error_msg['text'] = 'Please enter your username'
    elif password == '':
        error_msg['text'] = 'Where is your password'
    elif first_date == '':
        error_msg['text'] = 'Enter the first day you want \n to log motherfucker'
    elif not date_validation(first_date):
        error_msg['text'] = 'You entered an invalid first date, \n please enter a valid date.'
    elif not date_validation(end_date):
        error_msg['text'] = 'You entered an invalid end date, \n please enter a valid date.'
    elif not first_date_and_end_date_validation(first_date, end_date):
        error_msg['text'] = 'Invaild duration! please check both \n entered first date and end date.'
    elif end_date == '':
        error_msg['text'] = 'Are you kidding me?'
    else:
        confirmation_window = tk.Toplevel(window)
        confirmation_window.title('Confirmation')

        top_con_frame = tk.Frame(confirmation_window)
        top_con_frame.pack(side=tk.TOP)

        btn_frame = tk.Frame(confirmation_window)
        btn_frame.pack(side=tk.TOP)

        confirmation_msg = tk.Label(top_con_frame)
        
        try:
            start_date = date_validation(first_date)
            end_date = date_validation(end_date)

            confirmation_msg['text'] = "So you want to log time from {} to {}?".format(
                start_date, end_date)

            confirmation_msg.pack(side=tk.TOP)

            confirm_btn = tk.Button(
                            master=btn_frame,
                            text="Yes, bring it on",
                            command=logging_time
                            )               
            confirm_btn.pack(side=tk.LEFT, ipadx=20, fill=tk.X)

            cancel_btn = tk.Button(
                            master=btn_frame,
                            text="No, I want my mommy",
                            command=confirmation_window.destroy
                            )
            cancel_btn.pack(side=tk.LEFT, ipadx=20, fill=tk.X)

        except:
            confirmation_msg['text'] = 'Please enter a correct date format!'
            confirmation_msg.pack(side=tk.TOP)

            close_btn = tk.Button(master=btn_frame, text='Close', command=confirmation_window.destroy)
            close_btn.pack()
            
        confirmation_window.lift()
        
        confirmation_window.mainloop()


header_label = tk.Label(window, text="I'm Not Your Babysitter!")
header_label.pack()

# Image frame
img_frame = tk.Frame(window)
img_frame.pack(side=tk.TOP)

try:
    selected_image = Image.open(f'img\\{rick_img}')
except FileNotFoundError:
    selected_image = Image.open(f'img/{rick_img}')

selected_image = selected_image.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(selected_image)
panel = tk.Label(img_frame, image=img)
panel.pack()

# Execute frame
exe_frame = tk.Frame(window)
exe_frame.pack(side=tk.BOTTOM)

# defining frame that containing labels
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT)

username_label = tk.Label(left_frame, text='Username')
username_label.pack(side=tk.TOP)
password_label = tk.Label(left_frame, text='Password')
password_label.pack(side=tk.TOP)
first_day_label = tk.Label(left_frame, text='First date')
first_day_label.pack(side=tk.TOP)
end_date_label = tk.Label(left_frame, text='End date')
end_date_label.pack(side=tk.TOP)

# defining frame that containing entry fields
right_frame = tk.Frame(window)
right_frame.pack(side=tk.LEFT)

username_entry = tk.Entry(right_frame)
username_entry.pack(side=tk.TOP)
password_entry = tk.Entry(right_frame, show='*')
password_entry.pack(side=tk.TOP)
first_day_entry = tk.Entry(right_frame)
first_day_entry.pack(side=tk.TOP)
end_date_entry = tk.Entry(right_frame)
end_date_entry.pack(side=tk.TOP)

# # Execute frame
# exe_frame = tk.Frame(window)
# exe_frame.pack(side=tk.BOTTOM)

error_msg = tk.Label(exe_frame)
error_msg.pack(side=tk.TOP)
enter_btn = tk.Button(exe_frame, text="Start", command=confirmation)
enter_btn.pack(side=tk.TOP, ipadx=20, fill=tk.X)

creator_label = tk.Label(exe_frame, text="Created by Jeter\n Img donated by Logan", fg='blue')
creator_label.pack()

window.lift()

window.mainloop()
