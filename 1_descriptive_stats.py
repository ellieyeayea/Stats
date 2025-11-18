# Manual Implementations of Arithmetic Mean, Median, Mode, Variance, and Standard Deviation.

def ar_mean(data):
    """
    Calculate the arithmetic mean of a list of numeric values.

    Parameters
    ----------
    data : list of float or int
        A list containing numeric values. Must not be empty.

    Returns
    -------
    float
        The arithmetic mean of the provided numbers.

    Raises
    ------
    ValueError
        If the input list is empty.

    Examples
    --------
    >>> ar_mean([1, 2, 3, 4])
    2.5
    """

    if not data:
        raise ValueError("Input list cannot be empty.")

    return sum(data)/len(data)

def median(data):
    """
    Calculate the median of a list of numeric values.

    Parameters
    ----------
    data : list of float or int
        A list containing numeric values. Must not be empty.

    Returns
    -------
    float
        The median of the provided numbers.

    Raises
    ------
    ValueError
        If the input list is empty.

    Examples
    --------
    >>> median([1, 2, 3, 4, 5])
    3
    >>> median([1, 2, 3, 4, 5, 6])
    3.5
    """

    if not data:
        raise ValueError("Input list cannot be empty.")

    data_len = len(data)
    # If the data length is even, get the middle point
    # If the data length is even, get the 2 middle points and average them
    if data_len % 2 == 0:
        mid = int(data_len/2)
        med1 = data[mid-1]
        med2 = data[mid]
        med = (med1 + med2) / 2
    else:
        med = data[int(data_len/2)]

    return med

def mode(data):
    """
    Identify the mode(s) of a list.

    Parameters
    ----------
    data : list of Any.
        A list containing dataset elements. Must not be empty.

    Returns
    -------
    a list of Any
        A list containing the mode value or values from the provided dataset.

    Raises
    ------
    ValueError
        If the input list is empty.

    Examples
    --------
    >>> mode([1, 2, 3, 4, 5, 1, 2])
    [1, 2]
    >>> mode(["Apple", "Apple", "Orange", "Melon"])
    ["Apple"]
    """

    if not data:
        raise ValueError("Input list cannot be empty.")

    tally = {}

    for e in data:
        # If element exists in dict, then set value = value + 1
        # If element not found, then set value = 1
        tally[e] = tally.get(e, 0) + 1

    # Get the highest number of tally from dict
    max_tally = max(tally.values())

    # Return all the elements with the highest tally
    return [key for key, value in tally.items() if value == max_tally]


# data = [1.05, 2.3, 3.6, 4.8, 7.9, 10.6]
# print(ar_mean(data))
# print(median(data))
# print(median([1, 2, 3, 4, 5, 6]))
# print(median([1, 2, 3, 4, 5]))

# data = ["a", "b", "c", "a"]
data = [1, 2, 3, 4, 5, 6, 6, 1, 3]
print(mode(data))
print(mode(["Apple", "Apple", "Orange", "Melon"]))
print(mode([1, 2, 3, 4, 5, 1, 2]))
