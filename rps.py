import sys
import random 
print("")
playerchoice = int(input('Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n'))

if playerchoice < 1 or playerchoice > 3:
    sys.exit("You must enter 1, 2, or 3.")

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
        print("🎊 Player won")
elif playerchoice == 2 and computerchoice == 1:
        print("🎊 Player won")
elif playerchoice == 3 and computerchoice == 2:
        print("🎊 Player won")
elif playerchoice == computerchoice:
    print("👀Tie")
else: 
    print("😣 Python wins!")
