# Задача 1: Проверка на повторяющиеся элементы с выводом индексов

arr1 = [3, 5, 7, 3, 9, 5, 1, 7, 4]

found = {}
duplicates = {}

for i, num in enumerate(arr1):
    if num in found:
        if num not in duplicates:
            duplicates[num] = [found[num]]
        duplicates[num].append(i)
    else:
        found[num] = i

if duplicates:
    print("Повторяющиеся элементы и их индексы:")
    for val, idx_list in duplicates.items():
        print(f"Элемент {val} найден на индексах {idx_list}")
else:
    print("Повторяющихся элементов нет.")

print("\n" + "-"*30 + "\n")

# Задача 2: Замена элементов меньше 15 на удвоенные значения

arr2 = [12, 20, 5, 17, 8, 25, 14, 15]

for i in range(len(arr2)):
    if arr2[i] < 15:
        arr2[i] = arr2[i] * 2

print("Преобразованный массив:")
print(arr2)
