import random
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
outcome = [rock,paper,scissors]
printer = ["Rock", "Paper", "Scissors"]
choice = int(input('''Enter your choice
0 for Rock
1 for Scissors
2 for Paper'''))
print(f"You choose {printer[choice]}'\n{outcome[choice]}")



comp_choice = random.randint(0,2)
print(f"computer choose {printer[comp_choice]} '\n{outcome[comp_choice]}")
if choice == comp_choice:
  print("Draw")
elif choice ==0 and comp_choice==1:
  print("You win")
elif choice == 1 and comp_choice==2:
  print("You win")
elif choice == 2 and comp_choice==0:
  print("You win")
else:
  print("Computer wins")

