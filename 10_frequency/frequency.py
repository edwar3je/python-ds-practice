def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    #initialize count to 0
    count = 0

    #run for loop on list to check if any are equal to the term
    for l in lst:
        if l == search_term:
            count += 1
    
    return count

print(frequency([1,2,3,3,4,5], 3))
print(frequency([5,10,12,13,15], 7))