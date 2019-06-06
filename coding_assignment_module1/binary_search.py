def BinarySearch(arr,key,b,e):
	if e>=1:
		mid=int((b+(e-1))/2)
		if arr[mid]==key:
			return mid
		elif (arr[mid]<key):
			return BinarySearch(arr,key,mid+1,e)
		elif (arr[mid]>key):
			return BinarySearch(arr,key,b,mid-1)
		else:
			print('Element is not present')
n=int(input('Enter the number of elements you would like to enter: '))
a=[]
print('Enter the elements in ascending order: ')
while len(a)<n:
	num=int(input('Enter the number: '))
	a.append(num)
x=int(input('Enter the element whose position you want to search: '))
ans=BinarySearch(a,x,0,len(a))
print(ans)
	