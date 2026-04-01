'''
# input
M N (열 수 , 행 수)
start (시작위치)
(M*N 01로 사다리위치받음)

# output
최종위치
'''
import sys
input = sys.stdin.readline

# logic ====
def down_ladder(line, start): # 시작 행, 열
    global GRAPH
    
    #case: L (i-1==1) / R(i==1) / down(둘다 0)
    if line == len(GRAPH):
        return start
    
    nextL = start-1
    nextR = start
    nextLine = line+1
    
    if nextL >= 0 and GRAPH[line][nextL] == 1:
        return down_ladder(nextLine, start-1)
    elif nextR < len(GRAPH[0]) and GRAPH[line][nextR] == 1:
        return down_ladder(nextLine, start+1)
    else:
        return down_ladder(nextLine, start)

# input ====
M,N = map(int, input().split())
FROM = int(input())

GRAPH = []
for i in range(N):
	line = input().strip()
	GRAPH.append(list(map(int, line)))

# output ====
TO = down_ladder(0, FROM)
print(TO)

'''
랜덤으로 사다리 게임 만들기도 재밌겠다.
'''