'''
<바이러스 경쟁적 감염>

# 궁금한것
 S초가 지난 후 (X,Y)에 존재하는 바이러스의 종류 출력 (없으면 0출력)

# 조건
 - 모든 바이러스 1초마다 상,하,좌,우 증식 (낮은 번호가 먼저 증식)
 - 이미 바이러스 존재하는 칸이면 다른 바이러스 못 들어감
 
# 입력
N K (시험관 크기, 바이러스 최댓값)
(NxN만큼 각 위치에 존재하는 바이러스의 번호, 바이러스 번호는 K 이하)
S X Y (지난 초, 좌표)
 
# 접근 방법
0. 행렬로 좌표값 받기
	- 초 카운트변수
	- visited[] N*N개 만큼 생성
 >>	K크기의 딕셔너리 그래프 만들어야할까?
1. BFS- 큐 생성해 낮은 번호 바이러스부터 차례대로 판별 후 퍼진좌표 넣기(상하좌우(존재한다면))
2. 초 카운트
3. for문으로 원하는 초만큼 반복

1. 

'''
import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

def worm_go(MAP, who):
    print()