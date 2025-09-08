N, b, c = 1001, 2, 8
N = int(str(N), b)
s = ''
while N != 0:
    s += str(N % c)
    N //= c
print(int(s[::-1]))
