A = int(input("Введите длину - "))
B = int(input("Введите ширину - "))
C = int(input("Введите высоту - "))
M = int(input("Ширина дверного проёма - "))
H = int(input("Высота дверного проёма - "))
if ((C <= H and B <= H)
    or (C <= H and A <= H)
    or (A <= H and B <= H)):
    print("Коробка пройдет.")
else:
    print("Коробка не пройдет.")
