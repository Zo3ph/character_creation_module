
from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculatesquareroot(your_number):
    """Вычисляет квадратный корень."""
    return sqrt(your_number)


def calc(your_number):
    """Ввод числа."""
    if your_number <= 0:
        return
    result = calculatesquareroot(your_number)

    print('Мы вычислили квадратный корень из введённого вами числа. Это будет: ' 
         f'{calculatesquareroot(your_number)}')


print(message)
calc(25.5)
