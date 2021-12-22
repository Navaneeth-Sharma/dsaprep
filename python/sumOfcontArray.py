# Kadane's algorithm

def MaxsumOfArray(arr):
    i=0
    j=len(arr)-1
    SUM=-1e10
    while(i<=j):
        if sum(arr[i:j+1])>SUM:
            SUM=sum(arr[i:j+1])
            if arr[i]>arr[j]:
                j-=1
            else:
                i+=1
        else:
            if arr[i]>arr[j]:
                j-=1
            else:
                i+=1
    return SUM

print(MaxsumOfArray([1, 2, 3, -2, 5]))