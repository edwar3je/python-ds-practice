def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    #use list comprehension to return a list of values that are True
    return [val for val in lst if val]

def mycompact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    #my attempt at creating the function

    #initialize true_list as empty list
    true_list = []

    #run a for loop to check if any of the values are true and append the ones that are to the true_list
    for l in lst:
        if bool(l) == True:
            true_list.append(l)
    
    return true_list

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))