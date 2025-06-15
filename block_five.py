def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def find_amicable_pairs(limit):
    pairs = set()
    for a in range(2, limit + 1):
        b = sum_of_divisors(a)
        if b > a and b <= limit:
            if sum_of_divisors(b) == a:
                pairs.add((a, b))
    return pairs

def digital_root(n):
    if n < 10:
        return n
    digit_sum = sum(int(d) for d in str(n))
    return digital_root(digit_sum)

def main():
    print("Выберите действие:")
    print("1 - Найти пары дружественных чисел до N")
    print("2 - Найти цифровой корень числа")
    choice = input("Введите номер действия (1 или 2): ")

    if choice == "1":
        n = int(input("Введите верхний предел (N): "))
        result = find_amicable_pairs(n)
        if result:
            print(f"\nПары дружественных чисел до {n}:")
            for a, b in result:
                print(f"{a} и {b}")
        else:
            print("Дружественные пары не найдены.")
    elif choice == "2":
        number = int(input("Введите натуральное число: "))
        root = digital_root(number)
        print(f"Цифровой корень числа: {root}")
    else:
        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
