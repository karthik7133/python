import re

txt = "The rain in 678 Spain"
x = re.sub("\d", "a", txt)
print(x)

txt = "The rain in 543 842 Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.split("\d", txt)

print(x)

