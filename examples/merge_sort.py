def merge_sort(arr):
    """
    Recursively splits the list until it has single elements, 
    then merges them back in sorted order.
    """
    # 1. Base case: a list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # 2. Find the midpoint and split the array
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 3. Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Helper function to merge two sorted lists into one.
    """
    sorted_list = []
    i = j = 0

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # If there are remaining elements in 'left', add them
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # If there are remaining elements in 'right', add them
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

# Example Usage:
numbers = [38, 27, 43, 3, 9, 82, 10]
print(f"Sorted List: {merge_sort(numbers)}")
