def isSorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
                return False
    return True


def main():
    lst = input('Enter a list: ')
    if isSorted(lst):
        print('The list is already sorted...')
    else:
        print('The list is not sorted...')


main()

# 1 1 3 4 4 5 7 9 10 30
