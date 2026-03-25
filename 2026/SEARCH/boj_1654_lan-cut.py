'''
## 문제 조건
제각각 길이의 K개 랜선들 잘라서 최대&동일 길이의 N개 랜선 만들기

- K <= N
- K: 1~10만
- N: 1~100만

** N개보다 많이 만드는 것도 N개를 만드는 것에 포함


## input
4 11 : K N (K: 갖고있는 개수 / N: 필요 개수)
802 : K개의 각각의 길이
743
457
539

## output
200 : (N개 만들 수 있는 최대 길이)

## 접근 계획
- 1~MAX중에 하나일테니 (MAX = K개 랜선 중 최대길이)
이진탐색으로 구하기

1: L = 1 / R = max(K)
2: 이진탐색 - 각각 K를 mid로 나눠서 총 개수 구하기 (N과 비교)
'''
import sys
input = sys.stdin.readline

def LAN_amount(targetLen): #해당 길이로 K개 안에서 뽑을 수 있는 최대 동일길이 랜 개수
    global EACH
    amount = 0
    
    for e in EACH:
        amount += e // targetLen
        
    return amount
    
def bin_search(targetAmount, MIN, MAX):
    L = MIN #min_len
    R = MAX #max_len
    answ = 0
    
    while L <= R:
        mid = (L + R)//2
        # edge-case ==
        if mid == 0:
            mid = 1
        
        lanAmount = LAN_amount(mid)
        if lanAmount >= targetAmount:
            answ = mid #일단 임시저장
            L = mid+1
        else:
            R = mid-1
        # else: ## maxAmount==target이어도 덜만들어도됨.(최대길이여야함)
        #     return mid
    
    return answ ##


# input ====
K, N = map(int, input().split())
EACH = []
[EACH.append(int(input())) for _ in range(K)]

# output ====
print(bin_search(N, 1, max(EACH)))

'''
[엣지케이스]

1 4 
6

-> 1 나와야하는데 2 나옴


'''
