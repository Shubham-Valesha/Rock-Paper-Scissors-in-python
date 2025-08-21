import random 
print("")
playerchoice = int(input('Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n'))
computerchoice = int(random.randint(1,3))
if playerchoice == 1:
    print('Rock')
elif playerchoice == 2:
    print('Paper')
elif playerchoice == 3:
    print('Scissors')
if computerchoice == 1:
    print('Rock')
elif computerchoice == 2:
    print('Paper')
elif computerchoice == 3:
    print('Scissors')
if playerchoice == 1 and computerchoice == 3:
        print("Player won")
if playerchoice == 2 and computerchoice == 1:
        print("Player won")
if playerchoice == 3 and computerchoice == 2:
        print("Player won")
if playerchoice == 3 and computerchoice == 1:
    print("Player lost")
if playerchoice == 1 and computerchoice == 2:
    print("Player lost")
if playerchoice == 2 and computerchoice == 3:
    print("Player lost")
if playerchoice == computerchoice:
    print("Tie")
