nested = ["раз", ("два", "три"), ["четыре", "пять", "шесть"]]

print("Печатаем список:", nested)

print("Печатаем поэлементно:")
for item in nested:
	print(item)

print("Печатаем совсем поэлементно")
for item in nested:
	for it in item:
		print(it)

print("Распаковка последовательности")
name, score = ("Иван Иванович", 1000)
print(name)
print(score)

