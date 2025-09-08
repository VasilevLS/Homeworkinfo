f = open("input.txt").readlines()
h = open("output.txt", "w")
s = list(map(int,f[0].split()))
if f[1] == "+":
    h.write(str(sum(s)))
if f[1] == "-":
    h.write(str(s[0]-s[1]))
if f[1] == "*":
    h.write(str(s[0]*s[1]))
