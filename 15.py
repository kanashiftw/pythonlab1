def pre_process(a = 0.97):
    def deckor(func):
        def wrapper(s):

            for i in range(len(s)):
                s[i] = s[i] - a * s[i - 1]
        return wrapper
    return deckor


@pre_process(a = 1)
def plot_signal(s):
    for sample in s:
        print(sample)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
plot_signal(data)

