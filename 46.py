import random
import numpy

N = int(input("Количество элементов массива"))
T = int(input("Положительное число"))
A = [random.randint(-10, 10) for i in range(0, N)]

print(A)

S = 0
for i in range(N):
    if A[i] > 0:
        S = S + A[i]
K = T/S
for i in range(N):
    if A[i] > 0:
        A[i] += (A[i]*K)
        
print(K)
print(A)
