import re

txt = "hellof planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("^h.*t$", txt)
if x:
    print("Hi")
else:
    print("Hello")




import re


txt = "That will be 678 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)



import re

st = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-k]", st)
print(x)
