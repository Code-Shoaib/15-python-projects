class calculator:
    #add all logic
    def add ():
        print(x+y)
    
    def subtract():
        print(x-y)

    def multiply():
        print(x*y)
    
    def divide():
        print(x/y)


x=int(input('Enter first number'))
symbol=input('Enter symbol + , - , * , /, :')
y=int(input('Enter second number'))

person=calculator
#Add all conditions
if symbol =='+':
    person.add()

if symbol=='-':
    person.subtract()

if symbol=='*':
    person.multiply()

if symbol=="/":
    person.divide()

