'''
https://www.acmicpc.net/problem/1697

## 조건
N ---> K
(0 <= N <= 100,000)
(0 <= K <= 100,000)

1초당
	- 1칸 이동 (+1 / -1)
	- 2배 이동 (*2)


## 입력
N K

## 출력
(가장 빠른 찾는 시간 몇 초인지)

## 접근 계획
방법1: bfs탐색?
	- 최초로 끝나는 지점에서 끝내면됨. 
	- 근데 다단계식이라 O(2^N) --> 최악의 경우 2^10민
	- 무지성으로 모든 경우의수 따질 순 없음. 목표치에 가까워져야함

방법2: 그리디?

방법3: 수학
	- 2배이동 횟수 경우의수 기준으로
	5 17 -> *1 *2 *3 *4 -> 
 
===========
 >> 제미나이 힌트: bfs가 맞다.(최단거리 구할 때 가장 적합)
 단, 내가 우려했던 O(2^N)은 X. visited처리만 하면 O(N)
	(***한번 방문한 좌표는 다시 방문할필요없다. 이미 방문한 경로가 더 빠름)
 
 * 그리디 - 현재위치에서 *2 / +1 중 뭐할지가 최단시간 보장 못함
 * 수학 - 숫자 커질수록 수 복잡해져서 단순 계산으로 풀기 매우 까다로움
 

[반례] 
0 0 (출발-도착이 같은 경우 - )
'''
import sys
input = sys.stdin.readline
from collections import deque

MIN = 0
MAX = 100000

# logic ====
def bfs_shortest(FROM, TO):
    
    if FROM == TO: ## edge case
        return 0

    visited = [0] * (MAX+1)
    visited[FROM] = 1
    
    Q = deque()
    Q.append((FROM, 0))
    
    while Q:
        NOW = Q.popleft()
        #print("now: ",NOW[0])
        
        count = NOW[1]+1 #다음애들 경로횟수
        new1 = NOW[0] - 1
        new2 = NOW[0] + 1
        new3 = NOW[0] * 2
        #print("후보: ", new1, new2, new3)
        #print("count: ", count)
        
        
        if new1 == TO or new2 == TO or new3 == TO:
            return count
        #print("====")
        # new1
        if new1 >= MIN and visited[new1] == 0:
            visited[new1] = 1
            Q.append((new1, count))
        # new2 & new3
        if NOW[0] < TO:
            if new2 <= MAX and visited[new2] == 0:
                visited[new2] = 1
                Q.append((new2, count))
                
            if new3 <= MAX and visited[new3] == 0:
                visited[new3] = 1
                Q.append((new3, count))
    
    return count

# input ====
N,K = map(int, input().split()) #N-->K

# output ====
print(bfs_shortest(N, K))