'''
## 조건
- 1은이동 가능, 0은 이동 불가
- (1,1) -> (n,m) 이동할때 지나야하는 최소 칸 수

## 접근

* 상하좌우 모두 체크
* visited 체크 ** (아이디어)
* dfs vs bfs
	- 지난 칸 수 세려면 dfs로 해야할듯?


1. 상하좌우 중 '1' && visited==false 안 곳 스택에 넣기
2. 하나 뽑아(count+=1) 해당 위치에서 갈 수 있는 곳도 모두 넣기
3. 만약 갈 데가 없으면 count-=1하고 pop
4. ㅇ=
'''
import sys
input = sys.stdin.readline
from collections import deque


N,M = map(int, input().split()) #행: N / 열: M
maze = [list(map(int, input().strip())) for _ in range(N)]


def bfs_maze(x, y):
    Q = deque([(x,y)])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while (Q):
        x,y = Q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < N and 0 <= ny < M):
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    Q.append((nx,ny))
        
    return maze[N-1][M-1]

print(bfs_maze(0,0))