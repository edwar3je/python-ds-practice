def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    #initialize final list
    final_list = []
    #convert phrase into a list
    lst = [char for char in phrase]

    #run for loop to check casing and add appropriate casing to final_phrase
    for l in lst:
        if l == to_swap.lower() or l == to_swap.upper():
            if l == to_swap.lower():
                final_list.append(l.upper())
            else:
                final_list.append(l.lower())
        else:
            final_list.append(l)
    
    #create final_phrase using .join() method and return
    final_phrase = "".join(final_list)
    return final_phrase

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))