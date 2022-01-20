#strings
g="2"+"2"
print(g)

k="hello"+"charles"
print(k)

#"i am a boy"
# 0123456789
#slicing strings string slicing=sub-stringing
my_string="i am a boy"
my_string[3]
print(my_string[3])

print(my_string[2:6])

print(my_string[2: ])
print(my_string[:5])
print(my_string[-5:])
print(my_string[-9:-5:2])
#classwork
st1="this is 1000 naira"
st2="this 500 is lovely"
first_value=int(st1[8:12])#converting from string to integer
second_vale=int(st2[5:8])
answer=((first_value)+(second_vale))


#f-string #under string formatting
print(f"the sum of {first_value} and {second_vale} is {answer} ")

#new line and tabbing
print("""This is a wonderful string



                    yours in country
                    the astroverse team.""")
#string methods
#index #first method

a="aaboy"
print(a.index("a"))
print(a.rindex("a"))#searches from right to left

#find #second method

print(a.find("a"))
print(a.rfind("a"))#if it doesnt find what it is asked for it tells you -1
#count
print(a.count("a"))

#replace
print(a.replace('a','w'))

#split
sen="ada is a girl and tunde loves ice cream but, ayo does not give him"
print(sen.split())

print(sen.split(','))

num=('0', '4' , '3' , '2')
otp="".join(num)
print(otp)

#count
str1="welcome to USA, usa awesome, isnt it?"
print("the_usa_count_is:", str1.lower().count("usa"))

str2="emma is a data scientist who knows python. emma works at google."
print(str2.rfind("emma"))

str1="emma is a data scientist"
print(str1.replace("-", " "))

str1="/*jon is @developer & musician"
final_answer=str1.replace("/"," ").replace("*" , " ").replace("@"," ").replace("&", "")
print(final_answer)

#data structures
#list #first data structure

my_list=["i", "am", "good"]
a_list=["she", "is", "a", "queen"]

list1=[10, 20,[300, 400,[5000, 6000], 500],30 ,40]
first_val= list1[2][2][0]
second_val=list1[2][3]
print(first_val + second_val)