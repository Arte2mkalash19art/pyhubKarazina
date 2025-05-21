import numpy as np

# 1)
tensor = np.random.rand(10, 5)
print("Початковий тензор:", tensor)

# 2)
mean_value = np.mean(tensor)
print("\nСереднє значення тензора:", mean_value)

# 3)
filtered = tensor[tensor > mean_value]
print("\nЕлементи, які більші за середнє:", filtered)


# 1)
tensor1 = np.random.rand(5, 5)
tensor2 = np.random.rand(5, 5)

print("\nПерший тензор:", tensor1)

print("\nДругий тензор:", tensor2)

# 2)
mask = tensor1 > tensor2
print("\nМаска (True, якщо tensor1 > tensor2):", mask)

# 3)
result = np.where(mask, tensor1, 0)
print("\nРезультат після маскування:", result)
