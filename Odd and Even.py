def main():

    #we usae it to call all the function

    is_odd(get_input())
    tryagain()



#This is get_input in the main function inside is_odd
#It will get all the input
def get_input():

    try:

        #This function check that number in range from 1to 1000
        number=int(input('What are you thinking:'))

        if number<0 or number>1000:

            print(f'The number must be from range 1 to 1000')

            number=int(input('What are you thinkng:'))

            #Return number
        else:
            return number
        
    except ValueError:

        #Check that value is not str
        print('That not a number ')
        main()



#That check that number is add or even


def is_odd(number):

    if number % 2 ==0:
        print('That an even number')

    else:
        print('That an odd number')

#This fuction is use to ask to user for another try



def tryagain():
    choice=str(input('Have another? (y,yes or n,no)')) .strip() .lower()
    #It will check that input is only y,yes or n,no
    while choice not in ('y','yes','n','no'):
            choice=str(input('Have another? (y,yes or n,no)')) .strip() .lower()

    else:
        if choice in ('y','yes'):
            main()
        else:
            exit()


#It will call the function
if __name__=="__main__":
    main()

        