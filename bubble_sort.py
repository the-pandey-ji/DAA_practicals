arr = [40, 5, 86, 32, 100, 25]
print("Unsorted array")
print(arr)

# Traverse through all array elements
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array by bubble sort")
print(arr)
