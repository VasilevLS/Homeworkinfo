# import math
# a, b = input().split()
# a, b = int(a), int(b)
# nod = math.gcd(a,b)
# if a<0 and b>0 or a>0 and b<0:
#     print(-1*abs(a//nod), abs(b//nod))
# else:
#     print(abs(a // nod), abs(b // nod))
import random

# x1, y1, x2, y2, x3, y3, x4, y4 = map(int,input().split())
# k1 = (y2-y1)/(x2-x1)
# k2 = (y4-y3)/(x4-x3)
# b1 = y1 - k1*x1
# b2 = y4 - k2*x4
# e = True
# if x1<x2:
#     for x in range(1000*x1,1000*x2):
#         x/=1000
#         if x3 < x4:
#             if x3 <= x <= x4:
#                 if k1*x+b1 == k2*x+b2:
#                     print("YES")
#                     e = False
#                     break
#         if x4 < x3:
#             if x4 <= x <= x3:
#                 if k1*x+b1 == k2*x+b2:
#                     print("YES")
#                     e = False
#                     break
# if x1>x2:
#     for x in range(1000*x2,1000*x1):
#         x/=1000
#         if x3 < x4:
#             if x3 <= x <= x4:
#                 if k1*x+b1 == k2*x+b2:
#                     print("YES")
#                     e = False
#                     break
#         if x4 < x3:
#             if x4 <= x <= x3:
#                 if k1*x+b1 == k2*x+b2:
#                     print("YES")
#                     e = False
#                     break
# if e:
#     print("NO")
# s = input()
# m = 0
# for l in range(len(s)):
#     for r in range(l+m,len(s)):
#         c = s[l:r+1]
#         if len(c) != len(set(c)):
#             break
#         else:
#             m = max(m,len(c))
# print(m)

# p = input()
# s = input()
# k = 0
# r = []
# for l in range(0,len(s)-len(p)+1):
#     if s[l:l+len(p)] == p:
#         r.append(l+1)
#         k+=1
# print(k)
# print(*r)

# s = input()
# k = int(input())
# o = set()
# for l in range(len(s)):
#     for r in range(l,len(s)):
#         c = s[l:r+1]
#         o.add(c)
# o = sorted(list(o))
# print(len(o))
# if k>len(o):
#     print("NO")
# else:
#     print(o[k-1])


# from math import dist
# n = int(input())
# pr = []
# m = 0
# for i in range(n):
#     p = list(map(int,input().split()))
#     pr.append(p)
# print(pr)
# for i in range(n-1):
#     m+=dist(pr[i], pr[i+1])
# m+=dist(pr[-1], pr[0])
# print(round(m+0.001,6))

a,b = 5,6
print(a+b,a-b, a*b, sep="\n")



print(input()[-1])

a = list(map(int, input().split()))
b = 1
for i in a:
    b *= i
print(b**(1/len(a)))

# N, b, c = int(input()), int(input()), int(input())
# N = int(str(N), b)
# s = ''
# while N!=0:
#     s+=str(N%c)
#     N//=c
# print(s[::-1])

import numpy as np
# 10
# print(np.identity(3))

# 24
# a = np.random.random((5,3))
# b = np.random.random((3,2))
# print(a@b)

# 37
# a = np.zeros((5,5))
# x = np.arange(5)
# a+=x
# print(a)

#42
# a = np.random.rand(5)
# b = np.random.rand(5)
# print(np.array_equal(a,b))

# a = np.random.random((2,3))
# print(a)
# a = np.roll(a,2)
# print(a)

