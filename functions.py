def display(message):
	print(message)

def give_me_five():
	return 5

def ask_yes_no(question):
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response


display("Сообщение!\n")

nubmer = give_me_five()
print("Вот что возвратила функция give_me_five(): ", give_me_five())

answer = ask_yes_no("Поажулйста, скажите да или нет!")
print("Введено: ", answer)

