import random

from game_data import *
# 1  Display art (I don't need it...)




def clean_screan():
    for _ in range(100):
        print("\n")


def check_answer(guess,follower_count1,follower_count2):
    if follower_count1 > follower_count2:
        return guess == "a"
    else:
        return guess == "b"

point = 0
# 2  Generate a random account from the game data.
play_game = True
clean_screan()

random_number2 = random.choice(data)

while play_game:
    random_number1 = random_number2
    random_number2 = random.choice(data)

    while random_number1 == random_number2:
        random_number2 = random.choice(data)


    # 3  Format the account data into printable format.
    print(f"Name [ {random_number1['name']} ]    Follower_count [ {random_number1['follower_count']} ]    Description [ {random_number1['description']} ]    Country [ {random_number1['country']} ]")
    print("\n\nVS\n\n")
    print(f"Name [ {random_number2['name']} ]    Follower_count [ ??? ]    Description [ {random_number2['description']} ]    Country [ {random_number2['country']} ]")

    # 4  Ask user for a guess.

    guess = input("A or B                 ").lower()

    clean_screan()
    # 5 and 6----- Check the answer.---------- Give user the feedback on their guess.
    is_correct= check_answer(guess, random_number1['follower_count'], random_number2['follower_count'])
    if is_correct:
        print("Nice!")
        point += 1
    else:
        play_game = False
    print(f"You point is [ {point} ]")
    if play_game == False:
        exit("You lost!!!")


# 7  Score keeping.

# 8  Let game can start again.



# 9  position B  become  position A.

# 10 Clear the screen.





































































































































































