num=int(input("Enter a number: "))
sum=0
while(num>0):
	rem=num% 10
	sum=sum+rem
	num=num//10
print("\n Sum of the digits of the number is ",sum)