import random

money = 100

#Write your game of chance functions here
def filp_a_coin():
  global money
  vaild=0

  while(vaild==0):
    print("How much do you bet?\n")
    betting = int(input())
    if type(betting) == type(1) and betting <= money:
      vaild = 1
    elif type(betting) != type(1) or betting <= 0:
      print("\nInvaild input, please enter your betting again.\nIt have to be a number biiger than 0 and smaller or equal to the money you have.\n")
    else:
      print("\nYou don't have enought money to bet. \nIt have to be a number biiger than 0 and smaller or equal to the money you have.\n")


  if betting > money:
    print(f"\nNot enough money to bet ${betting}")
    return 0
  
 
  answer = random.randint(0, 1)
  lst = ["Head","Heads", "heads","head","Tails","Tail","tail","tails"]


  vaild = 0
  while(vaild==0):
    print("Heads or Tails?\n")
    choice = input()
    if choice in lst:
      vaild = 1
    else:
      print("invaild input, please enter your choice again\n")

  if choice.lower() == "head" or choice.lower() == "heads":
    choice = 0
  else:
    choice = 1

  if choice == answer:
    money+=betting
    print(f"\nYou Win! You now have ${money}\n")
  
  else:
    money-=betting
    print(f"\nYou Lose! You now have ${money}\n")







#Call your game of chance functions here
filp_a_coin()
