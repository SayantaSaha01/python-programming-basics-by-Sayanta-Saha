'''
1 for snake
-1 for water 
0 for gun 
'''        
import random

computer = random.choice([-1, 0,1]) 
userinput =input("enter the alphabet between  s or w or g  :  ")
word_to_number ={"s":1,"w":-1,"g":0}
you= word_to_number[userinput]
number_to_word ={1:"snake",-1:"water",0:"gun"}
print(f"you choose : {number_to_word[you]}")
print(f"computer choose : {number_to_word[computer]}")


if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")