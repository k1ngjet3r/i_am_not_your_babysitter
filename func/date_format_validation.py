import datetime as dt

'''
    checking the entered date format
'''

def date_validation(first_date):
    first_date = str(first_date)
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
    
    try:
        return dt.date(year=y, month=m, day=d)

    except:
        return False
