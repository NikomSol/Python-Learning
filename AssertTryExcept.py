def g(x):
    return 1 / x

try: # проверяем на исключение
    g(0)
except ArithmeticError:
    print('Infinity') # выполняем в случае возникновения исключения
else:
    print(g(0)) # выполняем если исключения не возникло
finally:
    print('Мне все равно, что происходит') # выполняем в любом случае

try:
    g(1)
except ArithmeticError:
    print('Infinity')
else:
    print(g(1))
finally:
    print('Мне все равно, что происходит')


def f(x):
    assert x != 0, "Zero" # проверяем, в случае False разваливаем программу с AssertionError: Zero
    return 1/x

print(f(1))
# print(f(0))