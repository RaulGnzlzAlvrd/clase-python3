class Time:
    """ Representa la hora

    attributes:
    - hour: int
    - minute: int
    - second: float
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """ Imprime en formato hora:minuto:segundo """
        assert self.valid_time()
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        """ Regresa su representación en entero base 60 """
        assert self.valid_time()
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        """ Regresa un objeto time resultado de sumar seconds """
        assert self.valid_time()
        seconds += time.time_to_int()
        return int_to_time(seconds)

    def __gt__(self, other):
        """ Regresa True si ocurre después que other """
        assert self.valid_time() and self.valid_time()
        return self.time_to_int() > other.time_to_int()

    def valid_time(self):
        """ Verifica que sea un time válido

        hour debe ser positivo
        minute y second deben de estar en el rango (0,60]
        second debe admitir punto decimal """
        if not isinstance(self, Time):
            return False
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        if not isinstance(self.hour, int) or not isinstance(self.minute, int):
            return False
        if not isinstance(self.second, int) and not isinstance(self.second, float):
            return False
        return True

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        if isinstance(other, int) or isinstance(other, float):
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        """ Regresa un time que es la suma de self y other """
        if not self.valid_time() or not other.valid_time():
            raise ValueError('invalid Time object in add_time')
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __sub__(self, other):
        """ Regresa un time que es la diferencia de self con other """
        seconds = self.time_to_int() - other.time_to_int()
        return int_to_time(seconds)

    def __mul__(self, n):
        """ Regresa un time equivalente a self multiplicado n veces """
        if not self.valid_time():
            raise ValueError('invalid Time object in mul_time')
        return int_to_time(self.time_to_int() * n)

def avg_time(time, distance):
    """ Regresa un time que es la velocidad promedio de tiempo por millas """
    assert time.valid_time()
    return time * (1/distance)

def int_to_time(seconds):
    """ Convierte seconds en su representación en time

    seconds está en representación base 60 """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

if __name__ == '__main__':
    time = Time(11, 1, 5)
    print(time)

    # Se puede usar de cualquiera de las dos formas
    # la primera es la menos usual
    #Time.print_time(time)
    #time.print_time()

    # Una forma conveniente para usar la primera forma
    #Time.print_time(mul_time(time, 2))
    print(time * 2)

    # Si se usa init sin parámetros ocupa los valores por defecto
    #Time.print_time(Time())
    print(Time())

    # Probando el método __add__
    start = Time(9,45)
    duration = Time(1,30,25)
    end = start + duration
    print("Start:\t", start)
    print("End:\t", end)

    print("Duration:\t", end - start)
