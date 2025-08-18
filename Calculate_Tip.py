#take users bill


print('whats the total bill for today, please?')

#Ask for total bill
Bill=float(input('Enter bill :\n'))

#Get amount of tip
Tip=int(input('How much tip we add 10% , 18% , 20% : '))

#Multiply bill with tip and divide by 100 to get tip amount
percentage=(Bill*Tip/100)

#Give total value 
Total=(Bill+percentage)

#Print all the data
print(f'\n The {Tip}% of {Bill} is {percentage} and Total is {Total}')