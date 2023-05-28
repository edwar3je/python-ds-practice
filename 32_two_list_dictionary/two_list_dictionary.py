def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
    """

    #initialize an empty dictionary
    em_dict = {}
   
    #take the length of keys and values respectively
    key_length = len(keys)
    val_length = len(values)
    index = 0

    #note the difference (if positive, append None to values list; if negative, slice values list)
    diff = key_length - val_length

    if diff >= 1:
        for n in range(diff):
            values.append(None)
        for m in range(key_length):
            em_dict[keys[index]] = values[index]
            index += 1
        return em_dict
    elif diff <= -1:
        new_vals = values[:key_length]
        for n in range(key_length):
            em_dict[keys[index]] = new_vals[index]
            index += 1
        return em_dict
    else:
        for n in range(key_length):
            em_dict[keys[index]] = values[index]
            index += 1
        return em_dict 

print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))