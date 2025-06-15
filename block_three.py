text = input("Введите строку с одной парой скобок: ")

start = text.find('(')
end = text.find(')')

if start != -1 and end != -1 and start < end:
    inside = text[start+1:end]
    print("Символы внутри скобок:", inside)
else:
    print("В строке нет корректной пары скобок.")
