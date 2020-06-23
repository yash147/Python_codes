num=int(input("Enter the range of fibo=>"))

n1=0
n2=1
i=2

if num<=0:
    print("Enter the positive no:")
elif num==1:
     print("fobo series up to :",num)
     print (n1)
else:
     print("fibo series up to :",num)
     print(n1)
     print(n2)
     while i<num:
         n3=n1+n2
         print(n3)
         n1=n2
         n2=n3
         i=i+1
