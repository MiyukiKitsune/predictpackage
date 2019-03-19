# Function 1
def sum_array(array):

    '''Return sum of all items in array

    Args:
        array (list): list or list-like array of integers

    Returns:
        int: the sum of all the integer values in the array,

    Examples:
        >>> sum_array([1,2,3])
        6
        >> sum_array([4,5,6])
        15
        >> sum_array([7,8,9])
        24
    """'''
    if len(array)== 1:
        return array[0]
    else:
        return array[0]+sum_array(array[1:])

# Function 2
def fibonacci(n):

    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Function 3
def factorial(n):
    """
    Returns n!

    Args:
        n (int): positive integer or 0 for which to calculate factorial

    Returns:
        int: the factorial of n,
             equal to the product of an integer and all the integers below it

    Examples:
        >>> factorial(1)
        1
        >> factorial(2)
        2
        >> factorial(3)
        6
    """

    if n >= 1:
        return n * factorial(n - 1)
    else:
        return 1

# Function 4
def reverse(word):

    '''
    Return word in reverse

    Args:
        word (str): a string of the word you want reversed

    Returns:
        str: a string containing all elements of the input string in reverse order

    Examples:
        >>> reverse('firefly')
        ylferif
        >> reverse('serenity')
        ytineres
        >> reverse('miranda')
        adnarim
    '''

    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]
