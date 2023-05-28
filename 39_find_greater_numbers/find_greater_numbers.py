def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1

    return count

def myfind_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    #my attempt at trying to define the function

    #initialize count as 0
    count = 0

    #initialize count_index and track_index
    count_index = 0
    track_index = 0

    #calculate length and end_index
    length = len(nums)
    end_index = length - 1

    if length == 1 or nums == []:
        return count
    else:
        for n in nums:
            for m in range(length):
                if count_index == track_index:
                    if count_index == end_index:
                        return count
                    else:
                        track_index += 1
                elif count_index < track_index:
                    if nums[count_index] < nums[track_index]:
                        count += 1
                        track_index += 1
                    else:
                        track_index += 1
                elif count_index > track_index:
                    track_index += 1

print(find_greater_numbers([1, 2, 3]))
print(find_greater_numbers([6, 1, 2, 7]))
print(find_greater_numbers([5, 4, 3, 2, 1]))
print(find_greater_numbers([]))