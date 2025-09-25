'''
# N, M, V (정점개수, 간선개수, 시작정점번호)

# 조건
- 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문

# 목표
1. DFS 수행 결과
2. BFS 수행 결과

# 접근
일단 그래프 딕셔너리에 넣기
* 디에프에스
 - 시작정점 연결해서 자식노드들 중 가장 작은애만 방문하고나머지 스택에
 - 자식노드의 자식들도 똑같은 작업
'''
from collections import deque
# import sys
# input = sys.stdin.readline

N,M,V = map(int, input().split())#정점,간선,시작정점

GRAPH = {i: [] for i in range(N+1)}
for i in range(M):
    node1,node2 = map(int, input().split())
    GRAPH[node1].append(node2)
    GRAPH[node2].append(node1)

for i in range(1, N+1): ## 핵심 아이디어: 미리 자식들 정렬해두기
    GRAPH[i].sort()

## DFS ======== ####### visited 체크 시점: 스택에서 꺼낼떄 / 스택: 임시바구니(나중체크용)
def dfs(GRAPH, start, N):
    visited = [False]*(N+1)
    dfs_result = []
    stack = deque()
    
    #visited[start] = True
    stack.append(start)
    #dfs_result.append(start)
    
    while stack:
        node = stack.pop()
        
        if visited[node]:
            continue
        # not-visited-yet node
        visited[node] = True
        dfs_result.append(node)
        
        for child in reversed(GRAPH[node]): #스택유지하며 젤처음자식꺼내야해서
            if not visited[child]:
                stack.append(child)
                
    return dfs_result

result = dfs(GRAPH, V, N)
print(*result)

## BFS ========= ####### visited 체크 시점: 큐에 넣기전 (그래야 )/ 큐의용도: 이미체크하고 넣은 애의 자식순서대로 꺼내려고
def bfs(GRAPH, start, N):
    visited = [False]*(N+1)
    bfs_result = []
    ## start는 일단 먼저 검증 후 넣기 (넣은 애들은 다 )
    Q = deque()
    Q.append(start)
    visited[start] = True
    
    while Q:
        node = Q.popleft()

        for child in GRAPH[node]:
            if not visited[child]:
                Q.append(child)
                visited[node] = True
                bfs_result.append(node)
                
    return bfs_result

result = bfs(GRAPH, V, N)
print(*result)


## ===================
## 예시
# def bfs(dictArr, visited, root):
#     global cnt
#     que = deque()
#     que.append(root)
#     # cnt += 1
#     visited[root] = True
#     while que:
#         target = que.popleft()
#         childArr = dictArr[target]
#         for child in childArr:
#             if(not visited[child]):
#                 que.append(child)
#                 visited[child] = True
#                 cnt += 1
                
# queue = deque()
# def bfs(start):
#     queue.append(start)
#     visited[start] = True
#     while queue:
#         node = queue.popleft()
#         for ne in graph[node]:
#             if not visited[ne]:
#                 queue.append(ne)
#                 visited[ne] = True
# bfs(1)