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
options = ['rock', 'paper', 'scissors']
ascii = [rock, paper, scissors]

# What do you choose? (0) Rock (1) Paper (2) Scissors)
prompt = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

choice = options[prompt]
print(ascii[prompt])

computer = random.randint(0,2)
print(f"Computer chose {options[computer]}\n{ascii[computer]}")

if prompt == computer:
  print("It's a draw")
elif (prompt == 0 and computer == 2) or (prompt == 2 and computer == 1) or (prompt == 1 and computer == 0):
    print(f"You win! {options[prompt]} beats {options[computer]}")
else: 
    print(f"You lose! {options[computer]} beats {options[prompt]}")