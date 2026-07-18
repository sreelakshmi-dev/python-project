#roll the dice
#take input from usery/n
#if enter y take two random nubbers
#enter n
#print a message
import random
count=0
while True:
 choice=input('if you want to roll the dice (y/n):').lower()
 if choice=='y':
    
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    count+=1
    print(f'({dice1},{dice2})')
    
     
    
    
 elif choice=='n':
    print("thank for playing")
    print("total rolls:",+count)   


 else:
    print("invalid choice")

 















