def frange (start, end, step):
    for i in range(start, end):
        while i < end:
            i+=step
            yield i
for x in frange (1, 5, 0.1):
    print(x)