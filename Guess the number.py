import random
randnumber=random.randint(1,100)
print('Welcome to Guess the number')
userguess=None

guesses=0

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
