# Function 1
def bubble_sort(items):

    '''Return array of items, sorted in ascending order

    Args:
        items (list): list or list like array of integers

    Returns:
        list: a list of items sorted in ascending order using the bubble sort method
        The bubble sort makes multiple passes through a list.
        It compares adjacent items and exchanges those that are out of order.
        Each pass through the list places the next largest value in its proper place.

    Examples:
        >>> bubble_sort([6,12,1,8,4])
        [1, 4, 6, 8, 12]
        >> bubble_sort([88,22,55,11,66])
        [11, 22, 55, 66, 88]
        >> bubble_sort([101, 505, 707, 303])
        [101, 303, 505, 707]
    '''

    for num in range(len(items)-1,0,-1):
        for i in range(num):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items

# Function 2
def merge_sort(items):

    '''Return array of items, sorted in ascending order

    Args:
        items (list): list or list like array of integers

    Returns:
        list: a list of items sorted in ascending order using the merge sort method
        Merge sort is a recursive algorithm that continually splits a list in half.
        If the list is empty or has one item, it is sorted by definition (the base case).
        If the list has more than one item, we split the list and recursively invoke a merge sort on both halves.
        Once the two halves are sorted, the fundamental operation, called a merge, is performed.

    Examples:
        >>> merge_sort([6,12,1,8,4])
        [1, 4, 6, 8, 12]
        >> merge_sort([88,22,55,11,66])
        [11, 22, 55, 66, 88]
        >> merge_sort([101, 505, 707, 303])
        [101, 303, 505, 707]
    '''

    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1

    return items

# Function 3
def quick_sort(items):

    '''
    Args:
        items (list): list or list like array of integers

    Returns:
        list: a list of items sorted in ascending order using the quick sort method
        A quick sort first selects a value, which is called the pivot value.
        In this instance, it is the first item in the list.
        The role of the pivot value is to assist with splitting the list.
        The actual position where the pivot value belongs in the final sorted list,
        commonly called the split point, will be used to divide the list for subsequent calls to the quick sort.

    Examples:
        >>> quick_sort([6,12,1,8,4])
        [1, 4, 6, 8, 12]
        >> quick_sort([88,22,55,11,66])
        [11, 22, 55, 66, 88]
        >> quick_sort([101, 505, 707, 303])
        [101, 303, 505, 707]
    '''
    def _quicksort(items, low, high):
        # must run partition on sections with 2 elements or more
        if low < high:
            p = partition(items, low, high)
            _quicksort(items, low, p)
            _quicksort(items, p+1, high)
    def partition(items, low, high):
        pivot = items[low]
        while True:
            while items[low] < pivot:
                low += 1
            while items[high] > pivot:
                high -= 1
            if low >= high:
                return high
            items[low], items[high] = items[high], items[low]
            low += 1
            high -= 1
    _quicksort(items, 0, len(items)-1)
    return items
