inp = "1 2 3 4 5"
a = list(map(int, inp.split()))
b = 1
for i in a:
    b *= i
print(b ** (1 / len(a)))
