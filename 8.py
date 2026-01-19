import random

list = [random.randint(1,100) for _ in range(5)]
print(f'Исходный список:', *list)
min_value = min(list)
min_index = list.index(min_value)
list[0], list[min_index] = list[min_index], list[0]

print(f'Список после обмена:', *list)