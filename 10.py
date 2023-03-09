
password = input('Введите пароль:')
spec_symbols = ['!', '"', '#', '$', '%',
                '&', "'", '(', ')', '*',
                '+', ',', '-', '.', '/',
                ':', ';', '<', '=', '>',
                '?', '@', '[', ']', '^',
                '_', '`', '{', '|', '}']
count_num = 0
count_spec = 0
count_upp = 0
numeric = 0
specsymbols = 0
upper = 0
crash_pass = list(password)
pwlength = len(password)
for i in range (len(crash_pass)):
    if crash_pass[i].isdigit():
        count_num += 1
    if crash_pass[i].isupper():
        count_upp += 1
    for j in range (len(spec_symbols)):
        if crash_pass[i] == spec_symbols[j]:
            count_spec += 1
numeric = count_num
spec_symbols = count_spec
upper = count_upp
print('Кол-во символов: ',pwlength)
print('Кол-во цифр: ', numeric)
print('Кол-во спецсимволов: ' , spec_symbols)
print('Кол-во заглавных символов: ' , upper)
pwstrength = ((pwlength*5)-20)+(numeric*10)+(spec_symbols*15)+(upper*10)
if pwstrength > 100:
    pwstrength = 100
elif pwstrength < 0:
    pwstrength = 0
print('Уровень надежности вашего пароля: ' , pwstrength)