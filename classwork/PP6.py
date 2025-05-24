


PA=int(input("Enter pA"))
if PA<=2000:
    D=0.05*PA
elif PA>2000 and PA<=5000:
    D=0.05*2000+0.10*(PA-2000)
elif PA>5000 and PA<=10000:
    D=0.05*2000+0.10*3000+0.20*(PA-5000)
else:
    D=.05*PA
DP=PA-D
GST=0.09*DP
PA=DP+GST
print("Payable amoint is ",PA)
