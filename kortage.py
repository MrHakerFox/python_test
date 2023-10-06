inventory = ()

if not inventory:
	print("Вы безоружны")

input("\nНажмите Enter, чтобы продолжить...")


inventory = (
	"меч",
	"кольчуга",
	"щит",
	"целебное снадобье")

print("\nСодержимое кортежа:")
print(inventory)

print("\nИтак, в вашем арсенале:")
for item in inventory:
	print(item)

print("\nДлина кортежа:", len(inventory))

