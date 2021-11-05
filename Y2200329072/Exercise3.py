import random
Number= random.randint(0,101)
user_number = int(input("Enter the guessed number: "))
           
if (user_number < number):
     print("-> increase your number")
else:
     print("-> decrase your number")