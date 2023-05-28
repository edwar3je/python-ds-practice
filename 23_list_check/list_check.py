def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    
    #run a for loop and use isinstance to check if each individual value is a list
    for l in lst:
        if not isinstance(l, list):
            return False
    
    return True

print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))