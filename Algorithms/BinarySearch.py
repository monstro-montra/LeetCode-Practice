def binary_search_int_list(list: list[int], target: int) -> int: # return an integer (the target)
    low = 0 # low pointer
    high = len(list) - 1 # high pointer
    answer = None # value to return from function

    while low <= high: # loop as long as low pointer is less than or equal to high.
        mid = (low + high) // 2 # calculate the mid point for this iteration.

        if target == list[mid]: # if target is == to value of list at mid
            answer = mid
            return answer # return the answer.
        
        if target < list[mid]: # if target value is less than the value of list at mid
            high = mid - 1 # move high pointer to mid - 1.

        if target > list[mid]: # if the target value is greater than the value of list at mid
            low = mid + 1 # move low pointer to mid + 1.and
    
    return None

if __name__ == "__main__":
    nums_list = [8, 5, 7, 9 , 3, 4, 10, 14, 13, 6, 21]
    nums_list.sort() # binary search requires the list to be already sorted for efficiency.
    print(nums_list)
    target = 4

    print(f"The target, {target}, is at this position in the list:", binary_search_int_list(nums_list, target))