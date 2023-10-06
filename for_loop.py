# Слово по буквам
# Демонстрирует применение цикла for к строке

import random

word = input("Введите слово: ")
print("\nВот все буквы вашего слова по порядку:")

for letter in word:
	print(letter)


print("Почитаем: ")
for i in range(10):
	print(i, end = " ")

for i in range(0, 10, 1):
	print(i, end = " ")
	
for _ in range(10):
	print( "Привет!" )
	
print("Длина введённого вами текста составляет", len(word), "символов.")
	
if 'fo' in word:
	print( "fo встречается")
else:
	print("fo не встречается")
	
high = len(word)
low = -len(word)

for i in range(10):
	position = random.randrange(low, high)
	print("word[", position, "]", " -> ", word[position])

