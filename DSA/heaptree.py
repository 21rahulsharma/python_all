#Heap Implementation
#Max Heapify
def max_heapify(arr,n,i):
    largest=arr[i]
    left=2*i+1
    right=2*i+2
    if(left<n) and arr[largest]<arr[largest]

#Driver Code
arr=[2,66,30,5,9,10]
n=len[arr]

#Build a Max Heap
for i in range(n//2,-1,-1):
    max_heapify(arr,n,i)

#Max Heapify
print("Max Heap is")
for i in range(n):
    print(arr[i])