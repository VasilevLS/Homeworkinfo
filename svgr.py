#1
from collections import deque
import sys

def edmonds_karp(capacity, source, sink):
    n = len(capacity)
    parent = [-1] * n
    max_flow = 0

    def bfs():
        for i in range(n):
            parent[i] = -1
        parent[source] = source
        q = deque([source])
        while q:
            u = q.popleft()
            for v in range(n):
                if parent[v] == -1 and capacity[u][v] > 0:
                    parent[v] = u
                    if v == sink:
                        return True
                    q.append(v)
        return False

    while bfs():
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow
input_data = sys.stdin.read().strip().split()
idx = 0
network_num = 1
results = []

while idx < len(input_data):
    n = int(input_data[idx]); idx += 1
    if n == 0:
        break
    s = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    c = int(input_data[idx]); idx += 1
    capacity = [[0] * n for _ in range(n)]

    for _ in range(c):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        bw = int(input_data[idx]); idx += 1
        capacity[u-1][v-1] += bw
        capacity[v-1][u-1] += bw

    maxflow = edmonds_karp(capacity, s-1, t-1)
    results.append(f"Network {network_num}\nThe bandwidth is {maxflow}.")
    network_num += 1

print("\n".join(results))

#2
from collections import deque

t = int(input())
for case_idx in range(1, t + 1):
    N = int(input())
    have = [0] * (N + 1)
    for _ in range(N):
        x = int(input())
        have[x] += 1

    e = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    if case_idx != t:
        _ = input()

    extra = []
    missing = []
    for x in range(1, N + 1):
        if have[x] > 1:
            extra.extend([x] * (have[x] - 1))
        elif have[x] == 0:
            missing.append(x)
    total_cost = 0
    missing.sort()
    extra_available = extra[:]

    for target in missing:
        dist = [-1] * (N + 1)
        dist[target] = 0
        q = deque([target])
        found = -1
        while q:
            u = q.popleft()
            if u in extra_available:
                found = u
                break
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        if found != -1:
            total_cost += dist[found]
            extra_available.remove(found)

    print(total_cost)
