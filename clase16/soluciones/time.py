class Time:
    """ Representa la hora

    attributes:
    - hour: int
    - minute: int
    - second: float
    """

def print_time(time):
    """ Imprime time en formato hora:minuto:segundo """
    assert valid_time(time)
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def is_after(t1, t2):
    """ Regresa True si t1 ocurre después que t2 """
    assert valid_time(t1) and valid_time(t2)
    c1 = t1.hour > t2.hour
    a1 = t1.hour == t2.hour
    c2 = a1 and t1.minute > t2.minute
    c3 = a1 and t1.minute == t2.minute and t1.second > t2.second
    return c1 or c2 or c3 

def add_time(t1, t2):
    """ Toma dos time t1 y t2, y regresa un time que es la suma de t1 y t2 """
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def sub_time(t1, t2):
    """ Toma dos time t1 y t2, regresa un time que es la diferencia de ambos """
    seconds = time_to_int(t1) - time_to_int(t2)
    return int_to_time(seconds)

def increment(time, seconds):
    """ Agrega a time la cantidad en seconds """
    res = increment_pure(time,seconds)
    time.second = res.second
    time.minute = res.minute
    time.hour = res.hour

def increment_pure(time,seconds):
    """ Regresa un objeto time resultado de sumar seconds a time """
    return int_to_time(seconds + time_to_int(time))

def time_to_int(time):
    """ Convierte un time en su representación en entero base 60 """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    """ Convierte seconds en su representación en time

    seconds está en representación base 60 """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
def valid_time(t):
    """ Verifica que t sea un time válido

    hour debe ser positivo
    minute y second deben de estar en el rango (0,60]
    second debe admitir punto decimal """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    if not isinstance(time.hour, int) or not isinstance(time.minute, int):
        return False
    if not isinstance(time.second, int) and not isinstance(time.second, float):
        return False
    return True

def mul_time(time, times):
    """ Toma time y regresa un time equivalente a time multiplicado times veces """
    if not valid_time(time):
        raise ValueError('invalid Time object in mul_time')
    return int_to_time(time_to_int(time) * times)

def avg_time(time, distance):
    """ Regresa un time que es la velocidad promedio de tiempo por millas """
    assert valid_time(time)
    return mul_time(time, 1/distance)

if __name__ == '__main__':
    time = Time()
    time.hour = 11
    time.minute = 1
    time.second = 5

    time3 = add_time(time, time)
    print_time(time3)

    print_time(time)

    time2 = Time()
    time2.hour = 11
    time2.minute = 1
    time2.second = 59

    print_time(time2)
    print(is_after(time, time))
    print(is_after(time, time2))
    print(is_after(time2, time))

    time3 = add_time(time, time)
    print_time(time3)

    time4 = add_time(time2, time3)
    print_time(time4)

    time5 = increment_pure(time4, 120 * 60)
    print_time(time5)

    increment(time4, 120 * 60)
    print_time(time4)

    print_time(mul_time(time5, 2))