#
import random
from random import shuffle
from time import sleep

#
# Task1 a practice
#
# student_heights = input("Input a list of student heights\n").split()
# for n in range(0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# length = len(student_heights)
# total_height = 0
# for w in student_heights:
#     total_height += w
# average = total_height/length
#
# print (round(average,1))
#
# # Task2 a practice too
#
# student_score = input("Input a list of student score\n").split()
# for z in range(0,len(student_score)):
#     student_score[z] = int(student_score[z])
#
# biggest = 0
# for z in student_score:
#     if biggest < z :
#      biggest = z
#
# print(biggest)

#Task3 also a practice
#方案1
# n = 0
# for k in range(1,51):
#     n += 2*k
# print(n)
# #方案2
# nn = 0
# for kk in range(2,101,2):
#     nn += kk
#     print(nn)
print('''...................................................
...................................................
...................................................''')

# #Task3  a practice ...
# for s in range(1,101):
#     if (s % 3 == 0) and (s % 5 == 0):
#         print("FizzBuzz")
#     elif s % 3 == 0:
#         print("Fizz")
#     elif s % 5 == 0:
#         print("Buzz")
#     else:
#         print(s)
#
# #Task4 a practice......
# password = []
# letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# numbers = ["0","1","2","3","4","5","6","7","8","9"]
# symbols = ["~","!","@","#","$","%","^","&","*","(",")","_","+"]
# let = int(input("How many letters would you like in you password?\n"))
# num = int(input("How many numbers would you like in you password?\n"))
# sym = int(input("How many symbols would you like in you password?\n"))
# for l in range(0,let):
#     ran1 = random.randint(1,len(letters)+1)
#     password += letters[ran1]
# for n in range(0,num):
#     ran2 = random.randint(1,11)
#     password += numbers[ran2]
# for s in range(0,sym):
#     ran3 = random.randint(1,len(symbols)+1)
#     password += symbols[ran3]
# password = shuffle(password)
# # print(password)
#
#
#
# password = ''
# password_list = [ ]
# letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# numbers = ["0","1","2","3","4","5","6","7","8","9"]
# symbols = ["~","!","@","#","$","%","^","&","*","(",")","_","+"]
# let = int(input("How many letters would you like in you password?\n"))
# num = int(input("How many numbers would you like in you password?\n"))
# sym = int(input("How many symbols would you like in you password?\n"))
# for n in range(0,let):
#     password_list.append(random.choice(letters))
# for n in range(0,num):
#     password_list.append(random.choice(numbers))
# for n in range(0,sym):
#     password_list.append(random.choice(symbols))
# random.shuffle(password_list)
# for a in password_list:
#     password += a
# print(f"You password is {password}")







password =[]
ppp = ''
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["~","!","@","#","$","%","^","&","*","(",")","_","+"]
let = int(input("How many letters would you like in you password?\n"))
num = int(input("How many numbers would you like in you password?\n"))
sym = int(input("How many symbols would you like in you password?\n"))
for a in range(0,let):
    password.append(random.choice(letters))
for a in range(0,num):
    password.append(random.choice(numbers))
for a in range(0, sym ):
    password.append(random.choice(symbols))
random.shuffle(password)
for e in password:
    ppp += e
print(f"you password is {ppp}")
























