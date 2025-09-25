# 첫줄 = 테스트케이스의수 = 2줄(각각)
# 테케 1- 문서개수N, 궁금한문서가 현재 큐 몇번째에 놓여있는지 M
# 테케 2- N개 문서의 중요도 차례대로 주어짐
from collections import deque
CASE = int(input())
ANS  = []
# [0,1,2,3,4] - [1,1,1,9,2]

def find_num(D, targetIdx):
    queue = deque()
    for i in range(len(D)):
        queue.append((i, D[i]))
        
    max = -999
    
    while True:
        now = queue[0][1]
        for i in range(D[1:]):
            if queue[i][1] > now:
                queue.append(queue.popleft())
        if sorted(D) == queue:
            for q in queue:
                if q[0]==targetIdx:
                    return queue.index(q)
    
for i in range(CASE):
    N, M = map(int, input().split())
    DOCS = list(map(int, input().split()))
    ANS.append(find_num(DOCS, M))
    
print(*ANS)