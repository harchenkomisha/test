days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
def next_date(day,month,year):
    """ Возвращает следующую дату
    Args:
        day(int): день
        month(int): месяц
        year(int): год
    """
    day += 1
    if day >  days_in_month[month]  \
        + leap_year(year) if month == 2 else 0:
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1
    return day,month,year


def prev_date(day,month,year):
    """ Возвращает предыдущую дату
    Args:
        day(int): день
        month(int): месяц
        year(int): год
    """
    day -= 1
    if day ==  0:
        month -= 1
        if month == 00:
            month = 12
            year -= 1
        day = days_in_month[month] \
             + leap_year(year) if month == 2 else 0
    return day,month,year


def leap_year(year):
    """Определяет высокосный год
    Args:
        year(int): гоl
    """
    return(year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0)

day, month, year = map(
    int,
    input('Введите дату, например: 24.09.2022 -->').split('.'))

print(next_date(day, month, year))
print(prev_date(day, month, year))