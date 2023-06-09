def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    
    #isolate the list from each tuple using index values
    proto_lst1 = a[2]
    proto_lst2 = b[2]

    #create sets from each list
    s1 = {p for p in proto_lst1}
    s2 = {l for l in proto_lst2}

    #use the intersect operator to determine if there are any common interests
    inter = s1 & s2

    #run a boolean to determine if inter is empty (no, True, yes, False)
    if inter == set():
        return False
    else:
        return True

print(friend_date(('Elmo', 5, ['hugging', 'being nice']), ('Sauron', 5000, ['killing hobbits', 'chess'])))
print(friend_date(('Sauron', 5000, ['killing hobbits', 'chess']), ('Gandalf', 10000, ['waving wands', 'chess'])))