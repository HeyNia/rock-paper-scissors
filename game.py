import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = int(input())

if your_choice >= 0 and your_choice <=2:
    print("You chose")
    if your_choice == 0:
        print(f"rock {rock}")
    elif your_choice == 1:
        print(f"paper {paper}")
    else:
        print(f"scissors {scissors}")



    computer_choice = random.randint(0, 2)

    print("computer  chose")

    if computer_choice == 0:
        print(f"rock {rock}")
    elif computer_choice == 1:
        print(f"paper {paper}")
    else:
        print(f"scissors {scissors}")
else:
        print("INVALID CHOICE")



if your_choice == computer_choice:
    print("Draw!")
elif your_choice == 0 and  computer_choice == 2:
    print("You win!")
elif your_choice == 1 and  computer_choice == 0:
    print("You win!")
elif your_choice == 1 and  computer_choice == 2:
    print("You win!")
else:
    print("You loose!")

