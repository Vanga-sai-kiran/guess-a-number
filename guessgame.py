import art
import random
from replit import clear
should_continue=False
while should_continue==False:
    print(art.logo)
    print("Welcome to Guess game!!! ")
    print("iam thinking number between 1 and 100 ")
    difficulty=input("chosse a Difficulty.Type 'Easy' or 'Hard' : ").lower()
    attempts=0
    if difficulty=="easy":
        attempts=10
    else:
        attempts=5
    random_number=random.randint(1,100)
    def check_attempts():
        print("sorry !you lost the game!")
        return input("Type 'yes' to play again or to 'no' to stop : ")
    
    def check(comp_generated):
        global attempts
        global should_continue
        print(f"You have only {attempts} attempts remaining to guess the  number.")
        guessing_number=int(input("Make a guess: "))
    
        if guessing_number== comp_generated:
            print("you got it.")
            input("Type 'yes' to play again or 'no' to stop : ")
            clear()
        elif guessing_number>comp_generated:
            print("Too high.")
            attempts-=1
            if attempts<=0:
               result=check_attempts()
               if result=="no":
                   should_continue=True
               
                   
            else:
                check(random_number)
        elif guessing_number<comp_generated:
            print("Too low.")
            attempts-=1
            if attempts<=0:
              result=check_attempts()
              if result=="no":
                   should_continue=True
            else:
                check(random_number)
    check(random_number)
