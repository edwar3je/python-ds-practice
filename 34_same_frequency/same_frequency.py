def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    #convert to strings to become iterable
    str1 = str(num1)
    str2 = str(num2)

    #convert into a list using list comprehension and int()
    lst1 = [int(x) for x in str1]
    lst2 = [int(x) for x in str2]
    
    #create two empty dictionaries
    d1 = {}
    d2 = {}

    #create a dictionary for lst1
    for l1 in lst1:
        if d1.get(l1):
            d1[l1] += 1
        else:
            d1[l1] = 1

    #create a dictionary for lst2
    for l2 in lst2:
        if d2.get(l2):
            d2[l2] += 1
        else:
            d2[l2] = 1
    
    #compare both dictionaries to see if they have the same content (True if yes, False if no)
    if d1 == d2:
        return True
    else:
        return False

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))