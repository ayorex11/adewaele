from msilib import datasizemask
import random
data={
    "3456781234":{
        "name": "desmond",
        "dob":  "09-09-09",
        "bvn":  "123456237865473",
        "pin":  "3412",
        "bal":  0
    }   
}

print("welcome to the AstroBank app")
print("enter s to signup l to login w to withdraw or d to deposit:")
choice=input(">").lower()

if choice=='l':
    acc_num=input ("enter your account number:\n>")
    pin=input("enter your pin:\n>")

    user=data.get(acc_num)
    
    if user is not None and user["pin"]==pin:
        print("success")
    else:
        print("invalid login")
if choice=="s":
    name=input("welcome\n please enter your full name\n>")
    dob=int(input("enter your date of birth in this format ddmmyy\n> "))
    bvn=int(input("please enter your bvn\n>"))
    pin=int(input("create your four digit code\n>"))
    bal=int(0.0)
    q=str(random.randrange(1111111111, 9999999999))
    accountnumber=q
    print("generating account number\n", q)
    print("account successfully created!")

    data[accountnumber]={"name": name, "dob": dob, "bvn":bvn, "pin":pin, "bal":bal}
    data.update(accountnumber)

if choice=="w":
    withdraw=int(input("enter the amount you wish to withdraw\n>"))
    if withdraw>bal:
        print("insufficient funds")
    else:
        bal-=withdraw



    


