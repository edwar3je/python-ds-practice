def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

    #convert string to account for case sensitivity
    con_word = word.lower()

    #create a dictionary that includes each character position
    char_position = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    #initialize a result list and make it empty
    res_lst = []

    #initialize an empty total value for later
    total = 0
    
    #create a list from the word using list comprehension
    lst = [c for c in con_word]

    #run a for loop on the list and append the value of the character position (using char_position) to res_lst
    for l in lst:
        if char_position.get(l):
            res_lst.append(char_position[l])
    
    #add all the values from the list
    for r in res_lst:
        total += r
    
    #use boolean to determine if total is even (False) or odd (True)
    if total % 2 == 1:
        return True
    else:
        return False

print(is_odd_string('a'))
print(is_odd_string('A'))
print(is_odd_string('aaaa'))
print(is_odd_string('AAaa'))
print(is_odd_string('amazing'))
print(is_odd_string('Bananas'))