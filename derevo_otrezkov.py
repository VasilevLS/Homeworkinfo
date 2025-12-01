import math


class SegmentTreeMax:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, le, r):
        le += self.n
        r += self.n
        res = -float('inf')
        while le < r:
            if le & 1:
                res = max(res, self.tree[le])
                le += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            le //= 2
            r //= 2
        return res


class SegmentTreeGCD:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = math.gcd(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, le, r):
        le += self.n
        r += self.n
        res = 0
        while le < r:
            if le & 1:
                res = math.gcd(res, self.tree[le])
                le += 1
            if r & 1:
                r -= 1
                res = math.gcd(res, self.tree[r])
            le //= 2
            r //= 2
        return res


class SegmentTreeZeroCount:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = 1 if arr[i] == 0 else 0
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query_count(self, le, r):
        le += self.n
        r += self.n
        res = 0
        while le < r:
            if le & 1:
                res += self.tree[le]
                le += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            le //= 2
            r //= 2
        return res

    def find_kth_zero(self, k):
        if k > self.tree[1]:
            return -1
        idx = 1
        while idx < self.n:
            left_cnt = self.tree[2 * idx]
            if left_cnt >= k:
                idx = 2 * idx
            else:
                k -= left_cnt
                idx = 2 * idx + 1

        return idx - self.n


def solve_task1():
    print("Задача 1: Максимум на отрезке")
    print("Введите количество чисел в массиве N:")
    n = int(input().strip())
    print(f"Введите {n} чисел (элементы массива):")
    arr = list(map(int, input().split()))
    print("Введите количество запросов K:")
    k = int(input().strip())
    segtree = SegmentTreeMax(arr)
    results = []
    print(f"Введите {k} запросов:")
    for _ in range(k):
        l, r = map(int, input().split())
        results.append(str(segtree.query(l - 1, r)))
    print("\nРезультаты:")
    print(" ".join(results))


def solve_task2():
    print("Задача 2: НОД на отрезке")
    print("Введите количество чисел в массиве N:")
    n = int(input().strip())
    print(f"Введите {n} чисел (элементы массива):")
    arr = list(map(int, input().split()))
    print("Введите количество запросов K:")
    k = int(input().strip())
    segtree = SegmentTreeGCD(arr)
    results = []
    print(f"Введите {k} запросов:")
    for _ in range(k):
        l, r = map(int, input().split())
        results.append(str(segtree.query(l - 1, r)))
    print("\nРезультаты:")
    print(" ".join(results))


def solve_task3():
    print("Задача 3: Поиск k-го нуля на отрезке")
    print("Введите количество чисел в массиве N:")
    n = int(input().strip())
    print(f"Введите {n} чисел (элементы массива, могут быть нули):")
    arr = list(map(int, input().split()))
    print("Введите количество запросов M:")
    m = int(input().strip())
    segtree = SegmentTreeZeroCount(arr)
    results = []
    print(f"Введите {m} запросов:")
    for _ in range(m):
        l, r, k_val = map(int, input().split())
        zeros_in_left = segtree.query_count(0, l - 1)
        zeros_in_segment = segtree.query_count(l - 1, r)
        if zeros_in_segment < k_val:
            results.append("0")
            continue

        target_zero_global = zeros_in_left + k_val
        pos = segtree.find_kth_zero(target_zero_global)

        results.append(str(pos + 1) if pos != -1 else "0")

    print("\nРезультаты:")
    print(" ".join(results))


print("Выберите задачу (1, 2 или 3):")
print("1 - Максимум на отрезке")
print("2 - НОД на отрезке")
print("3 - Поиск k-го нуля на отрезке")

task = input().strip()

if task == "1":
    solve_task1()
elif task == "2":
    solve_task2()
elif task == "3":
    solve_task3()
else:
    print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")
