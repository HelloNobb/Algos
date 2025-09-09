## 시간초과 코드 (N <= 1000,000) =====================
# N = int(input())

# R = [int(input()) for _ in range(N)]
# for i in sorted(R):
#     print(i)

# > 시간초과이유: input(), print() 입출력속도(느림)

## 개선 코드 =====================
import sys
#N = int(input())
input = sys.stdin.readline
N = int(input())
R = [int(input()) for _ in range(N)]
for i in sorted(R):
    sys.stdout.write(str(i)+"\n")