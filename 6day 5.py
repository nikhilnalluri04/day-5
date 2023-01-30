from math import factorial
n = int(input("enter the number of rows:"))
b=int(input("enter  a row number:"))
s=0
for i in range(n):
    for j in range(n-i+1):

        print(end=" ")

    for j in range(i+1):
            a=(factorial(i)//(factorial(j)*factorial(i-j)))
            if b==i+1:
                s=s+a
               
            print(a,end=" ")
    print()
print()
print("sum of the elements of",b,"th row is ",s)
