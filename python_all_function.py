#string function

s="I am a boy"

print(len(s))#length on  string 

print(s.endswith("er"))#returns true if string ends with substr

print(s.startswith("i"))#Returns true if the string starts with the specified value


print(s.capitalize())#caapitalizes 1st character

print(s.replace("o","a"))#replaces all occurrences of old with new

print(s.replace("boy","man"))

print(s.find("o"))#returns 1st index of 1st occurrenc

print(s.count("a"))#counts the occurrence of substr in string

print(s.casefold())#Converts string into lower case

print(s.upper())#Converts a string into upper case

print(s.lower())#Converts a string into lower case

print(s.split())#Splits the string at the specified separator, and returns a list
