while True:
    number_card = input("Введите номер карты из 16 цифр:")
    if (number_card.isdigit() and len(number_card) == 16):
        break
for i in range(0, 16):
    if (i % 4 == 0):
        print(" ", end="")
    if (i <= 3 or i >= 12):
        print(number_card[i], end="")
    else:
        print("*", end="")