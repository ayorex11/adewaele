

import random


data = {}
trans_data = {}

print("Welcome to the AstroBank App")
while True:
    print("Enter s to signup or l to login:")
    print("Enter any other key to close")
    choice = input(">").lower()

    if choice == 'l':
        acc_num = input("Enter your account num:\n>")
        pin = input("Enter your pin:\n>")
        
        user = data.get(acc_num)
        
        if user and user['pin'] == pin:
            print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")
            
            while True:
                print("""\nWhat would you like to do?
                    Press 1 to withdraw
                    Press 2 to deposit
                    Press 3 to transfer
                    press 4 to get bank statement
                    Press any other key to quit.""")
                
                user_input = input(">")
                
                if user_input == '1':
                    amount = int(input("How much?\n>"))
                    debit_li=[amount]
                    if amount >= user['bal']:
                        print("Insufficient Funds")
                    else:
                        user['bal']-=amount
                        
                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "withdrawal"
                        }
                        average_debit=sum(debit_li)/len(debit_li) 
                        trans_data[acc_num].append(detail)
                        
                        
                        print("Please take your cash")
                        print(f"Balance is {user['bal']}")
                        
                elif user_input == '2':
                    amount = int(input("How much?\n>"))
                    amount_list=[amount]
                    user['bal']+=amount
                    
                    #log transaction data
                    detail = {
                        "amount":amount,
                        "type": "credit",
                        "action" : "deposit"
                    }
                    
                    average_credit=sum(amount_list)/len(amount_list) 
                    
                    
                    trans_data[acc_num].append(detail)
                        
                    print("Successful")
                    print(f"Balance is {user['bal']}")
                elif user_input == '3':
                    recepient_ = input("Enter recepient account\n>")
                    amount = int(input("How much?\n>"))
                    debit_li=[amount]
                    if user['bal'] < amount:
                        print("Insufficient Funds")
                    
                    recepient = data.get(recepient_)
                    if recepient:
                        recepient['bal'] += amount
                        user['bal'] -=amount
                        
                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "transfer"
                        }
                       
                        average_debit=sum(debit_li)/len(debit_li) 
                        trans_data[acc_num].append(detail)
                        
                        detail_recepient = {
                            "amount":amount,
                            "type": "credit",
                            "action" : "transfer"
                        }
                        
                        trans_data[recepient_].append(detail_recepient)
                        
                        print("Successful")
                        print(f"Balance is {user['bal']}")
                    else:
                        print(f"Unable to fetch customer with account {recepient_}")
                elif user_input == '4':
                    print(trans_data[acc_num])  
                      
                else:
                    print("Good bye")
                    break
        else:
            print("Invalid Login")
            
    elif choice == 's':
        def validate_name(name):
            is_valid=True
            if not any(char.islower() for char in name):
              print("invalid input")
              isValid= False
            if not any(char.isupper() for char in name):
              print("invalid input")
              isValid= False
            else:
                print("valid input")
        name=input("please enter name\n>")
        validate_name(name)
        def validate_dob(dob):
            is_valid=True

            if not any(char.isdigit() for char in dob):
              print("invalid input")
              is_valid=False
            else:
             print("valid input")
        dob=input("please enter dob\n>")
        validate_dob(dob)
        def validate_bvn(bvn):
            is_valid=True

            if not any(char.isdigit()for char in bvn):
                print("invalid input")
                is_valid=False
            else:
                print("valid input")
        bvn=input("please enter bvn\n>")
        validate_bvn(bvn)
        def validate_pin(pin):
            is_valid=True

            if not any(char.isdigit() for char in pin):
               print("invalid input")
               is_valid=False
            else:
              print("valid input")
        pin=input("please enter password\n>")
        validate_pin(pin)


     
        
        
        details = [('name', name), 
                ('dob', dob), 
                ('bvn', bvn), 
                ('pin', pin), 
                ('bal',0) 
                ]
    
        #generate account number
        num = [1,2,3,4,5,6,7,8,9,0]
        acc_num_list = ["3"]
        acc_num_list.extend([str(random.choice(num)) for _ in range(9)])
        
        
        acc_num = "".join(acc_num_list)
        
        data[acc_num] = dict(details)
        trans_data[acc_num] = []
        
        print(f"\nYour account has been created. You account number is {acc_num}\n")

    else:
        break



print(data)
print(trans_data)
print(f"your average credit is {average_credit}")
print(f"your average credit is {average_debit}")
