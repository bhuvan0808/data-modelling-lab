str= input("please enter your string")
print(str) 
first_char = str[0]
str = first_char + str[1:].replace(first_char, '$')
print(str)