import random
from day007_01 import word_list

the_word = random.choice(word_list)
word = []
correct_number = 0
lives = 6
#print(the_word)

for a in range(len(the_word)):
    word.append('_')
while not lives == 0:
    guess = input("Guess a letter: ").lower()
    if guess not in the_word:
        lives -=1
    print(str(lives)+ "❤")
    for position in range(len(the_word)):
        if word[position] == "_":
            if the_word[position] == guess:
                word[position] = guess
                correct_number += 1
                if correct_number == len(the_word):
                    exit("you win")

    print(word)
if lives == 0:
    exit(" you lost!!!\n")














































