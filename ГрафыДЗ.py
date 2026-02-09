# 1
# def solve():
#     m = int(input())
#     edges = [tuple(map(int, input().split())) for _ in range(m)]
#     if not edges:
#         print(True)
#         return
#     vertices = set()
#     for a, b in edges:
#         vertices.add(a)
#         vertices.add(b)
#     if not vertices:
#         print(True)
#         return
#     max_v = max(vertices)
#     V = [[] for _ in range(max_v + 1)]
#     for a, b in edges:
#         V[a].append(b)
#         V[b].append(a)
#     visited = [False] * (max_v + 1)
#     def DFS(start):
#         visited[start] = True
#         for v in V[start]:
#             if not visited[v]:
#                 DFS(v)
#     ncomp = 0
#     for v in vertices:
#         if not visited[v]:
#             ncomp += 1
#             DFS(v)
#     print(ncomp == 1)
# solve()
'''
5
0 1
1 2
2 3
3 5
4 1

Вывод:True


7
0 1
1 2
2 3
3 5
4 6
4 8
7 8

Вывод:False
'''

# 2
# def solve():
#     n_nodes = int(input().strip())
#     edges_str = input().strip()
#     edges_str = edges_str[1:-1]
#     if not edges_str:
#         edges = []
#     else:
#         pairs = edges_str.split('), (')
#         pairs[0] = pairs[0][1:] if pairs[0].startswith('(') else pairs[0]
#         pairs[-1] = pairs[-1][:-1] if pairs[-1].endswith(')') else pairs[-1]
#         edges = []
#         for p in pairs:
#             a, b = map(int, p.split(', '))
#             edges.append((a, b))
#     start, end = map(int, input().strip().split())
#     graph = {}
#     for a, b in edges:
#         if a not in graph:
#             graph[a] = []
#         graph[a].append(b)
#         if b not in graph:
#             graph[b] = []
#     visited = set()
#     def dfs(u):
#         if u == end:
#             return True
#         visited.add(u)
#         for v in graph.get(u, []):
#             if v not in visited:
#                 if dfs(v):
#                     return True
#         return False
#     result = dfs(start) if start in graph else False
#     print(result)
#
# if __name__ == "__main__":
#     solve()
'''
6
[(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)]
4 5

Вывод: True
'''


#3
# def find_itinerary(tickets):
#     all_airports = set(tickets.keys()) | set(tickets.values())
#     start = None
#     for airport in tickets.keys():
#         if airport not in tickets.values():
#             start = airport
#             break
#     route = []
#     current = start
#     while current:
#         route.append(current)
#         current = tickets.get(current)  # следующий аэропорт
#     return route
# import ast
#
# input_str = input().strip()
# tickets = ast.literal_eval(input_str)
# result = find_itinerary(tickets)
# print(result)
'''
{'HKG': 'DXB', 'FRA': 'HKG', 'DEL': 'FRA'}

Вывод: ['DEL', 'FRA', 'HKG', 'DXB']
'''

#4
# def f():
#     m = int(input().strip())
#     edges = [tuple(map(int, input().split())) for _ in range(m)]
#     max_v = 0
#     for u, v in edges:
#         max_v = max(max_v, u, v)
#     n = max_v + 1
#     graph = [[] for _ in range(n)]
#     for u, v in edges:
#         graph[u].append(v)
#         graph[v].append(u)
#     visited = [False] * n
#     def dfs(u, parent):
#         visited[u] = True
#         for v in graph[u]:
#             if not visited[v]:
#                 if dfs(v, u):
#                     return True
#             elif v != parent:
#                 return True
#         return False
#     for i in range(n):
#         if not visited[i]:
#             if dfs(i, -1):
#                 return True
#     return False
# print(f())
'''
3
0 1
1 2
0 2
Вывод:True

4
0 1
1 2
2 3
1 4
Вывод:False
'''

# 5
# import heapq, ast
#
# edges = ast.literal_eval(input())
# s, e = map(int, input().split())
#
# g = {}
# for u,v,w in edges:
#     g.setdefault(u,[]).append((v,w))
#     g.setdefault(v,[])
#
# dist = {n:10**9 for n in g}
# dist[s], q = 0, [(0,s)]
#
# while q:
#     d,u = heapq.heappop(q)
#     if u==e: print(d); break
#     if d>dist[u]: continue
#     for v,w in g[u]:
#         nd = d+w
#         if nd<dist[v]:
#             dist[v]=nd
#             heapq.heappush(q,(nd,v))

'''
[(0, 1, 3), (0, 4, 1), (1, 2, 1), (1, 3, 3), (1, 4, 1), (4, 2, 2), (4, 3, 1)]
0 2

Вывод:3
'''
#6
# def f(words):
#     n = len(words)
#     graph = [[False] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i != j and words[i][-1] == words[j][0]:
#                 graph[i][j] = True
#     visited = [False] * n
#     def backtrack(current, count):
#         if count == n:
#             return graph[current][start_index]
#         for next_word in range(n):
#             if not visited[next_word] and graph[current][next_word]:
#                 visited[next_word] = True
#                 if backtrack(next_word, count + 1):
#                     return True
#                 visited[next_word] = False
#         return False
#     for start_index in range(n):
#         visited = [False] * n
#         visited[start_index] = True
#         if backtrack(start_index, 1):
#             return True
#     return False
# input_str = input().strip()
# if input_str.startswith('[') and input_str.endswith(']'):
#     content = input_str[1:-1]
#     if content:
#         words = [word.strip() for word in content.split(',')]
#         words = [word.strip('"\'') for word in words]
#     else:
#         words = []
# else:
#     words = []
#
# print(f(words))
#

'''
[ANT, OSTRICH, DEER, TURKEY, KANGAROO, TIGER, RABBIT, RAT, TOAD, YAK, HYENA]

Вывод:True
'''
