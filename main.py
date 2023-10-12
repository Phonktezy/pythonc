#1
from math import sqrt
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print(distance(x1, x2, y1, y2))
#2
def power(a, b):
    res = 1
    for i in range(abs(b)):
        res *= a
    if b >= 0:
        return res
    else:
        return 1 / res
print(power(float(input()), int(input())))
#3
def func(n):
    if n == 1 or n == 2:
        return 1
    else:
        return func(n - 1) + func(n - 2)
print(func(int(input())))
#4
def ys(y):
    y = int(input("Вставьте желаемый год: "))
    if ys%4 != 0 or (ys%100==0 and ys%400!=0):
        return True
    else:
        return False
#5
def square(a):
    return 4 * a, a * a, a * 2 ** 0.5
#6
def season(m):
    if mo in [2, 12, 1]:
     print("Зима")
    elif m in [3, 4, 5]:
     print("весна")
    elif m in [6, 7, 8]:
     print("лето")
    elif m in [9, 10, 11]:
     print("осень")
    else:
     print("Неверный номер месяца")
#7
def bank(a, years):
    for a in range(years):
        a = a * 1.1
    return a
#8
def simpnums(a):
    if a % a == 0 and a != 0:
        return True
    else:
        return False

a = int(input("Введите номер: "))
print(easynums(a))
#9
def mdate(days, month, years):
    if days < 0 or month < 0 or years < 0:
        return False

    mon = [28, 30, 31]

    if years % 400 == 0 or ((years % 4 == 0) and (years % 100 != 0)):
        month[1]=29
    if month>=1 and month<=12:
       if days > 0 and days <=mon[month-1]:
           return True
    return False






