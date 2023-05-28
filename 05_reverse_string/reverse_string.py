def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    #initializes final string to be empty
    final_string = ''

    #converts characters from string into list
    sample_list = [char for char in phrase]

    #reverses the list
    sample_list.reverse()

    #use for loop to convert reversed list back into final string
    for sam in sample_list:
        final_string += sam
    
    return final_string

print(reverse_string('hello'))
print(reverse_string('goodbye'))