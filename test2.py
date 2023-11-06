pi = 3.14159

print(pi)

# string = input("문자열을 읿력하세요")

# print(string)

num1 = 5.9
num2 = 5.99999999999999999999

num1 = int(num1)
num2 = int(num2)

print(num1, num2, sep='\n')

import math

num4 = int(5.99999999999999999999)
print(num4, "num4")

a = str(10)
print(type(a))

# b = "{}".format(10.34)
name = "bob"
answer = "yes"
b = f"{name} is cool? {answer}"
print(type(b))

print(b)

import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))
now.year


print("{} sv".format(now.year))



if 0:
    print("0 is True")
else:
    print("0 is False")

if "":
    print("\"\" is True")
else:
    print("\"\" is False")

my_list = [1, 2, 3, 4, 5]

# Remove and return the last element
popped_element = my_list.pop()

print("Popped Element:", popped_element)
print("Updated List:", my_list)

import os

# 환경 변수에 접근
home_directory = os.environ["HOME"]
user_name = os.environ["USER"]

# 환경 변수 출력
print(f"홈 디렉토리: {home_directory}")
print(f"사용자 이름: {user_name}")
print(os.environ)

