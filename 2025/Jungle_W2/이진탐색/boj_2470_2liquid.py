import sys
input = sys.stdin.readline
# <투포인터방식> (왼,오 끝에서 시작해서 -1 / +1씩 하며 좁혀오며 0에 가장 가까운 합 찾는 방식)
# (이게 정석풀이라고는 함)

def find_pair(N, A):
    A.sort()
    l = 0
    r = len(A)-1
    k_l = -1
    k_r = -1
    k_sum = 9999999999
    while l < r:
        S = A[l] + A[r]
        
        if abs(S) < abs(k_sum):
            k_sum = S
            k_l = l
            k_r = r
        
        if S == 0:
            print(A[l], A[r])
            return
        elif S > 0:
            r -= 1
        else:
            l += 1
            
        
    print(A[k_l], A[k_r])
    return
            
#### 이진탐색으로 푸는 법(사진찍어둠))        
N = int(input())
A = list(map(int, input().split()))
find_pair(N,A)

## <이진탐색> 풀이
# : 각 원소마다 -A[i]에 가까운 값 찾기
