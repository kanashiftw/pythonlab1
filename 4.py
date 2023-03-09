words = (
        input("\nВведите текст, который будет разбит на слова: ")
        .replace(".", " ")
        .replace(",", " ")
        .split()
    )
w_7 = [w for w in words if len(w) > 7]
w_4_7 = [w for w in words if 4 <= len(w) <= 7]
w_other = [w for w in words if len(w) < 4]
print("Все слова длинной > 7: ", *w_7)
print("Все слова длинной <= 7 и >= 4:", *w_4_7)
print("Все остальные слова: ", *w_other)