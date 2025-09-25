#이진탐색
import sys
input = sys.stdin.readline

N = int(input())
CARDS = list(map(int, input().split()))
M = int(input())
TARGETS = list(map(int, input().split()))

CARDS.sort()
#카드들 속에 타깃이 있는지 확인
def find_target(C, t):
    left = 0
    right = len(C)-1
    while left <= right:
        mid = (left + right) // 2
        if C[mid] == t:
            return 1
        elif C[mid] < t:
            left = mid+1
        else:
            right = mid-1
        
        if left > right:
            return 0
            
for t in TARGETS:
    print(find_target(CARDS,t), end=" ")