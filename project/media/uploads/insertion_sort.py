def insertion_sort(arr):
     for i in range(1,len(arr)):
        value = arr[i]
        j = i-1
        while j>=0 and value<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = value
     return arr


arr = [6,2,8,1,2,10,120,22,23]
print(insertion_sort(arr))

 
