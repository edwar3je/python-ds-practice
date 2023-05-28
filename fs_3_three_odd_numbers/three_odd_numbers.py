def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    #determine the length of the list
    length = len(nums)

    #run a boolean to determine if the list is at least 3 (if not, return string "You must provide at least 3 numbers")
    if length < 3:
        return "You must provide at least 3 numbers"
    
    #run a boolean to determine if length is exactly 3, followed by another boolean to determine if total is even or odd
    if length == 3:
        total = nums[0] + nums[1] + nums[2]
        if total % 2 == 1:
            return True
    
    #run a boolean for if length is greater than 3, intialize a few values and run a for loop to inspect total of each slice
    if length >= 3:
        curr_index = 0
        slice_amount = length - 2
        stop_value = curr_index + 3
        for n in range(1, slice_amount):
            slice_lst = nums[curr_index:stop_value]
            total = slice_lst[0] + slice_lst[1] + slice_lst[2]
            if total % 2 == 1:
                return True
            else:
                curr_index += 1
                stop_value += 1
    
    return False
    

print(three_odd_numbers([1, 2, 3, 4, 5]))
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))
print(three_odd_numbers([5, 2, 1]))
print(three_odd_numbers([1, 2, 3, 3, 2]))