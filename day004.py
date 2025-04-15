# #Task1 random.
# #一种随机数
import random
from os.path import split

# random_int = random.randint(0,100)
# print(random_int)
# #另一种随机数
# random_float = random.random()
# print(random_float*100)

#Task2 Head or tail about coin

# coin_side = random.randint(0,1)
# if coin_side == 1:
#     print("head")
# else:
#     print("tail")

#Task3 List
#
# their_name = input("5 people... \nlike Alic lfd coco\n")
# who = random.randint(0,4)
# that_people = their_name.split(" ")[who]
# print(f"{that_people} need pay the bill!")
#
#Task4 practice  [a game]
#
# row1 = ["O","O","O"]
# row2 = ["O","O","O"]
# row3 = ["O","O","O"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = int(input("where do you want to put the treasure?\n"))
# if position == 11:
#     row1 = ["X","O","O"]
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == 12:
#      row1 = ["O","X","O"]
#      print(f"{row1}\n{row2}\n{row3}")
# elif position == 13:
#      row1 = ["O","O","X"]
#      print(f"{row1}\n{row2}\n{row3}")
# else:
#     print("...")
# if position == 21:
#     row2 = ["X","O","O"]
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == 22:
#      row2 = ["O","X","O"]
#      print(f"{row1}\n{row2}\n{row3}")
# elif position == 23:
#      row2 = ["O","O","X"]
#      print(f"{row1}\n{row2}\n{row3}")
# else:
#     print("...")
# if position == 31:
#     row3 = ["X","O","O"]
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == 32:
#      row3 = ["O","X","O"]
#      print(f"{row1}\n{row2}\n{row3}")
# elif position == 33:
#      row3 = ["O","O","X"]
#      print(f"{row1}\n{row2}\n{row3}")
# else:
#     print("...")
#
# row1 = ["O", "O", "O"]
# row2 = ["O", "O", "O"]
# row3 = ["O", "O", "O"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("where do you want to put the treasure?\n")
# row = int(position[0])
# columm = int(position[1])
# map[row - 1][columm - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")
#
#Task5 practice  [ Rock paper scissor ]
choose = (input("What do you choose?\nrock  paper  scissor\n").lower())
computer = random.randint(0,2)
if computer == 0:
    computer = "rock"
elif computer == 1:
    computer = "paper"
elif computer == 2:
    computer = "scissor"

print(f"you choose   [{choose}]\n")
print(f"computer is   [{computer}]")
if (choose == "scissor" and computer == "[paper]") or (choose == "paper" and computer == "[rock]") or (choose == "rock" and computer == "[scissor]"):
    print("You win!")
elif choose == computer:
    print("It's diw...\nTry again...")
else:
    print("You lose!")


