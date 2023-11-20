from random import randrange


def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def sentinelSearch(arr, key):
    n = len(arr)

    last = arr[n - 1]
    arr[n - 1] = key

    i = 0
    while arr[i] != key:
        i += 1

    # Put the last element back
    arr[n - 1] = last

    if (i < n - 1) or (arr[n - 1] == key):
        return i
    else:
        return -1


def binarySearch(arr, key):
    if sorted(arr) != arr:
        raise TypeError("Fibonacci search only works for Sorted arrays")

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def fibonacciSearch(arr: list, key: int) -> int:
    if sorted(arr) != arr:
        raise TypeError("Fibonacci search only works for Sorted arrays")

    n = len(arr)

    # calculating fibonacci
    fib2b = 0
    fib1b = 1
    fib = fib2b + fib1b
    k = 0
    while fib < n:
        fib2b = fib1b
        fib1b = fib
        fib = fib2b + fib1b
        k += 1

    offset = -1

    while fib2b > 0:

        i = min(fib2b + offset, n - 1)

        if arr[i] < key:
            fib = fib1b
            fib1b = fib2b
            fib2b = fib - fib1b
            offset = i

        elif arr[i] > key:
            fib = fib2b
            fib1b -= fib2b
            fib2b = fib - fib1b

        else:
            return i

    if fib1b and arr[n-1] == key:
        return n - 1

    return -1


if __name__ == '__main__':
    arr = []
    failed = 0

    for i in range(10):
        elem = randrange(1, 100)
        # Avoid repeats
        while elem in arr:
            elem = randrange(1, 100)
        arr.append(elem)

    arr.sort()

    print(f"Testing for {arr=}")
    for index, value in enumerate(arr):
        i = linearSearch(arr, value)
        if i != index:
            print(f"Unable to find {value}. Function returned {i}")
            failed += 1

    if failed:
        print(f"Test completed with {failed} failures")
    else:
        print("Test completed successfully")
