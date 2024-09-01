#to print the kth largest element in an array
def kl(arr,k):
    arr=sorted(arr)
    n=len(arr)
    return(arr[n-k])
arr=[3,2,1,5,6,4]
k=2
print(kl(arr,k))
