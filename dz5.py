# 1
# s = input().split("student_")
# d = dict()
# for i in s[1:]:
#     d[i[:3]] = int(i[3:])
# print(d)
# r = []
# for i in d.keys():
#     if d[i] == max(d.values()):
#         r.append(i)
# print(*r, sep="-")



# 2
# import numpy as np
# r, a = input().split()
# r, a = int(r), int(a)
# l = 2*np.pi*r
# S1 = np.pi*r**2
# S2 = a**2
# print(f"Длина окружности равно {round(l, 2)}. Площадь круга составляет {round(S1/S2*100, 2)}% от площади квадрата.")

# 3
# a, b = input().split()
# print(f"{a[1]+a[0]+a[2:]}-{b[1]+b[0]+b[2:]}")

# 4
# s = input()
# def f(s):
#     if len(s)>=4:
#         k = 0
#         for i in s:
#             if i == i.upper(): k+=1
#         if k>=3:
#             return s.upper()
#     return s
#
# print(f(s))

# 5
# def wrap_in_tag(tag, text):
#     valid_tags = ['a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's']
#
#     if tag not in valid_tags:
#         return "Введён неверный тег"
#     return f"<{tag}>{text}</{tag}>"
# a = input()
# b = input()
#
# print(wrap_in_tag(a, b))

# 6
# s = input()
# if len(s) <= 2:
#     print(ord(s[0]))
# elif len(s)<10 and len(s)%2==0:
#     print(ord(s[0]) + ord(s[len(s)//2 - 1]) + ord(s[-1]))
# elif len(s)<10 and len(s)%2!=0:
#     print(ord(s[0]) + ord(s[len(s)//2 ]) + ord(s[-1]))
# else:
#     print(ord(s[-1]))
