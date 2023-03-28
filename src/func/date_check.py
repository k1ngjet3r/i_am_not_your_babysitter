import json
import datetime


with open('src/json/national_holiday.json') as f:
    EXCEPTION_DATE = json.load(f)

NATIONAL_HOLIDAY = [EXCEPTION_DATE['year'] + day for day in EXCEPTION_DATE['holiday']]
MAKE_UP_DAY = [EXCEPTION_DATE['year'] + day for day in EXCEPTION_DATE['make_up']]


def date_determination(date: datetime.date):
    if (date.weekday() == 5 or date.weekday() == 6) and str(date) not in MAKE_UP_DAY:
        return False
    else:
        True 


if __name__ == '__main__':
    date = datetime.date(2023, 1, 1)
    print(type(date))

    print(date_determination(date))
    