import sys
arr=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   arr.append(l)
print("Unsorted array:",arr)

for i in range(len(arr)):
	min_idx = i
	for j in range(i+1, len(arr)):
		if arr[min_idx] > arr[j]:
			min_idx = j
			
	arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Sorted Array:",arr)