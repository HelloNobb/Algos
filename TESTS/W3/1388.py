'''
<바닥 장식>

# 궁금한것
방 바닥 장식하는 데 필요한 나무 판자 개수

# 조건
 - 나무판자 너비 1
 - |: 행으로 이어지면 같은 나무판자 / - : 열로 이어지면 같은 나무판자
 
# 입력
N M
(N*M) 나무판자문자(| -)

# 목표 출력값
필요한 나무판자 개수
 
# 접근 방법
0. 행렬로 좌표값 받기
	- visited[]*N[False]*M 생성
	- count변수 
	- 가로 체크 함수
	- 세로 체크 함수
1. 0,0 좌표부터 visited 처리-> 뭔판자인지 체크-> 해당 판자처리함수로 넘기기
	> -: 오른쪽으로 넘어가다가 막히면(=다른판자오거나 끝나면) 카운트+1하고 각 행 마무리, 지난곳은 visited처리
	> |: 아래로 넘어가다가 막히면 마찬가지 처리
'''
import sys
input = sys.stdin.readline
#import pprint

N, M = map(int, input().split())
MAP = [list(input()) for i in range(N)]
garo_count = 0
sero_count = 0

#visited = [[False]*M]*N
visited = [[False for _ in range(M)] for _ in range(N)]
#pprint.pprint(visited)

def garo(MAP, N, M):
    global garo_count
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] or MAP[i][j] != '-':
                continue
            
            visited[i][j] = True
            garo_count += 1
            k = j #임시인덱스(옆쪽확인하기위함)
            while k < M-1:
                k = k+1
                if MAP[i][k] == '-':
                    visited[i][k] = True
                else:
                    break
                
        #pprint.pprint(visited)

def sero(MAP, N, M):
    global sero_count
    
    for i in range(M):
        for j in range(N):
            if visited[j][i] or MAP[j][i] != '|':
                continue
            
            visited[j][i] = True
            sero_count += 1
            k = j #임시인덱스(옆쪽확인하기위함)
            while k < N-1:
                k = k+1
                if MAP[k][i] == '|':
                    visited[k][i] = True
                else:
                    break
                
        #pprint.pprint(visited)
            

garo(MAP, N, M)
sero(MAP, N,M)
print(garo_count + sero_count)
