#[gpt] 핵심 아이디어: 미리 입력될수있는 최대 숫자 크기의 배열 만들어두기
#	*** 입력될 수 있는 개수는 100만이지만, 입력될숫자는 1만 이내이다!
import sys
N = int(input())
count = [0] * (10000+1)

input = sys.stdin.readline
for i in range(N):
    n = int(input())
    count[n] += 1

for i,v in enumerate(count):
    if v == 0:
        continue
    for j in range(v):
        sys.stdout.write(str(i)+"\n")