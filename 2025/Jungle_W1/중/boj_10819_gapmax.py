#완전탐색
import itertools
N = int(input())
A = list(map(int, input().split()))

MAX_ = -1
for p in itertools.permutations(A):
    li = list(p)
    SUM_ = 0
    for i in range(len(li)):
        if i == len(li)-1:
            break
        SUM_ += abs(li[i] - li[i+1])
    if SUM_ > MAX_:
        MAX_ = SUM_
            
print(MAX_)