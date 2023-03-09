lst = [4, 6, 8, 6, 10]
for i, item in enumerate(lst):
        if i != 0 and lst[i-1] > item:
            print(False)
            break
        if i+1 == len(lst):
            print(True)