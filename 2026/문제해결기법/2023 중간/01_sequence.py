'''
[ 등차수열 ] 

# input ====
N
(N개만큼 띄어쓰기 간격으로 배열값들 입력받음)

# output ====
(등차수열이면 1 / 아니면 0)

# 접근전략 ====
/ 등차수열 = 각 수열간의 간격(차)이 일정한 수열
-> A[i+1] - A[i] 값이 동일헤야함

'''
import sys
input = sys.stdin.readline

# logic ====
def is_sequence(N):
    global ARR
    
    mem = -1
    for i in range(N-1):
        gap = ARR[i+1] - ARR[i]
        if mem == -1:
            mem = gap
        if gap != mem:
            return 0
    
    return 1
    

# input ====
N = int(input())
ARR = list(map(int, input().split()))

# output ====
print(is_sequence(N))