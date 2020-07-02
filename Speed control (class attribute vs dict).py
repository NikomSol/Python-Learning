from time import process_time
# from timeit import timeit

"""
Сравниваем время обращения к атрибуту класса и к элементу словаря
Примерно поровну
"""
class Class:
    # __slots__ = 'a','b','c'
    def __init__(self):
        self.a = 1
        self.b = 1
        self.c = 1

cl = Class()

start = process_time()
for i in range(10**7):
    cl.a
end = process_time()

print('att time: ',end - start)
#0.6-0.7 s


dict = {'a':1,'b':1,'c':1}

start = process_time()
for i in range(10**7):
    dict['a']
end = process_time()

print('dict time: ',end - start)
#0.6-0.7 s
