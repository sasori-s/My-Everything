test = [0, 1, 0, 1]
val = 0
for en, i in enumerate(test, start = 1):
    if i == 1:
        val = val + (2 ** (-en))

exp = int('1100', 2)
print(exp)


