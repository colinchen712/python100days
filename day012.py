import random



def clear_screen():
    print("\n" * 100)



again = 1
print("Welcome to the game!")
while again == 1:
    again = 1
    life = input("Hard or Easy    ")
    if life == "Hard" or life == "hard":
        life = 5
    else:
        life = 10
    random_number = random.randint(1, 100)
    print(random_number)
    while not life == 0:
        guess = int(input("Guess a number!   [1-100]  "))
        if guess == random_number:
            print("You win !")
        elif guess < random_number:
            print("Too small!")
            life -= 1
        elif guess > random_number:
            print("Too big!")
            life -= 1

        print(f"You still have [ {life} ] life...")

        if life == 0:
            again = input("You lost! \nDo you want to play again?    ")
            if again == "no":
                exit("!!!")
            else:
                again = 1
        elif guess == random_number:
            again = input("Do you want to play again?    ")
            if again == "no":
                exit("!!!")
            else:
                again = 1
                clear_screen()

















