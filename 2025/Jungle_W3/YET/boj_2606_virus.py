import sys
input = sys.stdin.readline
from collections import deque
##import pprint

'''
dfs 이용
 - 
'''
N = int(input())
E = int(input())

GRAPH = {i: [] for i in range(N+1)}
for i in range(E):
    node1, node2 = map(int, input().split())
    GRAPH[node1].append(node2)
    GRAPH[node2].append(node1)

def dfs(GRAPH, N, START):
    rslt = 0
    affected = [False] * (N+1)
    
    STACK = deque()
    STACK.append(START)
    
    while STACK:
        now = STACK.pop()
        
        if affected[now]:
            continue
        
        affected[now] = True
        rslt += 1
        
        for child in GRAPH[now]:
            if not affected[child]:
                STACK.append(child)
    return rslt

rslt = dfs(GRAPH, N, 1)
print(rslt-1)

##################


##
# stack = []
# def dfs(start):
#     stack.append(start)
#     while stack:
#         node = stack.pop()
#         if not visited[node]:
#             visited[node] = True
#             for ne in graph[node]:
#                 if not visited[ne]:
#                     stack.append(ne)
# dfs(1)
# print(len([b for b in visited if b]) - 1)


# V = int(rl())
# E = int(rl())
# graph = {}
# visited = [False for _ in range(V + 1)]
# for i in range(1, V + 1):
#     graph[i] = []
# for _ in range(E):
#     l, r = map(int, rl().split())
#     graph[l].append(r)
#     graph[r].append(l)