max_val = 0
a = "10"
b = "34"

for i in a:
    for j in b:
        for k in a:
            s = str(i) + str(j) + str(k)  # total length = len(a) + len(b) = 3
            if len(s) == len(a) + len(b):  # Ensure valid length
                if max_val < int(s):
                    max_val = int(s)

print(max_val)


