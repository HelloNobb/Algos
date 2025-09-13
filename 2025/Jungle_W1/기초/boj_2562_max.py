N = 9
## 기존 방법 =====
# A = []
# for i in range(N):
#     x = int(input())
#     A.append(x)
## new 방법 ===== 
A = [int(input()) for _ in range(N)]

M = -100
index = -1
for i, val in enumerate(A):
    if M < val:
        M = val
        index = i+1

print(M)
print(index)