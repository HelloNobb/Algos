'''
## 문제
- 주어진 시작 정점으로부터 탐색

# dfs - stack
	* 

# bfs - queue
방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
	> *** 그래프 미리 정렬해두기
for i in range(1, N+1):
    GRAPH[i].sort()

 
'''
from collections import deque
import sys
input = sys.stdin.readline

N,M,V = map(int, input().split())
li = [[] for i in range(N+1)]

for i in range(M):
	node1, node2 = map(int, input().split())
	li[node1].append(node2)
	li[node2].append(node1)
 
##### 그래프 각 요소들 정렬
for i in range(1, N+1):
    li[i].sort()


def bfs(start):
    rslt = []
    visited = [False]*(N+1)
    
    Q = deque()
    Q.append(start)
    visited[start] = True
    
    while Q:
        node = Q.popleft()
        rslt.append(node)
        
        for child in li[node]:
            if not visited[child]:
                Q.append(child)
                visited[child] = True
    return rslt

def dfs(start):
    rslt = []
    visited = [False]*(N+1)
    
    STACK = deque()
    STACK.append(start)
    
    while (STACK):
        node = STACK.pop()
        
        if visited[node]:
            continue
        visited[node] = True
        rslt.append(node)
        ##### 스택이라 마지막자식부터 넣어야함
        for child in reversed(li[node]): 
            if not visited[child]:
                STACK.append(child)

    return rslt

print(*dfs(V))
print(*bfs(V))