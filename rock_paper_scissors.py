import random

trials=5
user_name=input("please enter your name\n>")
user_name=0
comp=0
choices=["r", "p","s"]
print("welcome to rock paper scissors!!!")
while  trials>0:
    computer=random.choice(choices) 
    user_input=(input(f"please input your choice r , p or s\n>")).lower()
    if user_input not in choices:
        print("invalid option try again")
        trials-=1
        print(f"{trials} trial(s) left")
    if user_input in choices:
        if user_input=="r" and computer =="s" :
            print(f"computer selected {computer}\n you win!")
            user_name+=1
            trials-=1
            print(f"{trials} trial(s) left")
        elif user_input=="s" and computer =="r" :
            print(f"computer selected {computer}\n you lose!")
            comp+=1
            trials-=1
            print(f"{trials} trial(s) left")
        elif user_input=="p" and computer=="r":
            print(f"computer selected {computer}\n you win!")
            user_name+=1
            trials-=1
            print(f"{trials} trial(s) left")
        elif user_input=="r" and computer=="p":
            print(f"computer selected {computer}\n you lose!")
            comp+=1
            trials-=1
            print(f"{trials} trial(s) left")
        elif user_input=="p" and computer=="s":
            print(f"computer selected {computer}\n you lose!")
            comp+=1
            trials-=1
            print(f"{trials} trial(s) left")
        elif user_input=="s" and computer=="p":
            print(f"computer selected {computer}\n you win!")
            user_name+=1
            trials-=1
            print(f"{trials} trial(s) left")
        elif user_input=="p" and computer=="p":
            print(f"computer selected {computer}\n tie!")
            trials-=1
            print(f"{trials} trial(s) left")
        elif user_input=="s" and computer=="s":
            print(f"computer selected {computer}\n tie!")
            trials-=1
            print(f"{trials} trial(s) left")
        elif user_input=="r" and computer=="r":
            print(f"computer selected {computer}\n tie!")
            trials-=1
            print(f"{trials} trial(s) left")
print(user_name)
print(comp)
if user_name>comp:
    print("you win")
elif comp>user_name:
    print("you lose better luck next time")





        


