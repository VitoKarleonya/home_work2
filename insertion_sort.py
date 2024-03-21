def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Пример использования
array = [12, 11, 13, 5, 6]
sorted_array = insertion_sort(array)
print("Отсортированный массив:", sorted_array)
