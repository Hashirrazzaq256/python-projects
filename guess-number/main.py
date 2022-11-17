import random
print("welcome to guessing game")
actual_number = random.randint(1,50)*2
total_atempts = 0
difficulty = input("Choose difficulty level easy or hard ").lower()
if difficulty == 'easy':
  total_atempts = 10
else:
  total_atempts = 5
while total_atempts > 0:
  user_guess = int(input("Guess a number between 1 to 100 \n"))
  if user_guess>actual_number:
    print("Too high")
    total_atempts = total_atempts-1
    print(f"you have {total_atempts} left")
  elif user_guess < actual_number:
    print("Too low")
    total_atempts = total_atempts-1
    print(f"you have {total_atempts} left")
  elif user_guess== actual_number:
    print("HAA You Got IT")
    
    
