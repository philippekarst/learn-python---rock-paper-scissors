import random
import numpy
import math

choices = ['rock', 'paper', 'scissors']

playerchoice = input('To start game enter your choice:')
playerchoice = playerchoice.lower()

computerchoice = random.choice(choices)
computerchoice1 = computerchoice
list = [playerchoice, computerchoice]
k=0
for i in list:
    k=k+1
    if i == 'scissors':
        computerchoice = int(2)
        if k==1:
          playerchoice = int(2)
    if i == 'rock':
        computerchoice = int(3)
        if k==1:
            playerchoice = int(3)
    if i == 'paper':
        computerchoice = int(5)
        if k==1:
            playerchoice = int(5)

print(playerchoice*computerchoice)
if math.sqrt(playerchoice*computerchoice).is_integer():
    print(f'The computer also chose {computerchoice1}, its a tie')
elif playerchoice == int(2) and ((playerchoice*computerchoice)/3).is_integer():
    print(f'The computer chose {computerchoice1}, you lost')
elif playerchoice == int(3) and ((playerchoice*computerchoice)/5).is_integer():
    print(f'The computer chose {computerchoice1}, you lost')
elif playerchoice == int(5) and ((playerchoice*computerchoice)/2).is_integer():
    print(f'The computer chose {computerchoice1}, you lost')
else:
    print(f'The computer chose {computerchoice1}, you win')

print(type(math.sqrt(playerchoice*computerchoice)))
