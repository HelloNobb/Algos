'''
## input
N (배열크기)
K (행운숫자)
(N짜리 배열 입력)

## output
(행운숫자 몇번나왔는지)  -- ex) 7 17 14 77 --> 행운숫자 7이면 답: 4


## 접근계획
- 각 배열 원소가 0될때까지 각 자리수 확인후 10으로 나눠가며 1의자리만 확인
'''
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    now = A[i]
    while now > 0:
        num = now % 10
        if num == K:
            count += 1
        
        now //= 10

print(count)