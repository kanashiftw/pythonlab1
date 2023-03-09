words = (
        input("\nВведите текст, который будет разбит на слова: ")
        .replace(".", " ")
        .replace(",", " ")
        .split()
    )
for w in words:
    if w[0].isupper():
        print(w.upper(),end=' ')
    else:
        print(w, end=' ')