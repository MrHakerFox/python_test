message = input( "Введите текст: ")
new_message = ""
VOWELS = "aeiouаеёиоуыэюя"
print()
for letter in message:
	if letter.lower() not in VOWELS:
		new_message += letter
		
print("Создана новая строка: ", new_message)
