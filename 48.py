import random
import numpy

N = int(input("Количество элементов в массиве"))
A = [random.randint(-2, 2) for i in range(0, N)]

print(A)

for i in range(N):
    if A[i] == 0:
        A[i] = A[i-1] + A[i-2]
        
print(A)
