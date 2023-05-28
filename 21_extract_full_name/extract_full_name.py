def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    #initialize an empty list
    full_lst = []

    #run a for loop on the list to isolate each dictionary, then extract each value of the object to full_name and append to full_lst
    for pe in people:
        full_name = pe['first'] + ' ' + pe['last']
        full_lst.append(full_name)
    
    return full_lst

print(extract_full_names([{'first': 'Ada', 'last': 'Lovelace'}, {'first': 'Grace', 'last': 'Hopper'}]))