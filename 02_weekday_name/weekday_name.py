def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    
    #a list of the days of the week
    weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    # converts day_of_week to integer if it's a float (or keeps it)
    initial_index = int(day_of_week)
    
    #converts integer to index for list
    index_provided = initial_index - 1

    #prints day of the week based on if index works, or None if it doesn't
    if index_provided > -1 and index_provided <= 6:
        return weekday[index_provided]
    
    return None

print(weekday_name(6))

print(weekday_name(0))