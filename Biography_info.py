name=input ('Enter your name:')
if name.replace('.', '', 1).isdigit():
    print('Invalid object ! write a valid object')


month=input('Enter your birth month: ')
if month.replace('.', '', 1).isdigit():
    print('Invalid object ! write a valid object')
year=int(input('Enter birth year: '))
date=int(input('Enter birth date: '))
adddress=input('Enter your address: ')
goal=input('Enter your personal goal: ')

print(f'Name: {name}')
print(f'Date of birth: {month} {date}, {year}')
print(f'Address: {adddress}')
print(f'Personal goals: {goal}')


