class Time:
    """ Representa la hora del dia

    attributes:
        - hour: int
        - minute: int
        - second: int
    """

def print_time(t):
    """ Imprime time t en formato hora:minuto:segundo """
    print("%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second))

def is_after(t1, t2):
    """ Regresa True si t1 ocurre después de t2 """
    c1 = t1.hour > t2.hour
    c2 = t1.hour == t2.hour and t1.minute > t2.minute
    c3 = t1.hour == t2.hour and t1.minute == t2.minute and t1.second > t2.second
    return c1 or c2 or c3

def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2), 'invalid Time object in add_time'
    return int_to_time(time_to_int(t1) + time_to_int(t2))

def sub_time(t1, t2):
    return int_to_time(time_to_int(t1) - time_to_int(t2))

def increment(t, seconds):
    t2 = pure_increment(t, seconds)
    t.second = t2.second
    t.minute = t2.minute
    t.hour = t2.hour

def pure_increment(t, seconds):
    return int_to_time(time_to_int(t) + seconds)

def time_to_int(t):
    minutes = t.hour * 60 + t.minute
    return minutes * 60 + t.second

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.second >= 60 or t.minute >= 60:
        return False
    return True

def mul_time(t, n):
    return int_to_time(time_to_int(t) * n)

def avg_peace(end_time, distance):
    return

if __name__ == "__main__":
    start = Time()
    start.hour = 9
    start.minute = 45
    start.second = 0
    print_time(start)

    duration = Time()
    duration.hour = 1
    duration.minute = 35
    duration.second = 0
    print_time(duration)

    done = add_time(start, duration)
    print_time(done)

    print_time(pure_increment(done, 60**2))

    print_time(sub_time(done, duration))

    bad = Time()
    bad.hour = 13
    bad.minute = 0
    bad.second = -1
    #add_time(start, bad)

    print_time(mul_time(duration, 2))
