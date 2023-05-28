def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    #initialize an empty dictionary
    letter_dict = {}

    #run a for loop to examine phrase and add 1 to letter in dictionary if it exists, and assign 1 if it doesn't exist
    for p in phrase:
        if letter_dict.get(p) is None:
            letter_dict[p] = 1
        else:
            letter_dict[p] += 1
    
    return letter_dict

print(multiple_letter_count('Hello'))
print(multiple_letter_count('Aufwiedersehen'))