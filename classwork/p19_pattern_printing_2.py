


for i in range(1,6):
    k=1
    for j in range(1,6):
        if(j<6-i):
            print(" ",end=" ")
        else:
            print(k,end=" ")
            k=k+1
    print("\n")





for i in range(1,6):
    print("* "*i)
    print("\n")







rows = 10
# reverse loop
num=0
for i in range(1,rows+1):
    num = num+i
    num2=num
    for j in range(1, i+1):
        print(num2, end=' ')
        if i!=1:
            num2=num2-1
    print("\r")

print('\r')






rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    #b += 1
    
    for j in range(1, i + 1):
        #print(b, end=' ')
        print(rows+1-i, end=' ')
    print('\r')                  #End of program


print('\r')

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('') 

print('\r')

rows = 5
#i = 1
for i in range(1,rows+1):
    #j = 1
    for j in range(1,i+1):
        print((i * 2 - 1), end=" ")
        #j = j + 1
   # i = i + 1
    print('') 

print('\r')



rows = 5
# reverse loop
for i in range(rows, 0, -1):
    #num = i
    for j in range(1, i+1):
        print(i, end=' ')
    print("\r")

print('\r')

rows = 5
num=1
# reverse loop
for i in range(1,rows+1):
    for j in range(1, i+1):
        print(num, end=' ')
        num += 1
    print("\r")

print('\r')



start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop

print('\r')

rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")

print('\r')

def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


print('\r')

def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = 7
print_pascal_triangle(rows)

rows = 8
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()

print('\r')

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

print('\r')

print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")

    rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

    rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

    rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1

rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
