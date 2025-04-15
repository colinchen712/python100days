import random
from time import sleep


def clear_screen():
    print("\n" * 100)

card_list = ['a',2,3,4,5,6,7,8,9,10,10,10,10]

you_card = []
you_point = 0
computer_card = []
computer_point = 0

start_game = input("你要开始游戏吗？")
if start_game == "否" or start_game == "不" or start_game == "不要" or start_game == "no" or start_game == "No":
    exit("...")
else:
    start_game = "yes"
    clear_screen()
start_game = "yes"
for a in range(2):
    random_number = random.randint(0, 9)
    if random_number == 0:
        if you_point < 11:
            you_card.append(11)
            you_point += 11
        else:
            you_card.append(1)
            you_point += 1
    else:
        you_point += (random_number + 1)
        you_card.append(card_list[random_number])
    if computer_point < 17:
        random_number = random.randint(0, 9)
        if random_number == 0:
            if computer_point < 11:
                computer_card.append(11)
                computer_point += 11
            else:
                computer_card.append(1)
                computer_point += 1
        else:
            computer_point += (random_number + 1)
            computer_card.append(card_list[random_number])
print("你有"+str(you_card)+"你现在的点数是"+"[ "+str(you_point)+" ]")
print("电脑的第一张牌是" + "[ "+str(computer_card[0])+" ]")
while start_game == "yes":
    random_number = random.randint(0, 9)
    new_card = input("你要新的牌吗？")
    if new_card == "否" or new_card == "不" or new_card == "不要" or new_card == "no" or new_card == "No":
        new_card = "no"
        if you_point > computer_point:
            print("你赢了，干得漂亮!!!")
            sleep(2)
        elif you_point == computer_point:
            print("平局...")
            sleep(2)
        else:
            print("你输了...")
            sleep(2)
        start_game = input("你要开始游戏吗？")
        if start_game == "否" or start_game == "不" or start_game == "不要" or start_game == "no" or start_game == "No":
            exit("...")
        else:
            start_game = "yes"
            you_card = []
            you_point = 0
            computer_card = []
            computer_point = 0
            clear_screen()
            for a in range(2):
                random_number = random.randint(0, 9)
                if random_number == 0:
                    if you_point < 11:
                        you_card.append(11)
                        you_point += 11
                    else:
                        you_card.append(1)
                        you_point += 1
                else:
                    you_point += (random_number + 1)
                    you_card.append(card_list[random_number])
                if computer_point < 17:
                    random_number = random.randint(0, 9)
                    if random_number == 0:
                        if computer_point < 11:
                            computer_card.append(11)
                            computer_point += 11
                        else:
                            computer_card.append(1)
                            computer_point += 1
                    else:
                        computer_point += (random_number + 1)
                        computer_card.append(card_list[random_number])
            print("你有" + str(you_card) + "你现在的点数是" + "[ " + str(you_point) + " ]")
            print("电脑的第一张牌是" + str(computer_card[0]))
    else:
        new_card = "yes"
    clear_screen()
    if new_card == "yes":
        if random_number == 0:
            if you_point < 11:
                you_card.append(11)
                you_point += 11
            else:
                you_card.append(1)
                you_point += 1
        else:
            you_point += (random_number+1)
            you_card.append (card_list[random_number])
    print("你有"+str(you_card)+"你现在的点数是"+"[ "+str(you_point)+" ]")
    if you_point == 21:
        print("你赢了，干得漂亮!!!")
        sleep(2)
        clear_screen()
        start_game = input("你还想再玩一局吗？")
        if start_game == "否" or start_game == "不" or start_game == "不想" or start_game == "no" or start_game == "No":
            exit("...")
        else:
            start_game = "yes"
            you_card = []
            you_point = 0
            computer_card = []
            computer_point = 0
            for a in range(2):
                random_number = random.randint(0, 9)
                if random_number == 0:
                    if you_point < 11:
                        you_card.append(11)
                        you_point += 11
                    else:
                        you_card.append(1)
                        you_point += 1
                else:
                    you_point += (random_number + 1)
                    you_card.append(card_list[random_number])
                if computer_point < 17:
                    random_number = random.randint(0, 9)
                    if random_number == 0:
                        if computer_point < 11:
                            computer_card.append(11)
                            computer_point += 11
                        else:
                            computer_card.append(1)
                            computer_point += 1
                    else:
                        computer_point += (random_number + 1)
                        computer_card.append(card_list[random_number])
            print("你有" + str(you_card) + "你现在的点数是" + "[ " + str(you_point) + " ]")
            print("电脑的第一张牌是" + str(computer_card[1]))
            clear_screen()
    if you_point > 21:
        print("你输了...")
        sleep(2)
        clear_screen()
        start_game = input("你还想再玩一局吗？")
        if start_game == "否" or start_game == "不" or start_game == "不想" or start_game == "no" or start_game == "No":
            exit("...")
        else:
            start_game = "yes"
            you_card = []
            you_point = 0
            computer_card = []
            computer_point = 0
            for a in range(2):
                random_number = random.randint(0, 9)
                if random_number == 0:
                    if you_point < 11:
                        you_card.append(11)
                        you_point += 11
                    else:
                        you_card.append(1)
                        you_point += 1
                else:
                    you_point += (random_number + 1)
                    you_card.append(card_list[random_number])
                if computer_point < 17:
                    random_number = random.randint(0, 9)
                    if random_number == 0:
                        if computer_point < 11:
                            computer_card.append(11)
                            computer_point += 11
                        else:
                            computer_card.append(1)
                            computer_point += 1
                    else:
                        computer_point += (random_number + 1)
                        computer_card.append(card_list[random_number])
            print("你有" + str(you_card) + "你现在的点数是" + "[ " + str(you_point) + " ]")
            print("电脑的第一张牌是" + str(computer_card[1]))
            clear_screen()
    sleep(0.8)
    if computer_point < 17:
        random_number = random.randint(0, 9)
        if random_number == 0:
            if computer_point < 11:
                computer_card.append(11)
                computer_point += 11
            else:
                computer_card.append(1)
                computer_point += 1
        else:
            computer_point += (random_number+1)
            computer_card.append(card_list[random_number])
    print("电脑的第一张牌是"+str(computer_card[0]))










































