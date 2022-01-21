#join the items of this list to a string sentence. print the result on the terminal
from ast import Delete


my_list=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
" ".join(my_list)
print(" ".join(my_list))

#2
#Change the value of True in this list to False. Print the result on the terminal
new_list = ['this', "brown", 55, "oxen", True, 0.85]
new_list[4]=False
print(new_list)

#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Sample_List.remove('Red')
Sample_List.remove('Pink')
Sample_List.remove('Yellow')
print(Sample_List)
 
#Write a program that takes in the user input of his favourite colour and adds it to an existing list of colours.
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
user_list=['orange', 'blue', 'grey' ,'purple']
color_list.extend(user_list)
print(color_list)

