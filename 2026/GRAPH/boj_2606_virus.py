'''

'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
start = 1
line = int(input())

GRAPH = [[] for _ in range(N+1)]

for i in range(line):
    node1, node2 = map(int, input().split())
    GRAPH[node1].append(node2)
    GRAPH[node2].append(node1)

def bfs_virus(start):
    global GRAPH
    global N
    
    Q = deque()
    visited = [False]*(N+1)
    RESULT = []
    
    visited[start] = True
    Q.append(start)
    
    while Q:
        node = Q.popleft()
        RESULT.append(node)
        
        for c in GRAPH[node]:
            if not visited[c]:
                visited[c] = True
                Q.append(c)
    #print(*RESULT)
    return len(RESULT) - 1 #자기자신 제외

print(bfs_virus(start))

                