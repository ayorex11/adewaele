import random
rock="r"
paper="p"
scissors="s"
paper>rock
scissors>paper
rock>scissors
trials=4
user_name=input("please enter your name\n>")
user_name=0
comp=0
choices=[rock, paper,scissors]
print("welcome to rock paper scissors!!!")
while  trials>=0:
    computer=random.choice(choices) 
    user_input=(input(f"please input your choice {rock} {paper} or {scissors}\n>"))
    if user_input not in choices:
        print("invalid option try again")
    if user_input in choices:
        if user_input>computer:
            user_name+=1
            print(computer)
            print(f"yayy.. you won you have {trials} trial(s) left")
        if user_input<computer:
            comp+=1
            print(computer)
            print(f"awwnn.. you lost you have {trials} trial(s) left")
        if user_input==computer:
            print(computer)
            print(f"it's a tie!!!.. play again you have {trials} trial(s) left ")
    trials-=1  
print(f"your score is {user_name}")
print(f"computer's score is {comp}")   
if user_name>comp:
    print("you win!")
elif comp>user_name:
    print ("awww.. you lost, better luck next time.")


