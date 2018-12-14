def recursiveBinSearch(lst, key):
    low = 0
    high = len(lst) - 1
    return recursiveBinSearchHelper(lst, key, low, high)


def recursiveBinSearchHelper(lst, key, low, high):
    if low > high:
        return -low - 1

    mid = (low + high) // 2
    if key < lst[mid]:
        return recursiveBinSearchHelper(lst, key, low, mid - 1)
    elif key == lst[mid]:
        return mid
    else:
        return recursiveBinSearchHelper(lst, key, mid + 1, high)


def main():
    lst = [3, 5, 6, 8, 9, 12, 34, 36]
    print(recursiveBinSearch(lst, 3))
    print(recursiveBinSearch(lst, 4))


main()
