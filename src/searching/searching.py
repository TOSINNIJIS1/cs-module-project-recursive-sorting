# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if target <= end:
        mid_point = (start + end) // 2
        if arr[mid_point] == target :
            return mid_point

        elif target < arr[mid_point]:
            small_end = mid_point - 1
            return binary_search(arr, target, start, small_end)  

        else:
            large_start = mid_point + 1
            return binary_search(arr, target, large_start, end) # -- move to base case

    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
