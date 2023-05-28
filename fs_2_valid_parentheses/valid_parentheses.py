def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    #create a short dictionary containing keys to represent parentheses (0 for "(" and 1 for ")")
    num_of_char = {"(": 0, ")": 1}

    #run a loop on the string to convert it into a list of values using num_of_char
    lst = [num_of_char[p] for p in parens]

    #determine the length of lst and calculate last index
    length = len(lst)
    last_index = length - 1
    
    #create a separate dictionary for occurrences (initialize empty)
    occurrences = {}

    #run a loop on lst to count number of occurrences of 0 and 1
    for l in lst:
        if occurrences.get(l):
            occurrences[l] += 1
        else:
            occurrences[l] = 1
    
    #provide boolean
    if occurrences[0] == occurrences[1]:
        if lst[0] == 0 and lst[last_index] == 1:
            return True
        else:
            return False
    else:
        return False

print(valid_parentheses("()"))
print(valid_parentheses("()()"))
print(valid_parentheses("(()())"))
print(valid_parentheses(")()"))
print(valid_parentheses("())"))
print(valid_parentheses("((())"))
print(valid_parentheses(")()("))