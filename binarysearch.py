def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Get input from user to create the sorted array
num_elements = int(input("Enter the number of elements in the array: "))
array = []

print("Enter the elements of the sorted array (space-separated):")
elements = input().split()
for element in elements:
    array.append(int(element))

# Get input from user for the target element
target = int(input("Enter the target element to search: "))

# Perform binary search
result = binary_search(array, target)

# Print the result
if result != -1:
    print("Element", target, "is found at index", result)
else:
    print("Element", target, "is not found in the array.")
