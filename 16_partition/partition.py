def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)

def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    #create two empty lists, a for true, b for false
    a = []
    b = []

    #run a for loop that checks if values meet function (if yes, append to a; if no, append to b)
    for l in lst:
        if fn(l):
            a.append(l)
        else:
            b.append(l)
    
    #return a and b in single list
    return [a, b]

print(partition([1, 2, 3, 4], is_even))
print(partition(["hi", None, 6, "bye"], is_string))