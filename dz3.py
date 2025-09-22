# 1
# def fib(N):
#     if N == 1 or N == 2:
#         return 1
#     else:
#         return fib(N-1)+fib(N-2)
# print(fib(10))

# 2
# def simple(n):
#     if n <= 1:
#         return []
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return [i] + simple(n // i)
#     return [n]
#
#
# n = 120
# print(simple(n), " ")

# 3

# def evklid(a, b):
#     if b == 0:
#         return a, 1, 0
#     else:
#         d, x, y = evklid(b, a % b)
#         return d, y, x - y * (a // b)
# s = "4 6"
# a, b = map(int, s.split())
# d, x, y = evklid(a, b)
# print(x, y, d)

# 4
# def tr(size, symb):
#     for i in range(1, size + 1):
#         print(symb * min(i, size - i + 1))
#
# s = "7 b"
# size, symb = s.split()
# size = int(size)
# tr(size, str(symb))

# 5
# s = "5 5"
# n, m = [int(i) for i in s.split()]
# matrix = []
# for i in range(n):
#     temp = [0 for num in range(m)]
#     matrix.append(temp)
# x,y,= 0, 0
# k = int(1)
# matrix[0][0]=1
# while k < m*n:
#     if x + 1 < m:
#         if matrix[y][x+1] == 0:
#             x+=1
#             k+=1
#             matrix[y][x] = k
#             continue
#     if y + 1 < n:
#         if matrix[y + 1][x] == 0:
#             y += 1
#             k += 1
#             matrix[y][x] = k
#             continue
#     if matrix[y][x - 1] == 0 and x-1>=0:
#         x -= 1
#         k += 1
#         matrix[y][x] = k
#         continue
#     while matrix[y - 1][x] == 0:
#         y -= 1
#         k += 1
#         matrix[y][x] = k
#
# for row in matrix:
#     print(*row)



# 6
# import numpy as np
# x = np.array([3,6,7,8,5,6,4])
# y = np.array([7,3,9,2,6,4,7])
# a = (np.mean(x*y) - np.mean(x)*np.mean(y)) / (np.mean(x**2) * np.mean(x)**2)
# b = np.mean(y) - a*np.mean(x)
# std_a = 1/np.sqrt(len(x)) * np.sqrt((np.mean(y ** 2) - np.mean(y) ** 2) / ((np.mean(x**2)-np.mean(x)**2))-a**2)
# str_b = std_a * np.sqrt(np.mean(x**2) - np.mean(x)**2)
# print(std_a, str_b)

# 7
# import numpy as np
# a = np.array([[1, 1], [1, 2]])
# b = np.array([2, 1])
# x = np.linalg.solve(a, b)
# print(x)


# 8
# import random
# import numpy as np
#
#
# def generate_linear_data(N, a, b, noise_std=1.0):
#     x = np.linspace(-10, 10, N)
#     y_true = a * x + b
#     noise = np.array([random.gauss(0, noise_std) for _ in range(N)])
#     y = y_true + noise
#
#     return x, y
#
#
# # Пример использования:
# N = 100
# a = 2.5
# b = -3.0
# x, y = generate_linear_data(N, a, b, noise_std=2.0)

# import matplotlib.pyplot as plt
#
# plt.scatter(x, y)
# plt.plot(x, a * x + b, color='red')
# plt.show()
