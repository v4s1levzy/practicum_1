num = int(input("Введите число для проверки:"))
if num % 2 == 0 and num % 10 == 0:
    print("Число", num, "четно и кратно 10")
else:
    print("Число не соответсвует условию")
