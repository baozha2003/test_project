import time
import datetime


def today():
    today = datetime.date.today()
    return today


def endday():
    Sevenday = datetime.timedelta(days=7)
    endday = today + Sevenday
    return endday


if __name__ == "__main__":
    today = today()
    endday = endday()
    print(today)
    print(endday)
