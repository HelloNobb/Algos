import sys
input = sys.stdin.readline

#### 시간초과 원인:  선형탐색 >> 시간 오래걸림 =========================
# 타깃인덱스 위아래까지 배열에 타깃값이 총 몇개들었는지 리턴
# def get_count(A, t_idx):
#     amount = 1
#     new_idx = t_idx
#     while new_idx >= 0:
#         new_idx = new_idx - 1
#         if A[new_idx] == A[t_idx]:
#             amount += 1
#         else:
#             break
#     new_idx = t_idx
#     while new_idx <= len(A)-1:
#         new_idx = new_idx + 1
#         if new_idx > len(A)-1:
#             break
#         if A[new_idx] == A[t_idx]:
#             amount+= 1
#         else:
#             break
        
#     return amount 
#### 대안: 이진탐색 -> 키값의 윗인덱스, 아래인덱스 얻기=============================
def lower_bound(A, target): #A[i] >= target 처음 성립하는 가장왼쪽 인덱스 반환
    lo = 0
    hi = len(A)
    
    while lo < hi: #같아질때까지 반복
        mid = (lo + hi) // 2
        if target <= A[mid]:
            hi = mid
        else:
            lo = mid+1 #mid까지 왼쪽 다 버리기
    return lo

def upper_bound(A, target): #A[i] > target 처음 성립하는 가장왼쪽 인덱스 반환
    lo = 0
    hi = len(A)
    while lo < hi:
        mi = (lo+hi) // 2
        if target >= A[mi]:
            lo = mi+1
        else:
            hi = mi
    return lo


#### =============================================================
N = int(input()) #내가 갖고 있는 카드수
C = list(map(int, input().split())) #각 카드의 점수
C.sort()

M = int(input()) #갖고있어야할숫자개수
T = list(map(int, input().split())) #추적할 숫자들
count = []
for i in range(M): #목표: i값들 있는지,개수 체크
    count.append(upper_bound(C,T[i]) - lower_bound(C,T[i]))

print(*count)	# *: 리스트를 풀어 각각 인자로 넘겨줌 / print기본 구분자는 공백

## 코드 문제점
'''
	- 값을 찾긴 해도 count+1만 하고 한쪽으로 포인터 밀어버림
	- 같은 값이 몇 개 있는지 --> lower_bound(target), upper_vound(target)
'''