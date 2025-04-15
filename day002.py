# print("hello\"")
#

# # print("122333")
#
# 你输入的数字1=input("你想输入的第一个数字")
# 你输入的数字2=input("你想输入的第二个数字")
# 两个数字相加的结果=int(你输入的数字1)+int(你输入的数字2)
# 最后的结果=(int(两个数字相加的结果)**2**3)
# print(round(最后的结果,5))
#
#
# #Task1
# print(type("hello"))
# print(type(123))
# print(type(1.12))
# print(type(True))
# print(type(False))
# print(type(3.0))


# your_name=str(len(input("your name" )))
# print("number of name is " + (your_name))

stri="good"
num=123
flo=1.23
boo=True
#转数字
# # print(int(stri))
# print(int(flo))#!
# print(int(boo))#!
# # #转字符串
# print(str(num))#!
# print(str(flo))#!
# print(str(boo))#!
# # #转浮点
# # print(float(stri))
# print(float(num))#!
# print(float(boo))#!
# # #转布尔
# print(bool(stri))#!
# print(bool(num))#!
# print(bool(flo))#!


#$Task2

# +  -
# *  /
# **

# #Task3
# score1 = 5
# score1 -=5
#
# score2 = 5
# score2 *=5
#
# score3 = 5
# score3 /=5
#
# score4 = 5
# score4 +=5
#
#
# print(score1)
# print(score2)
# print(score3)
# print(score4)
#
# #Task3
#
# score=123
# print(f"yuor score is = {score}")
#
#Task4

print("Welcome to the tip calculator!")
bill=int(input("What was the total bill "))
tip=input("How much tip would you like to gave? 5%,10%,15%,20%,25% ")
final_tip=int(tip)/100*bill
peo=input("How many people to split the bill? ")
people=int(peo)
money=round((bill+final_tip)/people,3)
print(f"Each people should pay: ${money}")
