#T = [20, 7, 23, 19, 10, 15, 25, 8, 13]
T = []
for i in range(9):
    T.append(int(input()))


# 두개 조합 뽑기
for i in range(9): #기준
    for t in T[i+1:]: #
        a = T[i] #기준수하나
        b = t #나머지중에하나
        sum = 0
        for j in range(9):
            sum += T[j]
        sum -= (a+b)
        if sum == 100:
            break
    if sum == 100:
        break

for t in sorted(T):
    if t == a or t == b:
        continue
    print(t)