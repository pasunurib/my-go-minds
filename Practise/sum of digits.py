#give the number
i=int(input("Enter the number to find sum  : "))
#Here sum is 0
sum=0
# Here do some logical calculation to find sum of digits
while (i>0):
    sum=sum+i%10
    i=i//10
#Print the output
print("Sum of digits :  ",sum)
