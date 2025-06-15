# Ввод строки от пользователя
text = input("Введите строку: ")

# Разделение строки на слова
words = text.split()

# Поиск и вывод слов, оканчивающихся на букву "я"
print("\nСлова, оканчивающиеся на букву 'я':")
for word in words:
    if word.lower().endswith('я'):
        print(word)
