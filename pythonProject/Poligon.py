"""
a:int = 81              javobi: EKUB (81;45)
b:int = 45
import math
c = math.gcd(a,b)
print(c)
from _typeshed import SupportsLessThan
from typing import List, Any """
#   Foydalanuvchidan haqiqiy son so’rab uni ilmiy ko’rinishga o’tkazib chiqaradigan dastur tuzing.
# Masalan: 120000—>1.2*10^5
'''
a = input('Sonni kiriting: ')
b = str(a)
c = b[0:2]
d = int(c)      javobi: 1.6*10^3
e = d/10
f = str(e)
g = "*10^"
h = len(b)
i = int(h)
j = i - 1
k = str(j)
l = f + g + k
print(l)
'''
# 2 chi usul
'''
a = input('Sonni kiriting: ')
b = int(len(a))
c = int(a) / (10**(b-1))
d = f'{c}' + f'*10^{b-1}'
print(d)
'''

# 5-dars
'''
age = 29
if age >= 18:
    print("Ovoz berishingiz mumkin")
else:
    print("Ovoz berish mumkin emas")  '''

# 5-dars  1-topshiriq
'''`
number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))
this_number = ""
if number_1 % 2 == 1:
    print("This is odd number")
else:
    print("This is even number")

if number_2 % 2 == 0:
    print("This is even number")
else:
    print("This number is incorrect")   '''

# 5-dars  2-topshiriq
'''
number = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))
number_3 = int(input("Enter your third number: "))
if number % 5 == 0 and number % 3 == 0:
    print("FizBiz")
elif number % 5 == 0:
    print("Biz")
elif number % 3 == 0:
    print("Fiz")
else:
    print(number)


if number_2 % 5 == 0 and number_2 % 3 == 0:
    print("FizBiz")
elif number_2 % 5 == 0:
    print("Biz")
elif number_2 % 3 == 0:
    print("Fiz")
else:
    print(number_2)


if number_3 % 5 == 0 and number_3 % 3 == 0:
    print("FizBiz")
elif number_3 % 5 == 0:
    print("Biz")
elif number_3 % 3 == 0:
    print("Fiz")
else:
    print(number_3)   '''

'''
import  math
a = int(input("a sonni kiriting: "))
b = int(input("b sonni kiriting: "))
c = int(input("c sonni kiriting: "))
e = pow(b,2)-4*a*c
if e < 0:
    print("Tenglama yechimga ega emas")
if e > 0:
    print("Tenglama 2 ta yechimga ega")
if e == 0:
    print("Tenglama 1 ta yechimga ega")  '''

# 6-dars 1-vazifa
'''
a = ["Father", "Mather", "Sister"]
b = a [0]
c = a[1]
d = a[2]
print(b)
print(c)
print(d) '''

# 6-dars 2-vazifa
'''words = input("Vergul bilan ajratib ismlarni kiriting: ").split(sep=",")[::-1]      # javobi: kiritilgan 
ma'lumotlarni teskarisiga yozib beradi. print(words) '''

# Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligini alifbo tartibida chiqaradigan dastur
# tuzing Masalan:  Ismlar: john, alice, bob Natija: alice, bob, john
'''
words = input("Vergul bilan so'zlarni kiriting: ").split(sep=",")
words.sort()
print(words)  '''

# Standart kiruvchi ma'lumotdagi vergullar bilan ajratilgan so'zlar ketma-ketligi orasida maqsad qilingan so'z aynan
# qaysi indeksda turganligini aniqlovchi dastur tuzing Masalan:  -  Ismlar: john, alice, bob Maqsad: bob Natija: 2
'''
words = input("Vergul bilan ajratib kiriting: ").split(sep=",")
a = words.index("bob")
print(a)  '''

# Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligida maqsad qilingan so'z necha marta
# takrorlanganligini aniqlovchi dastur tuzing Masalan: -  Ismlar: alice, john, bob, alice, bob, john,
# alice -  Maqsad: alice -  Natija: 3
'''
words = input("Vergul bilan ajratib kiriting: ").split(sep=",")
purpose = input("Maqsad: ")
x = words.count(purpose)
print(x) '''

# 7- dars 1-topshiriq Standart input orqali vergul bilan ajratilgan sonlarni o'qing va u yerda nechta son
# qatnashganini ekranga chiqaring (takrorlanishlar inobatga olinmasin).

# Misollar:
# Input: 2,3,3,4
# Natija: 3

# Input: 1,1,1,1,1
# Natija: 1

# Input: 1,2,3
# Natija: 3
'''
numbers = input("Sonlarni vergul bilan ajratib kiriting: ").split(sep=",")
a = set(numbers)
b = len(a)
print(b)   '''

# Standart kiruvchi ma'lumot sifatida ikkita so'zni o'qib olib, ularning anagram (bitta so'zni ikkinchisidan ajratib
# olish mumkin) ekanligini tekshiruvchi dastur tuzing. Havola: https://leetcode.com/problems/valid-anagram/ Masalan:
# Kiruvchi ma'lumot: anagram gramana Natija: True Kiruvchi ma'lumot: rat cat Natija: False
'''
s = list(input("1 chi so'zni kiriting: "))
t = list(input("2 chi so'zni kiriting: "))
u = sorted(s)
v = sorted(t)
if u == v:
    print("True")
else:
    print("False")  '''

# 8-dars 1-topshiriq:
# Salom deydigan greeting nomli funksiya tuzing va unga docstring yozing.

# def greeting(Text):
#  '''This is greeting function. It takes user's name'''
# return "{a}".format(a=Text)

# print(greeting("What's your name?"))
# help(greeting)


# 8-dars 2-topshiriq

# def greeting(name):
# return "Hello {d}".format(d=name)
# print(greeting("Dilshod"))


# 8-dars
# Parametr sifatida ismni o’qib olib, uni teskari tartibda chiqarib beradigan funksiya tuzing.
# def ask_name(name):
#   return name[::-1]
# print(ask_name("aziz"))

# Standart kirituvchi ma’lumot sifatida ismlarni o’qib olib, ularning ichidan eng uzunini chiqaruvchi dastur tuzing

'''text = input("Ismlarni vergul bilan ajratib kiriting: ").split(sep=",")
def myfunc(text):
    return len(text)
names = text
a = names.sort(key=myfunc)
b = names[-1]
print(b)   '''

# 1 - 100 oraliqdagi natural sonlardan 7 ga karrali sonlarning kvadratlarini ekranga chiqaring.

# for x in range(1,100):
# if x % 7 == 0:
# print(x**2)


# 2 dan 9 gacha bo’lgan sonlarning karra jadvalini ekranga chiqaruvchi dastur tuzing

# for x in range(2,10):
#   for y in range(0,11):
#      print(str(x) +"*" + str(y) + " =", x*y)


# Standart kiruvchi ma’lumotdan sonlarni o’qib olib, ushbu sonlarning raqamlarini teskari tartibda chiqaruvchi dastur
# tuzing. Masalan: Sonlar: 102 346 5897 Natija: 201 643 7985
'''
x = input("sonlarni vergul bilan ajratib kiriting: ").split(sep=",")
for y in x:
    print(y[::-1], end=" ") '''

# Quyidagi havoladagi Fizz Buzz misolini ishlang:  https://leetcode.com/problems/fizz-buzz/
'''
number = int(input("Sonni kiriting: "))
i = 1
while i < number:
    i += 1
    if i % 3 == 0 and not i % 15 == 0:
        print("Fizz", end=" ,")
    elif i % 5 == 0 and not i % 15 == 0:
        print("Buzz", end=" ,")
    elif i % 15 == 0:
        print("FizzBuzz")
    else:
        print(i, end=" ,")  '''

# Standart kiruvchi ma’lumot sifatida ismni o’qib olib, uni rekursiv funksiya yordamida teskari tartibda qaytaruvchi
# dastur tuzing

'''
def function(named):
    if len(named) == 1:
        return named[0]
    return named[len(named)-1] + function(named[0:(len(named)-1)])


name = input("Ismni kiriting: ")
print(function(name))   '''

# IndexError va KeyError hosil qiladigan kod yozing
'''
try:
    get_1 = [11100, 11300]
    a = {"dollor": get_1[3], "yevro": get_1[2]}
    print(a)
    print("sterling")
except IndexError or KeyError:
    print("Index and Key errors")   '''

# TypeError hosil qiladigan kod yozing
'''
try:
    information = input("Ismingizni kiriting: ")
    number = 2022
    print(information/number)
except TypeError:
    print("TypeError") '''

# 1- va 2- topshiriqda yozgan kodingizni try/except ichida yozib, ekranga errorni chiqaradigan kod yozing
'''
try:
    get_1 = [11100, 11300]
    a = {"dollor": get_1[3], "euro": get_1[2]}
    print(a, "Sterling")
except LookupError:
    print("LookupError")
try:
    information = str
    number = 2022
    print(information/number)
except TypeError:
    print("Type error") '''

# Har 2 soniyada ekranga vaqtni ko'rsatadigan kod yozing.
# Ctrl + C bosilganda (kod to'xtatilganda) ekranga "stopped" deb yozib, loopni to'xtating.

# Ayni vaqtni o'lish uchun "datetime" kutubxonasidan foydalaning. https://docs.python.org/3/library/datetime.html
# https://strftime.org/
'''
from datetime import datetime
now = datetime.now()
while int(now.strftime("%X")[len(now.strftime("%X"))-1]) % 2 == 0:
    print(now.strftime("%X"))  '''

# Darsda yaratilgan tahmin qilish o'yinini o'zgartiring: 3 marta xato taxmindan so'ng  o'yinni to'xtatib
# foydalanuvchi yutqizganligi haqida ekranga chiqaradigan kod yozing.
'''
import random
random_number = random.randint(1, 10)
guess = int(input("1 dan 10 gacha sonlardan bitta son o'yladim. Men qaysi sonni o'ylaganimni toping: "))
if random_number > guess or random_number < guess:
    print("xato")
    guess_2 = int(input("Yana urinib ko'ring: "))
    if random_number > guess_2 or random_number < guess_2:
        print("xato")
        guess_3 = int(input("Yana urinib ko'ring: "))
        if random_number > guess_3 or random_number < guess_3:
            print("xato va siz yutqazdingiz men " + "{a}".format(a=random_number) + " sonini o'ylagan edim.")
        elif random_number == guess_3:
            print("To'g'ri. Men " + "{a}".format(a=random_number) + " sonini o'ylagan edim.")
    elif random_number == guess_2:
        print("To'g'ri. Men " + "{a}".format(a=random_number) + " sonini o'ylagan edim.")
elif random_number == guess:
    print("To'g'ri. Men " + "{a}".format(a=random_number) + " sonini o'ylagan edim.")  '''


# Darsda yaratilgan tahmin qilish o'yinini o'zgartiring: 3 marta xato taxmindan so'ng  o'yinni to'xtatib
# foydalanuvchi yutqizganligi haqida ekranga chiqaradigan kod yozing.
'''
import random
random_number = random.randint(1, 10)
user_answer = 0
while user_answer < 3:
    user_answer += 1
    user = int(input("1 dan 10 gacha sonlardan bitta son o'yladim. Men qaysi sonni o'ylaganimni toping: "))
    if user < random_number or user > random_number:
        print("Xato")
        if user_answer == 3 and not user == random_number:
            print("Siz yutqazdingiz. Men " + "{u}".format(u=random_number) + " sonini o'ylagan edim.")
    elif user_answer < 3 and not user == random_number:
        print("Siz yutqazdingiz. Men " + "{u}".format(u=random_number) + " sonini o'ylagan edim.")
    elif user == random_number:
        print("To'g'ri. Men " + "{u}".format(u=random_number) + " sonini o'ylagan edim.")
        break   '''

# Student nomli class yarating.
# __init__ metodi orqali studentning ismi, yoshi va h,k larni qabul qilsin.
# about nomli metod ham qo'shing.
'''
class student:
    def __init__(self, first_name, last_name, age, education):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.education = education

    def about(self):
        return f'{self.first_name}, {self.last_name}'


Aziz = student("Aziz", "Hamidov", 27, "High education")
Bobur = student("Bobur", "Fayzirahmonov", 24, "Medium education")

print(f"student: {Aziz.about()}, age: {Aziz.age}, education: {Aziz.education} ")
print(f"student: {Bobur.about()}, age: {Bobur.age}, education: {Bobur.education} ")  '''

# Queue ma'lumot turini yarating.
# 3 ta metodni implement qilsin:
# 1. enque - element kiritish.
# 2. deque - elementni olish.
# 3. size - queue dagi elementlar sonini qaytarsin.
'''

class Queue:
    def __init__(self, first_name, last_name, Age):
        self.elements = [first_name, last_name, Age]

    def enque(self, education):
        return self.elements.append(education)

    def deque(self, Age):
        return self.elements.pop(Age)

    def size(self):
        return len(self.elements)


john = Queue("Aziz", "Obidov", 45)


def test_queue():
    john.enque("High")
    assert john.size() == 4

    john.deque(4)
    assert john.size() == 3


if __name__ == "__Poligon__":
    test_queue()        '''

# O'tgan dars vazifa sifatida yaratilgan Student classni o'zgartiring.
# Student class'dan yaratilgan obyektni print qiliganda studentni ismi ekranga  chiqarilsin.
# Misol:
# student = Student(name="John")
# print(student)
# John

'''
class Queue:
    def __init__(self, first_name):
        self.elements = [first_name]
        self.first_name = first_name

    def __str__(self):
        return self.first_name


student = Queue(first_name="John")
print(student) '''

# Dars davomida yaratilgan Vector class ga ayirish imkoniyatini qo'shing.

# Misol:
# v1 = Vector(3, 4)
# v2 = Vector(2, 4)

# v3 = v1 - v2
# v3 - Vector(1, 0) bo'lishi kerak.
# Vectorlar haqida qo'shimcha o'rganish uchun resurs - https://www.mathsisfun.com/algebra/vectors.html
'''

class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        a = self.x - other.x
        b = self.y - other.y
        return Vector(a, b)


v1 = Vector(3, 4)
v2 = Vector(2, 4)
v3 = v1 - v2
print(v3)  '''

# Student class yarating, name va age attributlari bo'lsin.
# Student class obyektlariga yosh bo'yicha taqqoslash  imkoniyatini qo'shing.

# Misol:
# john = Student(name="John", age=21)
# bob = Student(name="Bob", age=32)
# alice = Student(name="Alice", age=21)


# print(john > bob)  # False
# print(john < bob)  # True
# print(john == alice)  # True chiqishi kerak
'''
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age


John = Student(name="john", age=21)
Bob = Student(name="bob", age=22)
Alice = Student(name="alice", age=21)

print("John > Bob ", John > Bob)
print("John < Bob ", John < Bob)
print("John = Bob ", John == Alice)     '''

# Student nomi class yarating, __init__ da ism, familiyani qabul qilsin.
# Misol:  student = Student('John', 'Smith')

# Student classga from_full_name nomli class metod qo'shing, to'liq ismni qabul qilsin va qabul qilingan stringdan
# ism va familiyani ajratib olib student yaratsin.

# Misol:
# student = Student.from_full_name('John Smith')
# print(student.first_name) # 'John'
# print(student.last_name) # 'Smith'

'''
class Student:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        x = list(full_name.split(sep=' '))
        return cls(x[0], x[1])


student = Student.from_full_name("Steve Jobs")
print(student.first_name)
print(student.last_name)    '''

# Calculator nomli class yarating.
# add, subtract, multiply, divide nomi static metodlar qo'shing.

# Misol:
# print(Calculator.add(1, 2))  # 3
# print(Calculator.subtract(1, 2))  # -1
# print(Calculator.multiply(1, 2))  # 2
# print(Calculator.divide(1, 2))  # 0.5
'''
class Calculator:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x/y


print(Calculator.add(4, 12))
print(Calculator.sub(4, 12))
print(Calculator.mul(4, 12))
print(Calculator.divide(4, 8))      '''

# 2-modul 3-dars: Yangi Teacher classini hosil qiling va u dars mobaynida yaratilgan User classidan voris olsin.
# Dars mobaynida yaratilgan Mentor classi User class dan emas Teacher classdan voris olsin. Teacher classiga subclass
# bo'lgan yangi Assistant classini ham yarating.
'''
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} login")

    def logout(self):
        print(f"{self.name} logout")


class Teacher(User):
    def check_task(self):
        print(f"{self.name} checked homework")

    def send_answer(self):
        print(f"{self.name} sent homework results")


class Mentor(Teacher):
    def block_student(self):
        print(f"{self.name} blocked student")


class Assistant(Teacher):
    def block_student(self):
        print(f'{self.name} blocked student')


mentor = Mentor("Dilshod", "dilshod@example.com")
assistant = Assistant("Jasur", "jasur@example.com")

mentor.login()
assistant.login()
mentor.check_task()
assistant.send_answer()
mentor.block_student()      '''

# 2-modul 4-dars: Quyidagi ishlarni bajaradigan dastur tuzing:
#     file.txt nomli text fayl yaratib,
#     ichiga "Hello Files" deb yozsin.
'''
file = open("file.txt", 'w')

file.write("Hello files")
file.close()   '''

# data.gov.uz saytidan
# https://data.gov.uz/uz/datasets/12526 (Foydalanishga topshirilgan shifoxonalar)ni CSV faylda yuklab oling.
# Ushbu faylni o'qib, ekranga chiqaradigan dastur tuzing.
'''
import csv

with open('info.csv', encoding="utf8") as f:
    read = csv.reader(f)
    for line in read:
        print(line)  '''

# 2-topshiridagi CSV faylni o'qib, 2012-2017-yillarda oralig'ida jami eng ko'p kasalxonalar qurilgan 3ta viloyatni
# ekranga chiqaradigan dastur tuzing.
'''
import csv

new_list = list()
with open('info.csv', encoding="utf8") as f:
    for my_info in csv.DictReader(f, delimiter=";"):
        a = dict(my_info)
        a['2012'] = int(a['2012'])
        a['2013'] = int(a['2013'])
        a['2014'] = int(a['2014'])
        a['2015'] = int(a['2015'])
        a['2016'] = int(a['2016'])
        a['2017'] = int(a['2017'])
        c = a['Hududlar']
        a['barchasi'] = a['2012'] + a['2013'] + a['2014'] + a['2015'] + a['2016'] + a['2017']
        if a['Hududlar'] != 'O`zbekiston Respublikasi':
            new_list.append(a)
print("2012-2017-yillar oralig'ida jami eng ko'p kasalxonalar qurilgan hududlar:")
result = sorted(new_list, key=lambda my_info: my_info["barchasi"], reverse=True)[:3]
for my_info in result:
    print(my_info["Hududlar"], my_info["barchasi"]) '''

# float_range nomli generator yarating.
# range kabi ishlasin, lekin 3-argumenti (step) float qabul qila olsin.

# chunki range(0, 2, 0.5) ishlamaydi

# for i in float_range(0, 2, 0.5):
#   print(i)

# 0
# 0.5
# 1.0
# 1.5

'''
import decimal
import time


def float_range(x, y, step):
    while x < y:
        time.sleep(1)
        yield float(x)
        x += decimal.Decimal(step)


for a in float_range(0, 2, 0.5):
    print(a)  '''

# log nomli dekorator yarating, u qaysi funksiya qachon chaqirilganini va qachon funksiya tugagani vaqtnini ekranga
# chiqarsin. Vaqtni formatlashni https://strftime.org/ saytidan ko'rishingiz mumkin. Misol: @log def hello(): print(
# "hello")

# hello()

# Output:
# - called function: hello at 8:43:35
# hello
# - finished function: hello at 8:43:36

'''import time


def log(func):
    def inner():
        print('called function: ' + time.strftime('%X'))
        func()
        print('finished function' + time.strftime('%X'))
    return inner


@log
def hello():
    print('Hello')


hello()
'''

# log nomli kontekst meneger yarating, u qaysi kontext qachon ochilganini va qachon  kontext yopilganini vaqtnini
# ekranga chiqarsin.
#
# Misol:
#
# with log():
#      print("hello")
#
# Output:
# - context manager opened at 8:43:35
# hello
# - context manager closed at 8:43:36


'''import time
from contextlib import contextmanager


@contextmanager
def log(file_name, mode):
    file = open(file_name, mode)
    print("Opened file " + 'at ' + time.strftime('%X'))
    try:
        yield file
    finally:
        file.close()
        print('closed file ' + 'at ' + time.strftime('%X'))


with log('file.txt', 'w') as file:
    print('file', file)

    raise Exception'''

# Standart kutubxonadagi "calendar"dan foydalanib, 2022-yilning kalendarini ekranga chiqaring.
'''import calendar
year = 2022

print(calendar.calendar(year))'''

# Standart kutubxonadagi "bisect" dan foydalanib quyidagi masalani yeching.

# 0-100 oraligidagi sonni foydalanuvchidan qabul qilib, Ekranga o'quvchini bahosini chiqaradigan dastur tuzing.
# "If" dan foydalanish mumkin emas.

# 0-20 -> 1
# 21-40 -> 2
# 41-65 -> 3
# 66-85 -> 4
# 86-100 -> 5

'''from bisect import bisect

grades = [0, 20, 40, 65, 85, 100]
grades_str = '12345'
grade = int(input('Enter grade: '))
print(bisect(grades, grade))'''

# pip orqali "requests" kutubxonasini kompyuteringizga o'rnatib,
# "http://iamawesome.com" ga GET request jo'natib, natijani ekranga chiqaring.

'''import requests

response = requests.get('http://iamawesome.com')
print(response.status_code)'''

# sqlite base da jadval yaratish usuli
'''
 from sqlite3 import connect


with connect("contacts.db") as db:
    cursor = db.cursor()
    cursor.execute(                                 
        """
        CREATE TABLE IF NOT EXISTS contacts(
            first_name VARCHAR,
            last_name VARCHAR,
            phone_number VARCHAR
        ) 
        """
    )
    '''

