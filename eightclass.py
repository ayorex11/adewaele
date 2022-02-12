# # #functions unfruitful functions
# # def cal():
# #     print(2+2)
# # cal()
# # a=cal()

# #fruitful functions
# def cal():
#     return 2+2
# a=cal()
# print(a)

# #how to make functions more generic
# def cal(x,y):#parameters are used when defining the function
#     print(x+y)
# cal(5,3)#arguments are used when calling the fnction
# def cal(x,y):
#     print(x-y)

# #type of arguments
# cal(10,5)#positional arguments
# def cal(x,y):
#     print(x-y)
# cal(y=5,x=10)#keyword arguments
# def cal(x,y):
#     print(x-y)
# cal(y=5)
# default parameters
# def cal(x,y=5):
#     print(x-y)
# cal(10)

# def cal(x,y=5):
#     print(x-y)
# cal(10,y=2)



# def is_odd(n):
#     return n%2!=0


# a=is_odd(5)
# print(a)   

# def is_odd(n):
#     if n%2==0:
#         return False
#     else:
#         return True

# a=is_odd(5)
# print(a)




# def is_prime(n):
#     if n==1:
#         return False
    
#     if n==2:
#         return True
#     if n>2 and n%2==0:
#           return False

#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#         return True

# a=is_prime(19)
# print(a)

#write a function that checks if a password is strong

def password_check(passwd):
    
 

    specialsym=["!", "@", "#" , "$"]
    val=True

    if len(passwd)>8:
        print("length of password must not be greater than eight")
        val=False
    if not any(char.isdigit() for char in passwd):
        print("password should have at least one numeral")
        val=False
    if not any(char.isupper() for char in passwd):
        print("password should have at least one uppercase letter")
        val=False
    if not any(char.islower() for char in passwd):
        print("password should have at least one lowercase letter")
        val=False
    if not any(char in specialsym for char in passwd):
        print("password requires at least one special symbol")
        val=False
    if val:
        return val


password=input("please input password\n>")
if (password_check(password)):
    print("password is valid")
else:
    print("invalid password")


    

import string
import random

charcters=list(string.ascii_letters+string.digits+string.punctuation)

def generate_password():

    length=12
    random.shuffle(charcters)
    password=[]
    for i in range(length):
        password.append(random.choice(charcters))
    random.shuffle(password)
    print("".join(password))

generate_password()



