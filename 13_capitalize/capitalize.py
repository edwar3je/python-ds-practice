def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    #convert phrase into a list
    lst = [p for p in phrase]

    #change the first letter in the list to uppercase
    lst[0] = lst[0].upper()
    
    #use the join method to create final phrase and return
    return ''.join(lst)

print(capitalize('python'))
print(capitalize('only first word'))