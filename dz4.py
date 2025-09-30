# 1
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(12, 6))
# x20 =np.array([99.2, 119, 139,	157.7,	176.3,	198.7,	217.4,	237.6,	255.04,	277])
# y20 = np.array([200, 240, 280, 320, 360, 400, 440, 480, 520, 560])
# plt.errorbar(x20,y20,xerr=0.002*x20+0.02,yerr=3.75,linestyle='',ecolor='red',linewidth=6)
# p, v = np.polyfit(x20, y20, deg=1, cov=True)
# x=np.arange(min(x20),max(x20),0.01)
# plt.plot(x,x*p[0]+p[1],color='red',label='U=RI',linewidth=1)
# plt.grid()
# plt.title("Graph")
# plt.xlabel('I, мА')
# plt.ylabel('U, мВ')
# plt.legend(loc='best', fontsize=12)
# plt.show()


# 2

# import matplotlib.pyplot as plt
# import numpy as np
#
# fig = plt.figure(figsize=(16, 16))  # создали рисунок/Figure Fig пропорциями 16:9
# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)
#
# values1 = np.random.normal(0, 10, 100)
# values2 = np.random.normal(0, 10, 1000)
# values3 = np.random.normal(0, 10, 10000)
# values4 = np.random.normal(0, 10, 1000000)
# ax1.hist(values1, 50)
# ax1.grid()
#
# ax2.hist(values2, 50)
# ax2.grid()
#
# ax3.hist(values3, 50)
# ax3.grid()
#
# ax4.hist(values4, 50)
# ax4.grid()
#
# plt.show()

# 3
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('iris_data.csv')
# a = list(df["PetalLengthCm"])
# a1 = len([i for i in a if i<1.2])/ len(a)
# a2 = len([i for i in a if i>=1.2 and i <= 1.5])/ len(a)
# a3 = len([i for i in a if i>1.5])/ len(a)
# print(a1,a2,a3)
# plt.pie([a1, a2, a3], labels = ['< 1.2','1.2 <= length <= 1.5','> 1.5'])
#
#
# plt.show()
#

# 4
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# df = pd.read_csv("iris_data.csv")
# l = [("SepalLengthCm", "SepalWidthCm"), ("SepalLengthCm","PetalLengthCm"), ("SepalLengthCm", "PetalWidthCm"), ("SepalWidthCm", "PetalLengthCm"), ("SepalWidthCm", "PetalWidthCm"), ("PetalLengthCm", "PetalWidthCm")]
# for i,j in l:
#     plt.scatter(df[i], df[j])
#     x = np.array(list(df[i]))
#     y = np.array(list(df[j]))
#     n = len(x)
#     m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2)
#     b = (np.sum(y) - m * np.sum(x)) / n
#     y_pred = m * x + b
#     plt.plot(x, y_pred, color='k', label='Линия регрессии')
# plt.show()

#5
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('BTC_data.csv')
#
# y = list(df["close"])
# x = [f"{str(i)[8]+str(i)[9]}-{str(i)[5]+str(i)[6]}-{str(i)[:4]}" for i in list(df["time"])]
# plt.xticks([i for i in range(1,len(x),125)])
# plt.plot(x,y)
#
# plt.show()


#6
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('BTC_data.csv')
#
# y = list(df["close"])
# x = [f"{str(i)[8]+str(i)[9]}-{str(i)[5]+str(i)[6]}-{str(i)[:4]}" for i in list(df["time"])]
# plt.xticks([i for i in range(1,len(x),125)])
# plt.plot(x,y)
#
# x = np.array([float(i) for i in range(1,len(y)+1)])
# y = np.array(y)
# z = np.polyfit(x, y, 90)
#
# p = np.poly1d(z)
#
#
# plt.plot(x,p(x))
# plt.show()

# 7
# import string
# d = dict()
# f = open("PYTHON-LICENSE.txt").read()
# f = "".join([i.lower() for i in f])
# for i in string.punctuation:
#     f = f.replace(i, " ")
# f = f.split()
# l = list(set(f))
# for i in l:
#     d[i] = f.count(i)
# for _ in range(11):
#     for i in d.items():
#         if i[1] == max(d.values()):
#             if i[0] in "1234567890":
#                 del d[i[0]]
#                 break
#             print(i[0])
#             del d[i[0]]
#             break

# 8
a = [1, 2, 2, 3, 4, 5, 4, 6]
b = [2, 3, 3, 7, 4, 4, 8, 1]
c = set(a)
d = set(b)
for i in a:
    if a.count(i)==1:
        print(i, end=" ")
print("")
for i in b:
    if b.count(i)==1:
        print(i, end=" ")

a.extend(b)
print("")
for i in a:
    if a.count(i)==1:
        print(i, end=" ")
print("")
print(d & c)