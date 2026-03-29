def merge_sort(arr):
    """
    Perform a recursive Merge Sort on a list of elements.
    
    Merge sort is a stable, divide-and-conquer algorithm that:
    1. Divides the input list into two halves.
    2. Recursively sorts each half.
    3. Merges the two sorted halves into a final sorted array.
    
    Time Complexity: O(n log n) in all cases (best, average, worst).
    Space Complexity: O(n) due to the temporary lists created.
    """
    
    # Check if the input is a list; if not, return it or handle error
    if not isinstance(arr, list):
        return arr

    # BASE CASE: A list with 0 or 1 element is already sorted.
    # This is the 'bottom' of the recursion tree.
    if len(arr) <= 1:
        return arr

    # DIVIDE: Calculate the middle index of the current array.
    # Use floor division (//) to ensure an integer index.
    mid_point = len(arr) // 2

    # RECURSE: Split the array into left and right slices.
    # This continues until we reach the base case (single elements).
    left_side = merge_sort(arr[:mid_point])
    right_side = merge_sort(arr[mid_point:])

    # CONQUER / MERGE: Combine the two sorted halves back together.
    # This helper function does the heavy lifting of comparison.
    return merge_sorted_halves(left_side, right_side)


def merge_sorted_halves(left, right):
    """
    A helper function that merges two pre-sorted lists into one.
    """
    merged_result = []
    left_pointer = 0
    right_pointer = 0

    # Continue looping as long as there are elements in BOTH lists.
    # Compare the current elements at each pointer.
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            # The element in the left list is smaller, so add it first.
            merged_result.append(left[left_pointer])
            left_pointer += 1
        else:
            # The element in the right list is smaller or equal.
            merged_result.append(right[right_pointer])
            right_pointer += 1

    # CLEANUP: After the loop, one list might still have elements left.
    # Since the input lists were already sorted, we just append the remainder.
    
    # Add any remaining elements from the left list.
    while left_pointer < len(left):
        merged_result.append(left[left_pointer])
        left_pointer += 1

    # Add any remaining elements from the right list.
    while right_pointer < len(right):
        merged_result.append(right[right_pointer])
        right_pointer += 1

    # Return the fully merged and sorted list back up the recursion stack.
    return merged_result
