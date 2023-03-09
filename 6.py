word = (
        input("\nВведите текст: ")
    )
print("Символы встречающиеся однажды:")
for char in word:
  if word.count(char) < 2:
    print (char)