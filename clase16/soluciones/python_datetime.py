from datetime import date, timedelta, datetime

def print_day_name():
    """ Imprime el nombre del día de hoy """
    current = date.today()
    name = current.strftime('%A')
    print(name)

def get_age(birthday, on_date=datetime.today()):
    """ Regresa la edad actual según el día de nacimiento birthday """
    today = on_date
    b = birthday
    next_birthday = datetime(today.year, b.month, b.day, b.hour, b.minute, b.second)

    age = today.year - birthday.year
    if today < next_birthday:
        return age - 1
    return age

def until_next_birthday(birthday):
    """ Regresa el número de días, horas, minutos y segundos hasta el siguiente cumpleaños """
    today = datetime.today()
    b = birthday
    next_birthday = datetime(today.year, b.month, b.day, b.hour, b.minute, b.second)
    if today > next_birthday:
        next_birthday.year += 1
    
    diff = next_birthday - today
    print(diff)

def double_day(b1, b2):
    """ Regresa el día en el que es el día doble de alguien que nació en b1 y otro en b2 """
    #s = sorted([b1, b2])
    #diff = s[1] - s[0]
    #return s[1] + diff

    return n_day(b1, b2, 2)

def n_day(b1, b2, n):
    """ Regresa el día en el que es el día n times de alguien que nació en b1 y otro en b2 """
    s = sorted([b1, b2])
    b = s[0] - datetime.min
    a = s[1] - datetime.min

    diff = (b - (a * n)) / (1 - n)
    return datetime.min + diff

if __name__ == '__main__':
    print('Día de la semana actual: ', end='')
    print_day_name()

    b = datetime(1997,12, 31, 6, 0 ,0)

    age = get_age(b)
    print(age)

    until_next_birthday(b)

    b2 = datetime(1992, 7, 31, 15, 0, 0)

    dd = double_day(b, b2)
    print(dd)
    for i in range(2, 10):
        print(i, n_day(b, b2, i))
