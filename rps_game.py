#import random module
import random

#Rules of Rock, Paper, Scissors (with Strong concatenation)
print('Winning Rules: \n' + "Rock v. Paper --> Paper wins \n"
      + "Rock v. Scissors --> Rock wins \n"
      + "Paper v. Scissors --> Scissors win \n")

round = 1
while True:
    print("Get ready for round ",round)

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    #receive user input
    user_choice = int(input("Enter your choice: "))

    #if user enters a number outside of 1  or 3, ask them to insert a valid value
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input('Please enter a valid choice'))
    
    #initialize variable containing name of choice
    if user_choice == 1:
        user_choice_name = 'Rock'
    elif user_choice == 2:
        user_choice_name = 'Paper'
    else:
        user_choice_name = 'Scissors'

    #print user choice
    print('You chose \n',user_choice_name)
    print('Computers Turn....')

    #Computer will randomly choose a number between 1 and 3 inclusivelt using randInt method from random module
    cpu_choice = random.randint(1,3)

    #loop until cpu_choice equals user choice value. IF YOU NEVER WANT THERE TO BE A TIE
    #while cpu_choice == user_choice:
    #    cpu_choice = random.randint(1,3)
    
    #initialize variable containing name of cpu choice
    if cpu_choice == 1:
        cpu_choice_name = 'RocK'
    elif cpu_choice == 2:
        cpu_choice_name = 'PapeR'
    else:
        cpu_choice_name = 'ScissorS'
    
    print("Computer chooses \n", cpu_choice_name)
    print(user_choice_name, 'vs.',cpu_choice_name)

    #Check if there is a draw
    if user_choice == cpu_choice:
        print('You Tied!', end="")
        result = "DRAW"
    #Winning conditions
    if user_choice == 1 and cpu_choice == 2:
        print('Paper wins =>', end="")
        result = 'papeR'
    elif user_choice == 2 and cpu_choice == 1:
        print('Paper wins =>', end="")
        result='Paper'

    if user_choice == 1 and cpu_choice == 3:
        print('Rock wins =>', end="")
        result = 'Rock'
    elif user_choice == 3 and cpu_choice == 1:
        print('Rock wins =>', end="")
        result='RocK'

    if user_choice == 2 and cpu_choice == 3:
        print('Scissors win =>', end="")
        result = 'ScissorS'
    elif user_choice == 3 and cpu_choice == 2:
        print('Scissors win =>', end="")
        result='Scissors'
    
    #Prints if the user or computer won, or if it was a draw
    if result == 'DRAW':
        print("<== Tie ==>")
    elif result == user_choice_name:
        print("You Win!")
    else:
        print("Computer Wins!")
    
    print("Play Again? (y/n)")
    #if user input n or N then condition is true
    ans = input()
    if ans == "n":
        break
    else:
        round = round + 1
print("Thanks for playing!")