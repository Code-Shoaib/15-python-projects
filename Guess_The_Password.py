import random as rd

easy_word = ['apple', 'banana', 'laptop', 'tablet', 'chair']
medium_word = ['playing', 'samsung', 'python', 'diamond', 'tiger']
hard_word = ['elephant', 'umbrella', 'computer', 'mountain', 'playstation']

print('Welcome to the password guessing game')
print('Choose a difficulty level: easy, medium or hard')

level = input('Enter difficulty level: ').lower()

if level == 'easy':
    secret = rd.choice(easy_word)
elif level == 'medium':
    secret = rd.choice(medium_word)
elif level == 'hard':
    secret = rd.choice(hard_word)
else:
    print('Invalid choice. Defaulting to easy level.')
    secret = rd.choice(easy_word)

attempt = 0
print('Guess the password')

while True:
    guess = input('Enter your password: ').lower()
    attempt += 1

    if guess == secret:
        print(f'Congratulations! You guessed it in {attempt} attempts.')
        break

    # Generate a hint
    hint = ''
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += '_'
    
    print('Hint: ' + hint)
    print('Try again.\n')
