
#Function to return the count of number of elements in union of two arrays.
def doUnion(a,n,b,m):
    arr=[0]*max(max(a)+1, max(b)+1)
    for i in range(n):
        arr[a[i]]=1
    for j in range(m):
        arr[b[j]]=1
    return sum(arr)

print(doUnion([1,3,5,6],4,[1,2],2))

