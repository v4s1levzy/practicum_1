import random

N = int(input("Количество элементов массива"))
A = [1,5,3,-4]

print(A)

a = 0
for i in range(N):
    if A[i] >= 0:
        break
    if A[i] < 0:
        for i in range(N):
            if A[i-1] < A[i]:
                a = 0
            else:
                a =1
                break
        A[i] = A[i] - 1
        
if (a == 0):
    print("Возрастающая")
    
else:
    print("Убывающая")
