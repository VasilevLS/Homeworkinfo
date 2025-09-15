#1
# s = "5 1 2 3 4"
# a = list(map(int, s.split()))
# N = a[0]
# for i in range(1,N+1):
#     if i in a[1:]:
#         continue
#     else:
#         print(i)
#         break

# 2
# n, s = "6 AB0TAEL0ANANAB0EVO0SANAN".split()
# n = len(s)//int(n)
# r = ""
# for i in range(0,len(s),n):
#     r += s[i:i+n][::-1]
# print(r)


# 3
# for s in ["ABC", "ABA", "EA3", "AMA"]:
#     T = False
#     Z = False
#     U = True
#     if s == s[::-1]:
#         T = True
#     v = s.replace("E", "3").replace("J", "L").replace("S","2").replace("Z","5")
#     for i in v:
#         if i not in "AHIMOTUVWXY183L25":
#             U = False
#     if v == v[::-1] and U:
#         Z = True
#     if T and Z:
#         print(f"{s} is a mirrored palindrome.")
#     elif T and not Z:
#         print(f"{s} is a regular palindrome")
#     elif not T and Z:
#         print(f"{s} is a mirrored string.")
#     else:
#         print(f"{s} is not a palindrome.")


# 4
# t = "1 2 3 4 5".split()
# for i in range(1,len(t),2):
#     print(t[i], t[i-1], end=" ")
# if len(t)%2!=0: print(t[-1])

# 5
# s = "1 2 3 4 5"
# print(s[-1], s[:-1])

#6
# s = "1 2 2 3 4 3 5 55 6 7 6 5".split()
# for i in s:
#     if s.count(i)==1:
#         print(i, end=" ")

# 7
# s = "1 2 3 2 3 3".split()
# k = 0
# j = 0
# for i in s:
#     if s.count(i)>k:
#         k = s.count(i)
#         j = i
# print(j)

#8
# def mediana(r):
#     a = sum(r)/len(r)
#     med = r[0]
#     dmed = abs(med - a)
#     for i in r[1:]:
#         d = abs(i - a)
#         if d < dmed:
#             dmed = d
#             med = i
#     return med
#
#
# n = 5
# r = list(map(int, "3 1 5 2 4".split()))
# print(mediana(r))

# 9
# s = "В лесу родилась ёлочка! В лесу росла? Зимой и летом стройная... Зеленая была?! Зелёная. Была!"
# s = s.replace("...", "1").replace("?!", "1").replace("?","1").replace("!","1").replace(".", "1")
# print(s.count("1"))

# 10
# s = "Привет, я - Лунтик, я упал с Луны"
# l = 'ёаиуеэыяою'
# r = ""+s[0]
# for i in range(1,len(s)):
#     if s[i-1] not in l and s[i] in l:
#         r = r + s[i] + "c" + s[i]
#     else:
#         r = r + s[i]
# print(r)
