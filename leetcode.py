def upto20(n):
    l=["Zero","one","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen"
            "Eighteen","Nineteen"]
    return l[n]
def tens(n):
    l=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninty"]
    return l[n]
def printer(n):
    if n<20:
        print(upto20(n))
    elif n<100:
        print(tens(n//10)+" "+upto20(n%10))
    elif n<1000:
        if n==100:
            print("Hundred")
        else:
            print(upto20(n//100)+" Hundred and "+upto20(n%100//10)+" " +upto20(n%10))
    elif n<100000 and n>999:
        if n==1000:
            print("Thousand")
        if n==10000:
            print("Ten thousand")
        else:
            print(tens(n//10000)+" "+upto20(n%10000//1000)+ " Thousand "+upto20(n%1000//100) +" Hundred and "+tens(n%100//10)+" "+upto20(n%10))

n=int(input("Enter number:"))
printer(n)