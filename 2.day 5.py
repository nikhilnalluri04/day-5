n=input("enter the grade of the employee :")
while(n!="A")&(n!="B")&(n!="a")&(n!="b"):
    if(n!="A")&(n!="B")&(n!="a")&(n!="b"):
        print("invalid grade ")
    n=input("enter a proper grade(i.e A or B):")
m=int(input("enter the employee salary :"))
while(m<=0):
    if(m<=0):
        print("invalid")
        m=int(input("enter a valid employee salary :"))


if(n=="A")|(n=="a"):
    bonus=5*m/100
    print("bonus:",bonus)
    a=m+bonus
    print("the total salary with bonus is ",a)
elif(n=="B")|(n=="b"):
    bonus=10*m/100
    print("bonus:",bonus)

    a=m+bonus
    print("the total salary with bonus is ",a)

else:
    print("invalid")

if(m<10000):
    b=2*a/100+a
    print("you got more 2% bonus ")
    print("Hurray! your bonus salary is",b)

    
    
    
    
    
    
    
    
