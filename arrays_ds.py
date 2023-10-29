def reverseArray(array):
    array_lenght = len(array)
    for i in range(array_lenght // 2):
        tmp = array[i]
        array[i] = array[array_lenght - 1 - i]
        array[array_lenght - 1 - i] = tmp
    return array