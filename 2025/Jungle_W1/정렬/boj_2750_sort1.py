## 시간초과 코드 (N <= 1000,000) =====================
N = int(input())

R = [int(input()) for _ in range(N)]
for i in sorted(R):
    print(i)
