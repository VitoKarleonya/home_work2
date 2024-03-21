def binary_search(target, generator):
    left = 0
    right = len(generator) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if generator[mid] == target:
            return mid
        elif generator[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Пример использования со списком, вроде бы тоже отсортированый массив
target = int(input('Введите число которое ищете: '))
number = int(input('Введите диапазон: '))
generator = (x for x in range(number))  # Генератор для чисел
generator_list = [x for x in generator]  # Преобразуем генератор в список
result = binary_search(target, generator_list)  # Применяем бинарный поиск к списку
if result != -1:
    #отформатированные строки с выводом актуальных значений, полность не понял, но работает
    
    print(f"Число {target} найдено в позиции {result}.")
else:
    print(f"Число {target} не найдено в последовательности.")
