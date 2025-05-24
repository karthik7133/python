r1="rate of intrest of SBI"
r2="rate of intrest of ICICI"
SI1="simple intrest of SBI"
SI2="simple intrest of ICICI"
CI1="compound intrest of SBI"
CI2="compound intrest of ICICI"
p="principal"
p=5000
n="no of years"
n=3
r1=0.06
r2=0.065
SI1=(p*r1*n)/100
CI1=((p*((1+r1)/100))** n)-p
print(SI1)
print(CI1)

