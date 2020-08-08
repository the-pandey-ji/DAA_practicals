arr = [40, 5, 86, 32, 100, 25]
print("Unsorted array")
print(arr)

# Traverse through all array elements
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    print (arr)

print("Sorted array by insertion sort")
print(arr)
