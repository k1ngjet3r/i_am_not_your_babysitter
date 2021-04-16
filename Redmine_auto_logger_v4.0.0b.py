import tkinter as tk
from PIL import Image, ImageTk
from func.date_format_validation import date_validation
import datetime as dt
from logger import Logger

window = tk.Tk()
window.title("Redmine Auto time logger")

def logging_time():
    username = username_entry.get()
    password = password_entry.get()
    first_date = first_day_entry.get()
    duration = duration_entry.get()
    logging = Logger(username, password, first_date, duration)
    logging.start_log_time()

def confirmation():
    '''
        Get the username, password, first_date, and duration from the gui
    '''
    username = username_entry.get()
    password = password_entry.get()
    first_date = first_day_entry.get()
    duration = duration_entry.get()

    if username == '':
        error_msg['text'] = 'Please enter your username'
    elif password == '':
        error_msg['text'] = 'Where is your password'
    elif first_date == '':
        error_msg['text'] = 'Enter the first day you want \n to log motherfucker'
    elif date_validation(first_date) == False:
        error_msg['text'] = 'You entered an invalid date, \n please enter a valid date.'
    elif duration == '':
        error_msg['text'] = 'Are you kidding me?'
    else:
        confirmation_window = tk.Toplevel(window)
        confirmation_window.title('Confirmation')

        top_con_frame = tk.Frame(confirmation_window)
        top_con_frame.pack(side=tk.TOP)

        btn_frame = tk.Frame(confirmation_window)
        btn_frame.pack(side=tk.TOP)

        confirmation_msg = tk.Label(top_con_frame)

        start_date = date_validation(first_date)
        end_date = start_date + dt.timedelta(days=int(duration)-1)

        confirmation_msg['text'] = "So you want to log {} days\n started from {} to {}?".format(
            duration, start_date, end_date)
        
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

        confirmation_window.lift()
        
        confirmation_window.mainloop()


header_label = tk.Label(window, text='Please Enter Your Info')
header_label.pack()

# Image frame
img_frame = tk.Frame(window)
img_frame.pack(side=tk.TOP)
selected_image = Image.open('img\\dog.jpeg')
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
first_day_label = tk.Label(left_frame, text='First day')
first_day_label.pack(side=tk.TOP)
duration_label = tk.Label(left_frame, text='Duration')
duration_label.pack(side=tk.TOP)

# defining frame that containing entry fields
right_frame = tk.Frame(window)
right_frame.pack(side=tk.LEFT)

username_entry = tk.Entry(right_frame)
username_entry.pack(side=tk.TOP)
password_entry = tk.Entry(right_frame, show='*')
password_entry.pack(side=tk.TOP)
first_day_entry = tk.Entry(right_frame)
first_day_entry.pack(side=tk.TOP)
duration_entry = tk.Entry(right_frame)
duration_entry.pack(side=tk.TOP)

# # Execute frame
# exe_frame = tk.Frame(window)
# exe_frame.pack(side=tk.BOTTOM)

error_msg = tk.Label(exe_frame)
error_msg.pack(side=tk.TOP)
enter_btn = tk.Button(exe_frame, text="Start", command=confirmation)
enter_btn.pack(side=tk.TOP, ipadx=20, fill=tk.X)

window.lift()

window.mainloop()
