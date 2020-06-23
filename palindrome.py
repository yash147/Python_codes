a=eval(input("Enter the number to palindrome : "))
reverse=0
temp=a

while (temp > 0):
    reminder =temp % 10
    reverse =(reverse * 10)+reminder
    temp=temp//10

print("reverse of a string is = %d" %reverse)

if(a == reverse):
    print("Number is palindrome")
else:
    print("Number is not palindrome")


    
