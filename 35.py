N = int(input("Введите количество элементов массива "))
A = int(input("Количесвто элементов в группе"))
C = int(input("Позиция C"))
B = int(input("Позиция B"))
a = [random.randint(0, 100) for i in range(0, N)]

print(a)
for i in range(N):
    a[C: C + A], a[B: B + A] = a[C: C + A], a[B: B + A]
    
print(a)
