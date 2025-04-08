#Prac 1
import numpy as np
np.random.seed(42)  
arr = np.random.randint(2, 12, (3, 4))
print("Масив:\n", arr)

cols = np.all(arr % 2 != 0, axis=0)
cols_indices = np.where(cols)[0]
print("Стовпці без парних елементів:", cols_indices)

count_in_range = np.sum((arr > 5) & (arr < 8))
print("Перше завдання кількість чисел у (5, 8):", count_in_range)

#Prac 2
np.random.seed(42)  
arr = np.random.randint(1, 5, (3, 5))
print("Масив:\n", arr)

sum_cols = np.sum(arr, axis=0)
max_col = np.argmax(sum_cols)
print("Друге завдання стовпець з максимальною сумою:", max_col)