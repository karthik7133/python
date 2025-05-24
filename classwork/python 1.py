#perimeter and area of tringle:
'''from math import sqrt
s1=int(input("Enter s1 value:"))
s2=int(input("Enter s2 value:"))
s3=int(input("Enter s3 value:"))
s=(s1+s2+s3)/2
perimeter = s1+s2+s3
area =sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(area)
print(perimeter)'''
#to calculate area of circle and perimeter of circle:
R=float(input("Enter radius of circle:"))
from math import pi
area = pi*R*R
perimeter = 2*pi*R
print("area of circle=",area)
print("perimeter ofcircle=",perimeter)
