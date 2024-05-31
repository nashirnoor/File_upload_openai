def bubble_sort(arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j+1],arr[j] = arr[j],arr[j+1]
        return arr


arr = [3,2,7,5,99,12,11,11,21,101,22,734,30,25]
print(bubble_sort(arr))

