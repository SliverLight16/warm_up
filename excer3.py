import math

def breakup(word):
    num = 0  
    letters = list(word)

    while num < len(letters):
        
        if num%2 == 0:
            print(letters[num])

        num += 1

myTurn = breakup(input())

'''the code break if "num" is allowed to equal the length, then it will exceed the  and cause an error
Ex: artisan, length = 7, in a list 0 to 6
list[7] doesnt exist so it shouldn't be allowed to enter the loop
Can only be < the length '''