import math
from curses.ascii import isalpha
from time import sleep

# parameter = input("What's you name?")
#
# def greet(argument):
#     print(f"hello {argument}")
#     print("...")
#     print(f"bye {argument}")
#
# greet(parameter)
# number1 = int(input("a number\n"))
# number2 = int(input("a number\n"))
# def addd(b,a):
#     print(a ** b)
# addd(a = number1,b = number2)
#
# height = float(input("Height    "))
# width = float(input("Width    "))
# coverage = 5
# def calculate(a,b,c):
#     print(math.ceil((a*b/c)**1.05))
# calculate(a = height,b = width,c = coverage)
#
#
#
# number = int(input("A Number!!!!!!        "))
# def prime(a):
#     if a == 2 or a == 3 or a == 5:
#         print("It's a prime number!")
#     elif  (a % 2 != 0) and (a % 3 != 0) and (a % 5 != 0):
#         print("It's a prime number!")
#     else:
#         print("It's not a prime number!")
# prime(a = number)
#
#
#
#

letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
again = "yes"
text = input("The message what you wants...          ").lower()
distance = int(input("The distance that you want to move about you message\n                                       "))

def encryption(text, distance, letter):
    direction = input("The direction...      <--  or  -->     ")
    print(f"[  {text}  ]")
    answer = ''
    for a in text:
        if a.isalpha():
            number = letter.index(a)
            if direction == "<--" or direction == "<-" or direction == "<":
                answer += (letter[((number - distance) % 26)])
            else:
                answer += (letter[((number + distance)) % 26])
        else:
            answer += a
    for aa in range(6):
        sleep(0.3)
        print(".",end = '')
    print(f"\n[  {answer}  ]")
while not again == "no":
    encryption(text,distance,letter)
    again = input("Do you want to play again?        Yes  or  No \n                                       ").lower()

    if again == "no":
        sleep(0.3)
        print("B", end = '')
        sleep(0.1)
        print("y", end='')
        sleep(0.1)
        print("e", end='')
        sleep(0.3)
        print(".", end='')
        sleep(0.2)
        print(".", end='')
        sleep(0.2)
        exit(".")
    text = input("The message what you wants...          ").lower()
    distance = int(input("The distance that you want to move about you message\n                                       "))
# #
#
#
#
# def caesar(text,distance):
#     direction = input("The direction...      <--  or  -->     ")
#     end_text = ""
#     if direction == "<--" or direction == "<-" or direction == "<":
#         distance *= -1
#     for lel in text:
#         number = letter.index(lel)
#         new_number = number + distance
#         end_text += letter[new_number]
#     print(end_text)
#
#
#
# caesar(text,distance)










































































