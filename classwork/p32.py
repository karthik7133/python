def fun(**a):
    print(a['Name'])
    def fun1():
        b=6
        print(a)
        print(b)
    fun1()
def fun2():
        b=6
        print(b)
        fun()
      
m=4
n=7
fun(Name="Ram",age=34,place="VIT")
#fun("Ram",34,"VIT")

