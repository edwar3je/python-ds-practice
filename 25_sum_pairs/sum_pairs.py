def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    #provide the length of the list along with the current index
    length = len(nums)
    curr_index = 0
    track_index = 0
    final_index = length - 1

    #create a for loop that iterates between each value in the list, along with another for loop to repeat to see if they add up to goal
    for num in nums:
        for n in range(length):
            if curr_index != track_index:
                if track_index == length:
                    curr_index += 1
                    track_index = 0
                elif nums[curr_index] + nums[track_index] == goal:
                    return (nums[curr_index], nums[track_index])
                elif nums[curr_index] + nums[track_index] != goal:
                    track_index += 1
            else:
                if curr_index == final_index:
                    return ()
                else:
                    track_index += 1

print(sum_pairs([1, 2, 2, 10], 4))
print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([5, 1, 4, 8, 3, 2], 7))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))

        
    

