from datetime import date


def numOfDays(date1, date2):
    return (date2 - date1).days


# Driver program
date1 = date(2014, 7,2)
date2 = date(2014, 7, 11)
print(numOfDays(date1, date2), "days")