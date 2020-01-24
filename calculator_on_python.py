import math


def is_digit(string):
    try:
        float(string)
        return True
    except ValueError:
        print('Ошибка!! <', string, '> нельзя преобразовать к числу! Введите корректные данные!')
        return False


def is_operator_support(operator):
    z = ['-', '*', '/', '%', '//', 'cos', 'x^2']
    if operator in z:
        return True

    else:
        print('вы ввели неподдерживаемый оператор')
    return False


def calculator():
    while True:
        x = input('введите первое число: ')
        a = input('введите операцию (* / //  % cos x^2): ')
        y = input('введите второе число: ')
        if is_digit(x) and is_digit(y) and is_operator_support(a):
            x = float(x)
            y = float(y)
            break

    if a == '*':
        print(x * y)
    elif a == '+':
        print(x + y)
    elif a == '-':
        print(x - y)
    elif a == '/':
        print(x / y)
    elif a == '//':
        print(x // y)
    elif a == '%':
        print(x % y)
    elif a == 'cos':
        print(math.cos(x))
    elif a == 'x^2':
        print(math.sqrt(x))


while 1:
    calculator()
