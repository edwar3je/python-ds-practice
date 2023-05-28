def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    #initialize empty dictionary
    v_count = {}

    #convert phrase to lowercase to be case-sensitive
    con_phrase = phrase.lower()

    #iterate over the string and check to see if it is in vowels string (if yes, add to dictionary)
    for ph in con_phrase:
        if ph in 'aeiou':
            if v_count.get(ph) is None:
                v_count[ph] = 1
            else:
                v_count[ph] += 1
    
    return v_count

print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))