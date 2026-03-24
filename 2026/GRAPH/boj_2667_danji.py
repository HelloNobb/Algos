'''
단지번호 붙이기
N*N 맵

## 입력
- N값
- N*N 0또는 1로 표현한 맵

## 출력
- 총 단지수
- (각 단지내 집의 수 오름차순 정렬, 한줄에 하나씩)

## 접근 계획
[ 상하좌우 탐색 > !visited 시, bfs로 큐에 넣는다. 큐가 빌때까지 돌면서 개수 센다.]
0: 어디서 시작? - 한 동네 끝나면 다음 타겟은 어디부터 확인?
	- 일단 (0,0)에서 출발, 끊기면 for문으로 행단위로 돌리자.
1: 상하좌우 탐색 > !visited이면, bfs로 큐에 넣는다.
2: 큐가 빌때까지 돌며 개수 세기 및 visited 처리한다.
'''
import sys
input = sys.stdin.readline
from collections import deque
# input ====
N = int(input())

GRAPH = []
for i in range(N):
    line = list(map(int, input().strip()))
    GRAPH.append(line)
    
visited = [[0]*N for _ in range(N)]

# logic ====
def search_each(start): # 이어진 집 개수 반환
    global visited
    global GRAPH
    visited[start[0]][start[1]] = 1
    
    house_amount = 1 #시작점 포함하기
    
    Q = deque()
    Q.append(start)
    
    while Q:
        now = Q.popleft()
        
        # 범위 내 상하좌우 체크 후 visited처리 및 큐에 넣기
        d1 = [-1,1,0,0]
        d2 = [0,0,-1,1]
        
        for i in range(4):
            X = now[0] + d1[i]
            Y = now[1] + d2[i]
            
            if (X < N and X >= 0 and Y < N and Y >= 0):
                if visited[X][Y] == 0 and GRAPH[X][Y] == 1:
                    visited[X][Y] = 1
                    house_amount += 1
                    Q.append((X,Y))
            
    return house_amount            
    
def search_danji():
    global visited
    global GRAPH
    
    sum = 0 #총 단지수
    each_danji = [] #각 단지별 집 개수
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and GRAPH[i][j] == 1:
                house = search_each((i,j))
                each_danji.append(house)
    
    sum = len(each_danji)
    print(sum)
    
    each_danji.sort()
    for i in range(sum):
        print(each_danji[i])


# output ====
search_danji()