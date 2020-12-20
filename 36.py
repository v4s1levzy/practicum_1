import array
import random

N = int(input("Введите количество элементов массива "))
M = int(input("Количесвто элементов в группе "))
K = int(input("Позиция K "))
A = [random.randint(0, 100) for i in range(0, N)]
B = [random.randint(0, 100) for b in range(0, M)]

print(A)
print(B)

A.insert(K, B)
print(A)
