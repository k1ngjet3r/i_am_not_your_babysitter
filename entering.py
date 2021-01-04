import datetime as dt
# username = input('Enter your username: ')
# password = input('and your password: ')
# start_date = input('The first day you want to log: ')
# duration = input('How many days you want to log? ')
# print("So you want to log {} days started from {}?".format(duration, start_date))
# conformation = input('Are you sure? (y/n)')
# print('Entering the user info...')


def date_validation(date):
    y = int(date[:4])
    m = int(date[4:6])
    d = int(date[6:])

    return dt.date(year=y, month=m, day=d)


while True:
    username = input('Enter your username: ')
    password = input('and your passaasdfword: ')
    start_date = input('The first day you want to log: ')
    try:
        date_validation(start_date)
    except:
        print('please enter the valid date')
        break

    duration = input('How many days you want to log? ')

    print("So you want to log {} days started from {}?".format(duration, start_date))
    conformation = input('Are you sure? (y/n)')
    print('Entering the user info...')
