X = int(input("Введите год:"))

if (X % 4 == 0 and X % 100 != 0) or (X % 400 == 0):
    print("Год невисокосный:")
else:
    print("Год високосный")
if X % 100 == 0:
    X = X // 100
    print(X," век")
elif X % 100 != 0:
    X = (X // 100) + 1
    print(X," век")
