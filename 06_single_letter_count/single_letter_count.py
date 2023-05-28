def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    
    #convert word and letter to be lowercase to account for case sensitivity
    con_word = word.lower()
    con_letter = letter.lower()
    
    #initialize count as 0
    count = 0

    #run a for loop to check if con_letter appears in con_word, add 1 to count if True
    for con in con_word:
        if con == con_letter:
            count += 1
    
    return count

print(single_letter_count('Hello', 'h'))
print(single_letter_count('Greetings', 'E'))
print(single_letter_count('Aufwiedersehen', 'z'))