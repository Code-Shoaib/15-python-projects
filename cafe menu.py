menu= {'pizza': 1500 ,
       'burger':299 ,
       'coffe': 450 ,
       'sandwich':900 ,
       'zinger burger':550}
print('WELCOME TO PHYTON CAFE')
print('pizza: 1500 \nburger:299 \ncoffe: 450 \nsandwich:900\nzinger burger:550')
pizza=1500
burger=299 
coffe= 450 
sandwich=900 
zingerburger=550
order_total=0
a=input('Enter your order = ').lower()
if a in menu:
    order_total+= menu[a]
    print(f'your {a} is succesfully added' )
    print(f'total order to pay {order_total}')
else :
    print(f'The {a} is not present in our menu')
b= input('if you want to add something type yes/no ').lower()
if b=='yes'.lower():
    item2=input('Enter second item = ')
    if item2 in menu :
        order_total+=menu[item2]
        print(f'Your {item2} is succesfully added')
        print(f'You have to pay {order_total}')
    else :
        print(f'This {item2} is not present in menu ')
        print(f'The total to pay is {order_total}')