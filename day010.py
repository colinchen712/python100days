from time import sleep

def clear_screen():
    print("\n" * 100)

# def together(name,surname):
#     return (name +" "+surname).title()
# output = together("AaBbccd","1324567")
# print(output)
#

# final_number = 0
# go = 1
# number1 = int(input("1.        "))
# operator = input("运算符号  ")
# number2 = int(input("2.        "))
# while True:
#     def count(operator,final_number,number1,number2):
#         if operator == "*":
#             final_number = number1 * number2
#         elif operator == "/":
#             final_number = number1 / number2
#         elif operator == "+":
#             final_number = number1 + number2
#         elif operator == "-":
#             final_number = number1 - number2
#         else:
#             clear_screen()
#             print("?")
#             sleep(1)
#             operator = input("运算符号  ")
#         print(f"{number1}{operator}{number2} = {final_number}")
#         return final_number
#
#     final_number = (count(operator,final_number,number1,number2))
#     go = input("go ?   ")
#     if go == "yes":
#         go = 1
#         number1 = final_number
#         print(f"number1 = {number1}")
#         operator = input("运算符号  ")
#         number2 = int(input("2.        "))
#     else:
#         go = 0
#         number1 = int(input("1.        "))
#         operator = input("运算符号    ")
#         number2 = int(input("2.        "))






# def add(number1,number2):
#     return number1 + number2
#
# def less(number1,number2):
#     return number1 - number2
# def double(number1,number2):
#     return number1 * number2
# def deside(number1,number2,is_countinue):
#     if number2 != 0:
#         return number1 / number2
#     else:
#         return number1 / 1
#
#
# is_countinue = True
#
# number1 = int(input("1.        "))
#
# while is_countinue :
#
#     operator = input("运算符号  ")
#     number2 = int(input("2.        "))
#
#     if operator == "*":
#         final_number = double(number1,number2)
#     elif operator == "/":
#         final_number = deside(number1,number2,is_countinue)
#     elif operator == "+":
#         final_number = add(number1,number2)
#     elif operator == "-":
#         final_number = less(number1,number2)
#     print(f"{number1}{operator}{number2} = {final_number}")
#     go = input("go ?   ")
#
#     if(go != 'y'):
#         is_countinue = False
#     else:
#         number1 = final_number

def add(n1,n2):
    return n1+n2
def substance(n1,n2):
    return n1-n2
def double(n1,n2):
    return n1*n2
def devide(n1,n2):
    return n1/n2


n1 = input("1.    ")
operator = input("      ")
n2 = input("2.    ")

































