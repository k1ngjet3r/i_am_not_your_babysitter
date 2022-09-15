import datetime as dt

'''
    checking the entered date format
'''

def date_validation(date):
    date = str(date)
    # if date format is 20210101
    if len(date) == 8:
        y = int(date[:4])
        m = int(date[4:6])
        d = int(date[6:])
    # if data format is something like 2021-01-01 or 2021.01.01 or 2021/01/01
    elif len(date) == 10:
        y = int(date[:4])
        m = int(date[5:7])
        d = int(date[-2:])
    
    try:
        return dt.date(year=y, month=m, day=d)

    except:
        return False

def first_date_and_end_date_validation(first_date, end_date):
    first_date = date_validation(first_date)
    end_date = date_validation(end_date)

    if first_date >= end_date:
        return False
    return True


if __name__ == '__main__':
    print(first_date_and_end_date_validation('20221208', '20221208'))
