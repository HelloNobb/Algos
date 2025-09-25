from collections import deque
import pprint
N,M = map(int, input().split())

graph={i: [] for i in range(1, N+1)}
count = [0]*(N+1) # 0번은 none 1~N만 취급
count[0] = -1

def topo_sort():
    global graph
    queue = deque()
    
    for index,c in enumerate(count):
        if c == 0:
            queue.append(index)
            #print(f"{index} 큐에들어옴")
    result = []
    
    while queue:
        now = queue.popleft()
        #print(f"now: {now}")
        result.append(now)
        
        for neighbor in graph[now]:
            count[neighbor] -= 1
            
            if count[neighbor] == 0:
                queue.append(neighbor)
        
    if len(result) == N:
        return result
    else:
        return "그래프 망함"+str(result)

# 그래프 생성 + 각 진입차수 카운트
for i in range(M):
    first, sec = map(int, input().split())
    graph[first].append(sec)
    
    count[sec] += 1

#pprint.pprint(graph)
li = topo_sort()
for i in li:
    print(i, end=" ")