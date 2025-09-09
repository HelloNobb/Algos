#골드바흐 - 2제외 모든 짝수는 두 소수의 합으로 나타낼 수 있음

## 일단 <에라토스테네스의 체> 이용해 소거법으로 100까지만 소수구하기
MAX_NUM = 10000
PRIMES = [True]*(MAX_NUM+1)
PRIMES[0] = PRIMES[1] = False

for i in range(2, int(MAX_NUM**0.5)+1):
    if PRIMES[i]:
        for j in range(i*i, MAX_NUM + 1, i):
            PRIMES[j] = False
    
def get_gold(n):
    target = n // 2
    target2 = -1
    while True:
        if PRIMES[target]:
            target2 = n - target
            if PRIMES[target2]: #정답
                print(target, target2)
                return
        target = target-1
     
N = int(input())
T = []
for _ in range(N):
    x = int(input())
    T.append(x)

for t in T:
    get_gold(t)