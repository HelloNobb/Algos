#소수찾기
N = int(input())
arr = list(map(int, input().split()))
arr = arr[:N]

count = 0
for r in arr:
    if r == 1:
        continue
    for i in range(2,r+1):
        if r % i == 0:
            break
    if i == r:
        count+= 1
print(count)