
arr = [40, 5, 86, 32, 100, 25]
print("Unsorted array")
print(arr)
# Traverse through all array elements
for i in range(len(arr)):
    # Find the minimum element in remaining
    minIndex = i
    for j in range(i + 1, len(arr)):
        if arr[minIndex] > arr[j]:
            minIndex = j

        # Swap  minimum value element with the first element
    arr[i], arr[minIndex] = arr[minIndex], arr[i]

print("Sorted array")
print(arr)
