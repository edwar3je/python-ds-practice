def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    #initialize empty dictionary for collection
    em_dict = {}

    #run a for loop on nums to populate the dictionary
    for num in nums:
        if em_dict.get(num):
            em_dict[num] += 1
        else:
            em_dict[num] = 1
    
    #run a for loop on em_dict to see if any of the keys have more than 1 occurrence (if yes, provide the key)
    for em in em_dict:
        if em_dict[em] > 1:
            return em
        
    return None

print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))
print(find_the_duplicate([2, 1, 3, 4]))
