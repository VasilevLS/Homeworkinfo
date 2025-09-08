def tr(x,n):
    y = ""
    n = int(n)
    while x>0:
        y+=str(x%n)
        x //= n
    return y[::-1]
f = open("input1.txt").readlines()
h = open("output.txt", "w")
s = f[0].split()
if f[1][0] == "+":
    h.write(tr(int(s[0], int(f[2]))+int(s[1], int(f[2])), f[2]))
if f[1][0] == "-":
    h.write(tr(int(s[0], int(f[2]))-int(s[1], int(f[2])), f[2]))
if f[1][0] == "*":
    h.write(tr(int(s[0], int(f[2]))*int(s[1], int(f[2])), f[2]))
