def find_armstrong_numbers(limit):
    print(f"Числа Армстронга от 1 до {limit}:")
    for num in range(1, limit + 1):
        digits = str(num)
        n = len(digits)
        total = 0
        for d in digits:
            total += int(d) ** n
        if total == num:
            print(num)

def geom_term(a1, q, n):
    if n == 1:
        return a1
    else:
        return geom_term(a1, q, n - 1) * q

def main():
    k = int(input("Введите верхнюю границу для чисел Армстронга: "))
    find_armstrong_numbers(k)

    print()
    a1 = float(input("Введите первый член геометрической прогрессии a1: "))
    q = float(input("Введите знаменатель прогрессии q: "))
    n = int(input("Введите номер члена n: "))
    result = geom_term(a1, q, n)
    print(f"{n}-й член геометрической прогрессии: {result}")

if __name__ == "__main__":
    main()
