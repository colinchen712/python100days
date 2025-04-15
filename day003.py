import random


# #Task 1 if , else
# #A_number
# number=int(input("A number "))
#
# if number > 10000000:
#     print("A big number !!!")
# else:
#     print("Thank you...")
# #string
# strip=input("A word ")
#
# if strip == "A word":
#     print("Good !!!")
# else:
#     print("...")
# #bool
# boo=input("True or False ")
#
# if boo == 'True':
#     print("Yes,it's true")
# elif boo == 'False':
#     print("Oh no !?")
#     print("Why!!!")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #Task 2 even or odd

# That_number=input("Write a number please---> ")
# if int(That_number) % 2==0:
#     print("A even number...")
# # else:
# #     print("A odd number...")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # #Task 3 many options

# print("Welcome to the questions game!!!")
# name=input("So,What's you name? ")
# color=input(f"Ok,{name},so,which color do you prefer?Red or Blue ")
# if color == "Red":
#     fruit=input("Good,and which fruit do you like?Choose one...\n""Watermelon    Apple    Banana    Milk ")
#     if fruit == "Watermelon":
#         print("Wow!!! You get a Red Watermelon!!! That's so nice!")
#     elif fruit == "Apple":
#         eat=input("A Red Apple...\nVery good,very good...\nDo you want eat it? ")
#         if eat == "Yes":
#             print("That's nice...")
#         else:
#             print("Ok...")
#     elif fruit == "Banana":
#         print("Oh my god!!?\nWhat are you think about!?\nA Red Banana!!!")
#     elif fruit == "Milk":
#         print("ok...ok...Everyone think a milk is a fruit...\nYou lost!!!!!!!!! ")
#     else:
#         print("You lost!!!!!!!!!!")
# elif color == "Blue":
#     pet=input("Nice,I like it...\nDo you want have a cat or have a dog? ")
#     if pet == "dog":
#         print("A blue dog,so interesting...")
#     else:
#         print("A blue cat,I think it must cute...")
# else:
#     print("...")
# print("Bye...")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #Task4 BMI
#
# height=float(input("Your height in m:"))
# weight=float(input("your weight in kg:"))
# bmi=round(weight/height**2,2)
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("normal")
# elif bmi < 30:
#     print("overweight")
# elif bmi <= 35:
#     print("obese")
# else :
# #     print("clinically obese")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #Task5 Leap year !
#
# year=int(input("years "))
# if year % 100 ==0:
#     if year % 400 ==0:
#         print("Leap year")
#     else:
#         print("a normal year...")
# elif year %4 ==0:
#     print("Leap year")
# else:
#     print("A normal year...")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #Task6 practice about pizza...

# print("Welcome to the pizza shop...")
# size=int(input("Which size of pizza do you want? "))
# pepperoni=input("Ok,so do to want to add the pepperoni? ")
# cheese=input("Good,do you want extra cheese...\n")
#
# if size < 5:
#     print("Sorry,its too small...")
# elif size > 15:
#     print("That's so big...")
# else:
#     if pepperoni == "no":
#         print("...")
#     else:
#         size=(size+3)
#     if cheese == "no":
#         print(...)
#     else:
#         size=(size+1)
# print(f"you need pay {size} $")
#
#
# print("Welcome to the pizza shop...")
# size=input("Which size of pizza do you want? small  middle  big ")
# pepperoni=input("Ok,so do to want to add the pepperoni? ")
# cheese=input("Good,do you want extra cheese...\n")
# if size == "small":
#     money=15
#     if pepperoni == "no":
#         print("...")
#     else:
#         money=(money+2)
# elif size == "middle":
#     money=20
#     if pepperoni == "no":
#         print("...")
#     else:
#         money = (money + 3)
# elif size == "big":
#     money=25
#     if pepperoni == "no":
#         print("...")
#     else:
#         money = (money + 3)
# else:
#     money=-9999999999
#     print("...")
#
#
# if cheese == "no":
#     print("...")
# else:
#     money=(money+1)
# money=print(f"you need pay {money} $")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Task7 practice about "ture love"
#
# name1 = input("Please enter your name...\n")
# name2 = input("Please enter your spouse's name...\n")
# name1 = name1.lower()
# name2 = name2.lower()
# both_name = name1 + name2
# t = (both_name.count("t"))
# r = (both_name.count("r"))
# u = (both_name.count("u"))
# e = (both_name.count("e"))
# name_ture = ((t + r + u + e) * 10)
#
# l = (both_name.count("l"))
# o = (both_name.count("o"))
# v = (both_name.count("v"))
# ee = (both_name.count("e"))
# name_love = (l + o + v + ee)
# total_love = (name_ture + name_love)
# if total_love < 10 or total_love > 90:
#     print(f"your score is {total_love},you go together like coke and mentos.")
# elif 50 >= total_love >= 40:
#     print(f"your score is {total_love},you are alright together.")
# else:
#     print(f"Your scare is {total_love}")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Task8 冒险岛
#
#
#
#
print("欢迎来的冒险岛,你的目标是找到宝藏！")
side=input("现在，你刚刚来到这座神秘的岛屿...\n你决定探索一番，你要往 <--左边  还是  右边-->\n")
if side == "左边" or side == "左":
    exit("你决定先去左边探索一番，然而，幸运女神没有站在你这边...\n很不幸，你遇到了一个巨大的怪兽!!?\n它咆哮的冲向了你!!!\n...\n...\n\n你寄了...")
elif side == "右边" or side == "右":
    穿过湖面的方式 = input("你来到了一个湖边，湖面波光粼粼，看起来很是美丽...\n冥冥中的直觉告诉你，宝藏就在对岸，你得想办法穿过湖...\n湖很大，绕过去是不切实际的...\n好在，湖的周围有很多树，也许你可以 制作木筏 来到达对岸...\n湖看起来不深，也许你可以试着 游过去 ...\n")
    if  穿过湖面的方式 == "制作木筏":
        湖面之后 = input("出于谨慎，你打消了游过去的想法...\n经过几个小时的努力，你制作了一个看起来不太豪华的木筏，好在，它足够坚固:）\n你脚踏木筏，在波澜壮阔的湖面上自由“航行”，过了一会，你成功踏上了对岸...\n与湖另一边的生机盎然不同，这里更加荒凉...\n你看了看周围的环境，前方有一个山洞...\n你要 继续前进  还是  进入山洞\n")
    elif 穿过湖面的方式 == "游过去":
        游过去的概率 = int(random.randint(1,3))
        if 游过去的概率 == 1:
           print("你鼓起勇气，向着湖对岸游去，好在，水不深...\n过了会，你成功到达了对岸...\n太阳很暖和，水也不冷，你并没有感觉到不适...\n\n与湖另一边的生机盎然不同，这里更加荒凉...\n你看了看周围的环境，前方有一个山洞...\n你要 继续前进  还是  进入山洞\n")
        else:
            湖面之后 = input("你鼓起勇气，向着湖对岸游去，好在，水不深，一切看起来很正常...\n...\n...\n哦～不！糟糕！就在你游到湖中央的时候，一股巨大的吸力传来！！！\n你不受控制的被这股吸力拉入水下，恐慌和绝望在你心头蔓延，湖水像利刃一样撕扯着你那脆弱的身躯!\n然而，更致命的是氧气的匮乏，你的意识渐渐模糊，在混乱之中，你似乎看到了一丝光亮...\n...\n你寄了...")
    else:
        exit("?")
else:
    exit("?")
while not  湖面之后 == "继续前进" or 湖面之后 == "继续" or 湖面之后 == "前进" or 湖面之后 == "进入山洞" or 湖面之后 == "进入" or 湖面之后 == "山洞":
    if 湖面之后 == "继续前进" or 湖面之后 == "继续" or 湖面之后 == "前进":
        input("你摇了摇的，决定继续前进，过了一会，你在前方发现了一个有些破旧的祭坛...\n周围的石块不规则的摆放着，位于中间的一座石台吸引了你的目光...\n你摸了摸位于中央的石台，隐约间，你进入了一种奇妙至极的状态...\n你的意识无比清新，周围的一切似乎都变得不一样了，你毫不费力的以一种难以描述的方式感知到了周围的环境...\n一丝冰凉的能量透过石台传入了你的手中...\n你感觉你的灵魂仿佛在升华...\n接下来会发生什么？")
    elif 湖面之后 == "进入山洞" or 湖面之后 == "进入" or 湖面之后 == "山洞":
        input("抱着好奇心，你进入了山洞...")
    else:
        湖面之后 = input("? \n")






























