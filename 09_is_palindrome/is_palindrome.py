def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    #initialize reverse_string as empty
    reverse_string = ''
    
    #convert phrase/string to lowercase for case-sensitivity
    lower_string = phrase.lower()
    
    #remove spacing in converted phrase/string
    no_space_string = lower_string.replace(' ','')

    #convert string to list, then reverse list and convert back to string
    sample_list = [no for no in no_space_string]
    sample_list.reverse()
    for sam in sample_list:
        reverse_string += sam
    
    #compare regular string against reverse string
    if no_space_string == reverse_string:
        return True
    else:
        return False

print(is_palindrome('Noon'))
print(is_palindrome('Hiya'))
print(is_palindrome('Taco cat'))

