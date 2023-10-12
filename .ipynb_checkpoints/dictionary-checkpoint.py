dict = {
	"Key1": "Key1 text",
	"Key2": "Key2 text",
	"Key3": "Key3 text",
	"Key4": "Key4 text",
}

inpkey = input("Ключ: ")
if inpkey in dict:
	print("Значение ключа: ", dict[inpkey])
else:
	print("Нет ключа [", inpkey, "] в этом словаре")

