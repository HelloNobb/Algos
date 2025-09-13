# 여행지 한번씩만 갈때
import sys
input = sys.stdin.readline

N = int(input().strip())
W = [list(map(int, input().split())) for _ in range(N)] #행렬로 입력받음

INF = 10**12 ###
ans = INF ###
best_path = None #최소 비용일 때의 경로(사이클)

def dfs(start, now, depth, cost, visited, path):
    #start:출발도시/cur:지금있는도시/depth:지금까지방문한도시수/cost:누적비용/visited:도시사용여부배열
    #(path : 현재경로(스택))
    global ans, best_path
    #가지치기 - 더 가봐야 이길 수 없으면 중단
    if cost >= ans:
        return
    #모든 도시 방문 완료 -> 출발지로 돌아갈 수 있으면 정답 갱신
    if depth==N:
        if W[now][start] != 0:
            total = cost + W[now][start]
            if total < ans:
                ans = total
                best_path = path+[start]
        return
    
    #다음 도시 시도
    for nxt in range(N):
        if not visited[nxt] and W[now][nxt] != 0:
            visited[nxt] = True
            path.append(nxt)	# 내려가기 전에 경로에 추가
            dfs(start, nxt, depth+1, cost+W[now][nxt], visited, path)
            path.pop()
            visited[nxt]= False

#시작점 하나로 고정해도 정답 동일
start = 0
visited = [False]*N
visited[start] = True
dfs(start, start, 1, 0, visited, [start])
#result
print(ans if ans < INF else 0)