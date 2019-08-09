import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
  #Make sure bet is above 0
  if bet<0:
    print ("Oops! Looks like you forgot to place a bet!")
  #Announce coin plip
  print("Let's begin the game! You guessed " + guess + " and bet "+ str(bet) + " dollars.")
  #Coin flip: 1 = heads, 2 = tails
  result= random.randint(1,2)
  if result==1:
    print("It's Heads!")
  else:
    print("It's Tails")
  #Announces whether player lost or won
  if (result==1 and guess== "Heads") or (result==2 and guess== "Tails"):
    print ("Congratulations You Won " + str(bet) + " dollars!")
    return bet
  else:
    print("Awww You Lost " + str(bet)+ " dollars.")
    return -bet
