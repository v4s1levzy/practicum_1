import random

N = int(input("Количество элементов массива"))
A = [random.randint(-10,10) for i in range(0, N)]

print(A)
for i in range(N):
    if A[i] < 0:
        A[i] = A[i]**2
print(A)
