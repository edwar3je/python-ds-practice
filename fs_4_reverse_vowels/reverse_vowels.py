def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    #create an entire list consisting only of vowels
    just_vowels_lst = [r for r in s if r in "AaEeIiOoUu"]

    #reverse the list of vowels
    just_vowels_lst.reverse()

    #initialize current_index and string_index to 0
    vowel_index = 0
    string_index = 0

    #create a separate list consisting of the entire string
    entire_str_lst = [r for r in s]

    #run a for loop on entire_str_lst to check for vowels (if yes, it will replace the vowel with the reverse vowel at vowel_index and increase vowel_index by 1)
    for char in entire_str_lst:
        if char in "AaEeIiOoUu":
            entire_str_lst[string_index] = just_vowels_lst[vowel_index]
            vowel_index += 1
        string_index += 1
    
    return "".join(entire_str_lst)
    

print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))