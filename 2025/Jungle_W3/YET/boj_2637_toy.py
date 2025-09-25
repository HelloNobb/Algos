'''
장난감 조립

<입력>
1. N (1~N-1: 기본/중간부품 번호 , N: 완제품 번호)
2. M (받을 케이스 개수)
3. M * X,Y,K (중간/완제품번호, 중간/기본번호, 필요개수)

<출력>
하나의 완제품 조립하는ㄷ 필요한 기본 부품의 수(중간부품출력X)
 >> 기본 부품의 번호가작은것부터 [번호, 개수] 출력
 
 
<접근>
## 키워드: 위상정렬 (우선순위별로 ?덱에 순서대로 담기)
1.
완제품에 필요한 부품들은 (번호,개수) 튜플 값을 넣은 큐로 만든다.
2.
중간부품에 필요한 부품들은 (번호,개수) 튜플 값을 넣은 딕셔너리로 전부 만든다. 
3.
다시 완제품으로 돌아와서 popleft-> 해당번호가 중간부품딕셔너리의 키중에 하나라면 해당 키의 튜플값들을 완제품에 append한다.
(단, 튜플 각각의 두번째 원소인 개수는 지금꺼낸 중간부품개수만큼 배로 불린다)
4.
popleft를 반복하며, 만약 기본부품으로만 이루어진 튜플이라면, 해당 개수만큼 count하고 버린다.
5.
이 작업을 큐가 비어질때까지 반복한다.
}
'''
from collections import deque
import sys
input = sys.stdin.readline



N = int(input())
CASE = int(input())
GRAPH = {i:[] for i in range(CASE)}
for i in range(CASE):
    X, Y, K = map(int, input().split())
    GRAPH[X].append((Y, K))


#########
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]   # X -> (Y, K)
indeg = [0]*(n+1)
is_target = [False]*(n+1)        # 타깃(조립품) 표시
for _ in range(m):
    X, Y, K = map(int, input().split())
    adj[X].append((Y, K))
    indeg[Y] += 1
    is_target[X] = True          # 타깃으로 등장 = 조립품
need = [0]*(n+1)
need[n] = 1                      # 완제품 1개 필요
q = deque([n])
while q:
    x = q.popleft()
    for y, k in adj[x]:
        need[y] += need[x] * k
        indeg[y] -= 1
        if indeg[y] == 0:
            q.append(y)
# 기본 부품(타깃으로 한 번도 등장 X)만 출력
for i in range(1, n):
    if not is_target[i]:
        print(i, need[i])
        
        
        
        
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# 입력
N = int(input().rstrip())          # 부품 총 개수 (완제품 번호 = N)
M = int(input().rstrip())          # 관계 수

# 중간부품 딕셔너리: parts[X] = [(Y, K), ...]  (X를 만들 때 Y가 K개 필요)
parts = {}
for _ in range(M):
    X, Y, K = map(int, input().split())
    parts.setdefault(X, []).append((Y, K))

# 기본부품 누적 카운트
need = defaultdict(int)

# 큐: (부품번호, 필요한 개수)
q = deque()

# 시작: 완제품 N을 구성하는 직접 부품들로 초기화
if N in parts:                 # N이 중간부품(=분해 대상)
    for y, k in parts[N]:
        q.append((y, k))
else:                          # N 자체가 기본부품인 특수 케이스
    need[N] += 1

# 분해 진행
while q:
    x, c = q.popleft()
    if x in parts:
        # x가 중간부품이면 자식들을 (자식, 개수*누적배수)로 큐에 추가
        for y, k in parts[x]:
            q.append((y, k * c))
    else:
        # x가 기본부품이면 개수 누적
        need[x] += c

# 출력: 기본부품 번호 오름차순
for b in sorted(need):
    print(b, need[b])


## 동현님풀이
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
cnt = int(input().rstrip())
dictArr = {i:[] for i in range(1, n + 1)}
buildSet = set()   # 완제품, 조립품 목록
for _ in range(cnt):
    target, ingre, count = list(map(int, input().split()))
    buildSet.add(target)
    dictArr[target].append([ingre, count])   # 필요한 횟수만큼 추가
resultArr = [0] * n
que = deque()
que.append([n,1])   # 완제품 넣고 시작
while que:
    targetNum, targetCount = que.popleft()
    if(targetNum not in buildSet):
        resultArr[targetNum] += targetCount
    else:
        childArr = dictArr[targetNum]
        for child in childArr:
            childNum, childCnt = child
            if(childNum not in buildSet):   # 기본부품이면?
                resultArr[childNum] += childCnt * targetCount
            else:
                que.append([childNum, childCnt * targetCount])
for i in range(1, len(resultArr)):
    if(i not in buildSet):
        print(str(i) + ' ' + str(resultArr[i]))