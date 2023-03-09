import random
def randm(n):
    i = 0
    while i < n:
        yield random.randint(1, 100)
        i += 1
n =random.randint(1,100)
array = list(randm(n))
for i in range(n):
    if i**2 > n:
        ziro = [0 for ziro  in range(i**2)]
        array.extend(ziro)
        break
print(array)