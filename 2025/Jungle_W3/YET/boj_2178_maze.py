#미로 최단경로길이찾기
from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

#거리 기록 배열 (0- 방문아직안함 / 1-방문함)
dist = [[0]*M for _ in range(N)]

#BFS 위한 큐
q = deque()
q.append((0,0)) #시작좌표(0,0)큐에넣음
dist[0][0] = 1 #시작칸 포함해서 거리=1

#상-하-좌-우 이동 위한 델타 배열
dx = [1,-1,0,0] #dx[0]:아래, dx[1]:위
dy = [0,0,1,-1] #dy[2]:오른쪽, dy[3]:왼쪽

#BFS 시작
while q:
    x,y = q.popleft()
    
    #도착지