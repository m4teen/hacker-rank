def rotateLeft(d, arr):
    """
    Given an array and a number of left rotations, perform the rotations and return the resulting array.

    Parameters:
        d (int): number of left rotations
        arr (list of int): input array

    Returns:
        list of int: the array after performing d left rotations

    Description:
        A left rotation moves each element of the array one position to the left per rotation.
        The element at index 0 wraps around to the end.
        Example: Given arr = [1, 2, 3, 4, 5], d = 4 → result: [5, 1, 2, 3, 4].
    """
    n = len(arr)
    a = arr[::]
    
    for i in range(len(a)):
        arr[i] = a[(d+i) % n]
    
    return arr