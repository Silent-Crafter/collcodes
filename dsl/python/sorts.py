from tester import Tester


def quickSort(arr, low, high):
    if low >= high:
        return

    # divide and conquer
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[high], arr[i + 1] = arr[i + 1], arr[high]
    mid = i + 1
    # sort left half
    quickSort(arr, low, mid - 1)
    # sort right half
    quickSort(arr, mid + 1, high)


def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        j = gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j < n:
            i = j - gap  # This will keep help in maintain gap value

            while i >= 0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i + gap] > arr[i]:

                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]

                i = i - gap  # To check left side also
                # If the element present is greater than current element
            j += 1
        gap = gap // 2


def bubbleSort(arr: list):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def selectionSort(arr):
    n = len(arr)

    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if arr[j] <= arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]


def wrapper(arr, sorting_algorithm='quickSort'):
    if sorting_algorithm == 'quickSort':
        quickSort(arr, 0, len(arr) - 1)

    elif sorting_algorithm in ['bubbleSort', 'insertionSort', 'shellSort', 'selectionSort']:
        eval(sorting_algorithm)(arr)


def testmany(n, sortingalgo):
    # test for an array of length from 1 to 8
    for i in range(1, n):
        t = Tester(i, output=False)
        print(f"For an array of length {i}:", end='\t')
        t.test(lambda x: wrapper(x, sorting_algorithm=sortingalgo))
        del t


def testonce(len, sortingalgo):
    t = Tester(len, output=False)
    t.test(lambda x: wrapper(x, sorting_algorithm=sortingalgo))


if __name__ == '__main__':
    test_algo = ['selectionSort', 'shellSort', 'bubbleSort', 'insertionSort']

    for algo in test_algo:
        print(f'[{algo}]', end='\t\t')
        testonce(5, algo)


