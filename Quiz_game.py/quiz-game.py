
score=0
print("welcome to quiz game!😊")
playing=input("do you want to play the game? ")
if playing.lower()!="yes":
    quit()

print("welcome to quiz game!")
print("your first question") 
answer=input("1.what is the capital of the india?  ")
if answer.lower()=="delhi":
    print("correct")
    score=+1
else:
    print("Incorrect")       
answer=input("2.which planet is called the red planet?  ")
if answer.lower()=="mars":
    print("correct")
    score=+1
else:
    print("Incorrect")      
answer=input("3.what is the national bird of india?  ")
if answer.lower()=="peacock":
    print("correct")
    score=+1
else:
    print("Incorrect")     
answer=input("4.which language mainly used for web pages?  ")
if answer.lower()=="html":
    print("correct")
    score=+1
else:
    print("Incorrect")      
answer=input("5.how many days are in weak?  ")
if answer.lower()=="seven":
    print("correct")
    score=+1
else:
    print("Incorrect")      
answer=input("6.what does cpu stands for?  ")
if answer.lower()=="central processing unit":
    print("correct")
    score=+1
else:
    print("Incorrect")      
answer=input("7.what is the largest ocean in the earth?  ")
if answer.lower()=="pacific ocean":
    print("correct")
    score=+1
else:
    print("Incorrect")      
    answer=input("8.which keyword is used to define function in python?  ")
if answer.lower()=="def":
    print("correct")
    score=+1
else:
    print("Incorrect")
print("your score is "+str(score))  
if score>=5:
    print("excellent🤩") 
elif score<5 and score>=3:
    print("good ☺")
else:
    print("keep pratice📖🖋")             