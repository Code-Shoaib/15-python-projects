#MY first game  by watching code with harry video

import random # It was a random module for import random words or numbers for e.g : see line 29 to 35 
def game(Comp , you):
    # if two values are equal declare a tie
    if Comp == you :
        return None
    # Check all possibilities of s
    elif Comp == "r":
        if you == "s":
            return False
        elif you == "p":
            return True
        # check all possibilities of w
    if Comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True
    # check all possibilities of g
    if Comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True
   

    




# we make this process using import random in line 2
# we also give 1 = s 2= w 3= g so through random import it give us random number 
randno=random.randint(1,3)
if randno==1 :
    Comp ="r"
elif randno==2:
    Comp ="p"
elif randno==3:
    Comp ="s"





# from line to 42 to last we use it for the game input and other things
print("Comp Turn : Rock(r) Paper(p) or Scissor(s)?")
you=input("Your turn : Rock(r) Paper(p) or Scissor(s)?")
# print  what comp and you selected
print(f"Comp choose {Comp}")
print (f"You choose {you}")

a=game(Comp,you)
# print result 
if a == None :
    print("Its a tie")
elif a:
    print("you win")
else :
    print("you lose")


