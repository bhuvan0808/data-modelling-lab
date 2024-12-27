#write a python code that tkes list of words and returns length of smllest one

#small program to print smallest word in the string using isspace
#pyhthon code to get smallest word in string using isspace
     
'''def smallest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]


result = smallest_word(["abhi", "bhuvan", "ram"])
print(result[1])
print( result[0])''''

#write a python code to change occurences of letter H to $

#write a program to find repeated charecters

'''def char(str):

    hash = {}
    for ch in str:
        if ch in hash:
            return ch;
        else:
            hash[ch] = 0
    return ''

print(char('ABaBCbGc'))'''


'''def smallest_word(s):
    words = [word for word in s.split() if not word.isspace()]
    if not words:
        return None
    return min(words, key=len)'''

'''def smallest_word(string):
    # split the string into a list of words
    words = string.split()
    
    # initialize the smallest word as the first word in the list
    smallest = words[0]
    
    # iterate over the remaining words
    for word in words[1:]:
        # if the word is smaller than the current smallest word and not empty or whitespace
        if len(word) < len(smallest) and not word.isspace():
            # set it as the new smallest word
            smallest = word
    
    return smallest'''

'''#write a python code to find repeated charecters where string contains upper and lower case letters?

def find_repeated_chars(string):
    # convert string to lowercase to make case-insensitive
    string = string.lower()
    
    # initialize a set to hold repeated characters
    repeated_chars = set()
    
    # iterate over each character in the string
    for i in range(len(string)):
        # if the character is not already in the set and appears again in the string
        if string[i] not in repeated_chars and string.count(string[i]) > 1:
            # add it to the set of repeated characters
            repeated_chars.add(string[i])
    
    return repeated_chars'''

def Lab_3(string):
    str = string.replace('H', '$')
    return str
#write a python code to replace ll occurances of first charecter with $ except first charecter?

def question3(string):
    first_index = string.find('first_index')
    new_string = string[:first_index+1] + string[first_index+1:].replace('H', '$')
    
    return new_string


str= input("please enter your string")
print(str) 
first_char = string[0]
str = first_char + string[1:].replace(first_char, '$')
print(str)

str = input("Enter a string: ")
print("Given String: ", str)

ch = str[0]
str = str.replace(ch, '$')
str = ch + str[1:]

print("BeforeString:",str)