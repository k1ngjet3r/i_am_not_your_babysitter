import tkinter as tk


def username_password():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    username = username_entry.get()
    password = password_entry.get()
    first_date = first_date_entry.get()
    duration = duration_entry.get()
    confirmation['text'] = 'Log time from {}, total {} days, are you sure?'.format(
        first_date, duration)


window = tk.Tk()
window.title("Redmine Auto time logger")

tk.Label(window, text='username').grid(row=0)
tk.Label(window, text='password').grid(row=1)
tk.Label(window, text='First_date').grid(row=2)
tk.Label(window, text='Duration').grid(row=3)

username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show='*')
first_date_entry = tk.Entry(window)
duration_entry = tk.Entry(window)

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
first_date_entry.grid(row=2, column=1)
duration_entry.grid(row=3, column=1)

btn = tk.Button(
    master=window,
    text="Enter",
    command=username_password
)

confirmation = tk.Label(master=window)

btn.grid(row=0, column=2)
confirmation.grid(row=5, column=1)

window.mainloop()
