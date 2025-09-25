'''
# 입력값 : 트리 전위 순회한 결과
# 목표 출력값 : 트리 후위 순회한 결과

# 조건
 - 이진탐색트리(왼<루트<오)

# 개념
 - 전위: 루트 - 왼 - 오
 - 후위: 왼 - 오 - 루트
 
# 접근
1. 전위->후위
 

2. 후위순회로 출력
 - 

'''
from collections import deque
import sys
input = sys.stdin.readline

MAX_N = 10000
PRE_ALL = [] # 50, 30, 24, 5, ....
TREE = {} #ex. 1:[2,3], 2:[4,5]...
Q = deque()
# N(최대 10000)개 입력받기
for _ in range(MAX_N):
    n = input()
    if n == "":
        break
    #Q.append(n)
    PRE_ALL.append(int(n))
    
# (전위 순 원소리스트) -> (원소1개>끝, 2개>왼쪽만추가)루트-왼부분-오부분 > 
def pre_to_post(ALL):
    #빈배열ㅇ들어왔을떄 탈출해라
    if len(ALL) <= 1:
        print(*ALL)
        return
    
    root = ALL[0]
    ALL = ALL[1:]
    # root기준 왼/오 노드 나누기
    for i in range(len(ALL)):
        checker = i
        if ALL[i] > root:
            break
    ## 왼쪽만 남는경우
    if checker == 0:
        TREE[root] = ALL[0]
        
    L = ALL[:i]
    R = ALL[i:]
    # 그래프 추가
    #TREE[root] = [L[0], R[0]]
    pre_to_post(L)
    pre_to_post(R)
    print(root)
    

pre_to_post(PRE_ALL)
#print(TREE)