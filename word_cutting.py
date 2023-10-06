
word = None

while word != "":
	word = input( "Введите слово (пустое для выхода): ")
	if word:
		start = int(input("Начальная позиция: "))
		finish = int(input("Конечная позиция: "))
		print("Выборка строки от", start, "до", finish, "будет : ", word[start:finish])


