# Selection Sort


def selectionSort(lst):
    # find the minimum
    for i in range(len(lst) - 1):
        currentMin = lst[i]
        currentMinIndex = i

    for j in range(i + 1, len(lst)):
        if currentMin > lst[j]:
            currentMin = lst[j]
            currentMinIndex = j

    if currentMinIndex != i:
        lst[currentMinIndex] = lst[i]
        lst[i] = currentMin

    return lst


yo = [1, 9, 4.5, 10.6, 5.7, -4.5]

print(selectionSort(yo))
