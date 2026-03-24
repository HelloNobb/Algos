'''
https://www.acmicpc.net/problem/1012

## 문제
- 각 케이스의 단지수 찾기와 동일 (단, 입력방식이 10101 가 아닌 각 1인 좌표를 입력받음)

## 입력
- T (케이스 수)
==== 
- M, N, K (가로길이(1~50) / 세로길이(1~50) / 배추좌표개수(1~2500))
- (K만큼 타깃 좌표 한줄씩 받음)
==== T번 반복

## 출력
- (한줄씩 각 케이스의 지렁이 수 출력)


## 접근 계획
1: 좌표 받아서 

<그래프를 행렬로 만드는게 효율적일지, 그냥 좌표자체를 튜플로 저장해두고 좌표로 visited처리하면서 하는게나을지>
1: 타깃좌표를 튜플로 받아 (1,1) 이런식으로 배열에 모두 저장
2: for문으로 타깃좌표 돌면서, 해당 좌표받으면 bfs로 연결된 좌표 모두 확인해 visited처리
	==> 반복
 
3: 단지수 반환

'''
import sys
input = sys.stdin.readline
from collections import deque

# logic ==== : K만큼 타깃좌표 입력받고 단지수 반환
def bfs_amount(M,N,K):
    GRAPH = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    # input ====
    for _ in range(K):
        X,Y = map(int, input().split())
        GRAPH[Y][X] = 1
    
    # bfs search ====
    COUNT = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(N):
        for j in range(M):
            if GRAPH[i][j] == 1 and not visited[i][j]:
                COUNT += 1
                Q = deque([(j, i)])
                visited[i][j] = True
                
                while Q:
                    cx, cy = Q.popleft()
                    
                    for d in range(4):
                        nx, ny = cx + dx[d], cy + dy[d]
                        if 0 <= nx < M and 0 <= ny < N:
                            if GRAPH[ny][nx] == 1 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                Q.append((nx, ny))
                    
    return COUNT

# input ====
T = int(input())
RSLT = []
for i in range(T):
    M, N, K = map(int, input().split())
    
    amount = bfs_amount(M,N,K)
    RSLT.append(amount)

# output ====
[print(r) for r in RSLT]