import random
num=[1,2,3,4,5,6,7,8,9,0]
computer=random.choice(num)
score=0
trial=3

for i in range(10000000000000):
    if trial==0:
       print("game over!")
       print(f"your score is {score}")
       break
    computer=random.choice(num)
    play=int(input("enter your number\n>"))

    if play==computer:
        trial+=1
        score+=3
        print("correct")
        print("you have been given an extra trial")
        print("yayy!!!")
    
    else:
      trial-=1
      print("incorrect!")
      print(f"you have {trial} trial(s) left")