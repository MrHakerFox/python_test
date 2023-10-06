# Манипуляции с цитатой

quote = "Думаю, на мировом рынке можно будет продать штук пять компьютеров."

print("Исходная циатата:")
print(quote)

print("\nОна же в верхнем регистре")
print(quote.upper())

print("\nВ нижнем регистре")
print(quote.lower())

print("\nКак заголовок")
print(quote.title())

print("\nС ма-а-ленькой заменой")
print(quote.replace("штук пять", "несколько миллионов"))

print("\nА вот опять исходная цитата")
print(quote)

print("\nquote.strip()")
print(quote.strip())

input("\nНажмите ENTER, чтобы выйти...")



