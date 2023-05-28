def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    #create a set to get all distinct ages
    new_set = {age for age in ages}

    #convert set back into a list to use sort() method to sort by ascending age
    new_ages = [a for a in new_set]
    
    #use the sort() method on ages to sort by ascending age
    new_ages.sort()

    #determine the length of the new list, then create a slice of the last two ages and return a tuple of the first two values
    length = len(new_ages)
    start_value = length - 2
    final_ages = new_ages[start_value:length] 
    return (final_ages[0], final_ages[1])

print(two_oldest_ages([1, 2, 10, 8]))
print(two_oldest_ages([6, 1, 9, 10, 4]))
print(two_oldest_ages([1, 5, 5, 2]))