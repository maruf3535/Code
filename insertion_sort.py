def insertionSort(arr):
    j = 1
    while j < len(arr):
        current = arr[j]
        i = j - 1
        while (i >= 0) and (current < arr[i]):
            # swap arr[i], arr[i + 1]
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
            i -= 1
        j += 1

    print(arr)

elments = [2, 3, -1, 1, 10, 8]
insertionSort(arr=elments)
