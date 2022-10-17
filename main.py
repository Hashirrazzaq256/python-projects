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

#Write your code below this line 👇
array = [rock,paper,scissors]
choice = int(input("choose 0 for rock , choose 1 for paper , choose 2 for scissors"))
if choice == 0:
  print(f" you chose rock\n {rock}")
  comp = random.randint(0,len(array)-1)
  print(f" computer chose \n {array[comp]}")
  if comp == 2:
    print("you lost")
  elif comp == 1:
    print("you won")
  else:
    print("match tied")
elif choice == 1:
  print(f"you chose paper\n {paper}")
  comp = random.randint(0,len(array)-1)
  print(f"computer chose \n {array[comp]}")
  if comp == 2:
    print("you lost")
  elif comp == 1:
    print("match tied")
  else:
    print("you won")
else:
  print(f"you chose scissors:\n {scissors}")
  comp = random.randint(0,len(array)-1)
  print(f"computer chose \n {array[comp]}")
  if comp == 2:
    print("match tied")
  elif comp == 1:
    print("you won")
  else:
    print("you lost")
