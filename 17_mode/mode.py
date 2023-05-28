def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    #initialize an empty dictionary for storing data
    dt = {}

    #initialize max as 1
    max = 1

    #run a for loop on the list to add 1 for each occurrence of a number to the dictionary
    for num in nums:
        if dt.get(num):
            dt[num] += 1
        else:
            dt[num] = 1
    
    #run a for loop on the dictionary to check if the value of any keys has exceeded 1, then change max to that value and return
    for d in dt:
        if dt[d] > max:
            max = dt[d]
    
    #run one more loop to determine the key and then convert to string to return
    con_key = {i for i in dt if dt[i] == max}

    return con_key
    


print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))