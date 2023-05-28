def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    
    #convert phrase to lowercase to account for case sensitivity
    con_phrase = phrase.lower()

    #use the .split() method to create a list that has each word as a string
    split_lst = con_phrase.split()

    #create an empty list to add the new strings to
    full_lst = []

    #run a loop over split_lst and use capitalize()
    for sp in split_lst:
        full_lst.append(sp.capitalize())
    
    #use "".join() to update the list into a string
    return " ".join(full_lst)

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))