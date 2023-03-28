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

def start_date_and_end_date_validation(start_date, end_date):
    if not start_date or not end_date:
        return 'Start date or end date cannot be left empty'

    start_date = date_validation(start_date)
    end_date = date_validation(end_date)

    if not start_date:
        return 'Worng start date format'
    if not end_date:
        return 'Worng end date format'


    if start_date > end_date:
        return 'Start date should be earlier than end date'
    return True


if __name__ == '__main__':
    print(start_date_and_end_date_validation('20221208', '20221208'))
