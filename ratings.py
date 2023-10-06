scores = []
choice = None

while choice != "0":
	print( """0. Выход.
		   1. Показать рекорды.
		   2. Добавить рекорд.
		   """);
	choice = input("Ваш выбор: ")
	if choice == "0":
		print( "Досвидос" );
	elif choice == "1":
		print( "Рекорды\n")
		print( "Имя\tРезультат")
		for entry in scores:
			score, name = entry
			print(name, "\t", score)
	elif choice == "2":
		name = input("Введите имя игрока")
		score = int(input("Впишите его результат"))
		entry = (score, name)
		scores.append(entry)
		scores.sort(reverse=True)
		scores = scores[:5] # only five records
	else:
		print( "Выбор ", choice, "не понятен!" );

		

