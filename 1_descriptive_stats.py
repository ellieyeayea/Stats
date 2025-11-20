import math

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

def variance(data):
    """
    Compute the population variance of a numeric list.

    Parameters
    ----------
    data : list of float or int
        A list of numeric values. Must not be empty.

    Returns
    -------
    float
        The population variance of the dataset.

    Raises
    ------
    ValueError
        If the input list is empty.

    Examples
    --------
    >>> variance([1, 2, 3])
    0.6666666666666666
    """

    if not data:
        raise ValueError("Input list cannot be empty.")

    mean = ar_mean(data)
    diff_data = [(e-mean)**2 for e in data]
    return sum(diff_data)/len(data)

def std_dev(data):
    """
    Compute the population standard deviation of a numeric list.

    Parameters
    ----------
    data : list of float or int
        A list of numeric values. Must not be empty.

    Returns
    -------
    float
        The population standard deviation of the dataset.

    Raises
    ------
    ValueError
        If the input list is empty.

    Examples
    --------
    >>> std_dev([1, 2, 3])
    0.816496580927726
    >>> std_dev([5, 5, 5])
    0.0
    """

    var = variance(data)
    return math.sqrt(var)