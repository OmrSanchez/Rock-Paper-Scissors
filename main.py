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

#Write your code below this line 👇
import random

# Gameplay
rps = [rock, paper, scissors]

# Input validating based upon user input
user_choice = -1
while user_choice < 0 or user_choice >= 3:
    try:
        user_choice = int(input("What do you choose? Press 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
        if user_choice < 0 or user_choice >= 3:
            print("Invalid choice. Please enter 0, 1, or 2.")
    except ValueError:
        print("Invalid input. Please eneter a valid integer.")

npc_choice = random.randint(0,2)
user_final = rps[user_choice]
npc_final = rps[npc_choice]

# Determining Outcome
if user_choice == npc_choice:
    print(f'You chose: {user_choice}.\n{user_final}')
    print(f'NPC chose: {npc_choice}. \n{npc_final}')
    print('DRAW...')
elif user_choice == 0 and npc_choice == 2:
    print(f'You chose: {user_choice}.\n{user_final}')
    print(f'NPC chose: {npc_choice}. \n{npc_final}')
    print('You Win!')
elif user_choice == 0 and npc_choice == 1:
    print(f'You chose: {user_choice}.\n{user_final}')
    print(f'NPC chose: {npc_choice}. \n{npc_final}')
    print('You Lose.')
elif user_choice == 1 and npc_choice == 0:
    print(f'You chose: {user_choice}.\n{user_final}')
    print(f'NPC chose: {npc_choice}. \n{npc_final}')
    print('You Win!')
elif user_choice == 1 and npc_choice == 2:
    print(f'You chose: {user_choice}.\n{user_final}')
    print(f'NPC chose: {npc_choice}. \n{npc_final}')
    print('You Lose.')
elif user_choice == 2 and npc_choice == 0:
    print(f'You chose: {user_choice}.\n{user_final}')
    print(f'NPC chose: {npc_choice}. \n{npc_final}')
    print('You Lose.')
elif user_choice == 2 and npc_choice == 1:
    print(f'You chose: {user_choice}.\n{user_final}')
    print(f'NPC chose: {npc_choice}. \n{npc_final}')
    print('You Win!')




# Print to test
# print(user_choice)
# print(user_final)
# print(npc_final)
