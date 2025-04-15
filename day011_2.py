import random


card_list =[11,2,3,4,5,6,7,8,9,10,10,10,10]
player_card = []
computer_card = []
play_game = "y"
def send_card():
    for _ in range(2):
        player_card.append(random.choice(card_list))
        check_11(player_card)
        computer_card.append(random.choice(card_list))
        check_11(computer_card)
def check_11(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return cards
def check_point(play_game):
    if sum(player_card) == 21:
        print("You win!")
    elif sum(computer_card) == 21:
        print("You lost!")
    elif sum(player_card) > 21:
        print("You lost!")
    elif sum(computer_card) > 21:
        print("You win!")
    elif sum(computer_card) == sum(player_card):
        print("Draw...")
    elif sum(player_card) > sum(computer_card):
        print("You win!")
    else:
        print("You lost!")
    play_game =""
    return play_game
def game(play_game):
    send_card()
    print(f"你的牌是{player_card},加起来共有[ {sum(player_card)} ]")
    print(f"电脑的第一张牌是[ {computer_card[0]} ]")
    while play_game == "y":
        new_card = input("你还要新的牌吗？ ('y')   ")
        if new_card == "y":
            player_card.append(random.choice(card_list))
            check_11(player_card)
            print(f"你的牌是{player_card},加起来共有[ {sum(player_card)} ]")
            print(f"电脑的第一张牌是[ {computer_card[0]} ]")
            play_game = ""
        if new_card != "y":
            while not sum(computer_card) > 17:
                computer_card.append(random.choice(card_list))
                check_11(computer_card)
            check_point(play_game)
while True:
    play_game = input("你要玩游戏吗？  ")
    if play_game == "y":
        play_game = game(play_game)
        player_card = []
        computer_card = []
    else:
        exit("...")













































































