#find the sum of even numbers
num=85647
num_str=str(num)
even_sum=0

for digit in num_str:
    if int(digit)%2 ==0:
        even_sum+=int(digit)


print("Sum of Even digits :",even_sum)
