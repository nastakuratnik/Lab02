# Задача 1: Средняя плотность населения по области

population = []
area = []

print("Введите данные для 12 районов:")

for i in range(12):
    p = float(input(f"Количество жителей в районе {i+1} (тыс. чел.): "))
    a = float(input(f"Площадь района {i+1} (км2): "))
    population.append(p)
    area.append(a)

total_population = 0
total_area = 0

for i in range(12):
    total_population += population[i]
    total_area += area[i]

average_density = total_population / total_area

print(f"\nСредняя плотность населения по области: {average_density:.2f} тыс. чел./км²")


# Задача 2: Когда подарок дяди превысит 100$

age = 1
gift = 1

while gift <= 100:
    age += 1
    gift = gift * 2 + age

print(f"\nПодарок превысит 100$ на {age}-й день рождения.")
