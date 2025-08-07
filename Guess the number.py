#Import randmon module which give us random number from 1 to 100

import random

randnumber=random.randint(1,100)

print('Welcome to Guess the number')

#we give userguess a none value to use it before starting while loop otherwise while loop through an error


userguess=None


#give guesses a value so every time a person use a guess it will add here


guesses=0

#Start a while loop which willrun until  the user guess the number or the user exceed the limit of guessing number 
while(userguess != randnumber ):

    userguess=int(input('Enter your number:'))
    
    guesses += 1
    
    if userguess==randnumber:
        print('You guessed it right!')
        print(f'You guess in {guesses} guesses')

    else:
        print('You guessed it wrong!')

    
    if (userguess==randnumber):
        break  

    elif (userguess>randnumber):
        print('You guess a larger number enter a smaller one')

    else:
        print('You guess a small number enter a larger one')

    if guesses==5:

        print('You have exceed your guessing limit')
        print(f'The guess is {randnumber}')
        break
