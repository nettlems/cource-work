import Insert_sort
import Bubble_sort
import Select_sort
import random

dim = 40

count_move = [0, 0, 0]
count_compare = [0, 0, 0]

insert_arr = []
bubble_arr = []
select_arr = []
arr = []

for i in range(1, dim + 1):
    insert_arr.append(i)
    bubble_arr.append(i)
    select_arr.append(i)
    arr.append(i)

Count = Insert_sort.insert_sort(insert_arr, dim)
count_move[0] = Count[0]
count_compare[0] = Count[1]

Count = Bubble_sort.bubble_sort(bubble_arr, dim)
count_move[1] = Count[0]
count_compare[1] = Count[1]

Count = Select_sort.select_sort(select_arr, dim)
count_move[2] = Count[0]
count_compare[2] = Count[1]

print("УПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ: ")
print("Начальный массив: " + str(arr))
print(count_move)
print(count_compare)

insert_arr = []
bubble_arr = []
select_arr = []
arr = []

for i in range(dim + 1, 1, -1):
    insert_arr.append(i)
    bubble_arr.append(i)
    select_arr.append(i)
    arr.append(i)

Count = Insert_sort.insert_sort(insert_arr, dim)
count_move[0] = Count[0]
count_compare[0] = Count[1]

Count = Bubble_sort.bubble_sort(bubble_arr, dim)
count_move[1] = Count[0]
count_compare[1] = Count[1]

Count = Select_sort.select_sort(select_arr, dim)
count_move[2] = Count[0]
count_compare[2] = Count[1]

print("ОБРАТНОУПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ: ")
print("Начальный массив: " + str(arr))
print(count_move)
print(count_compare)

insert_arr = []
bubble_arr = []
select_arr = []
arr = []

insert_arr = [random.randint(0, 20) for i in range(dim)]
bubble_arr = [random.randint(0, 20) for i in range(dim)]
select_arr = [random.randint(0, 20) for i in range(dim)]
arr = [random.randint(0, 20) for i in range(dim)]

Count = Insert_sort.insert_sort(insert_arr, dim)
count_move[0] = Count[0]
count_compare[0] = Count[1]

Count = Bubble_sort.bubble_sort(bubble_arr, dim)
count_move[1] = Count[0]
count_compare[1] = Count[1]

Count = Select_sort.select_sort(select_arr, dim)
count_move[2] = Count[0]
count_compare[2] = Count[1]

print("СЛУЧАЙНАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ: ")
print("Случайный массив массив: " + str(arr))
print(count_move)
print(count_compare)