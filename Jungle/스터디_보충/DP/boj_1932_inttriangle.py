'''
[정수 삼각형 - 1932]: ~9:25

# 문제 분석 ========

<input>
* 삼각형 크기 n
* (n줄만큼 삼각형 긱 행 값들 입력)

<output>
: 합이 최대가 되는 경로에 있는 수의 합 (층마다 왼 대각선/ 오 대각선 중 하나씩 골라 내려옴)


- 삼각형 크기 n : 1~500
- 각 정수값 : 0~9999

# 접근 전략 ========

> 그리디 가능? : X
> 완탐 가능? : (가능한지 아직 모르겠음..)
	- 어떻게 구할건데 모든 경우의수를?: visited, 재귀 이용 

	T = 2차배열 
	visited=[0] * n
 
	def dfs (arr, idx, line): # idx: 직전 행 인덱스값 / line: 직전 행 
 
		if (idx == n):
			max값 갱신
			return
		
		for i in range(line, n): # 뽑을 행 인덱스
  
			# 다음 행 왼쪽 대각선 뽑는 경우 (재귀) ====
			arr.append(T[i][idx])
			dfs(arr, idx+1, i)
			arr.pop()
   
			# 다음 행 오른쪽 대각선 뽑는 경우 (재귀) ====
			arr.append(T[i][idx+1])
			dfs(arr, idx+1, i)
			arr.pop()

			
   
	> k번째값 뽑음 -> 다음 줄 (K / K+1) 번째 값 뽑음

====
1) 각 층마다 하나씩 뽑으며 내려오는 모든 경우의 수를 구한다.(how: 모름)
	====
	1: 매 층 0번째수 쭉 담기 : 5 7 3 8 2 (4)
	2: 합 구하기 -> max_sum 갱신
	3: 마지막 하나빼고 그 옆 대각선 추가  : 5 7 3 8 2 (5) (n-1번째 줄의 좌,우 대각선 모두 방문)
 
	4: 하나 더 뺸다. (n-1번째줄) -> 옆 대각선 추가 : 5 7 3 8 (7) ( )
	
	5: 좌,우 대각선 반복 : 5 7 3 8 7 (5)   &   5 7 3 8 7 (2)
	====
 
2) 매번 그 합이 최대합보다 크면 갱신한다.

'''
import sys
input = sys.stdin.readline

# input ========
n = int(input())
T = []
for i in range(n):
    line = list(map(int, input().split()))
    T.append(line)

# dfs: 모든 경우의 수의 배열 구하기 ========
MAX_SUM = -9
def dfs_triangle(arr, line, idx): #arr: 각 행에서 값 하나씩 담은 리스트 / line: 이번 차례 행 / idx: 직전 행의 값 인덱스
    global T, MAX_SUM
    
    if (len(arr) == n):
        print(f"{arr}")
        MAX_SUM = max(MAX_SUM, sum(arr))
        return
    
    # 다음 행 왼쪽 대각선 뽑는 경우 (재귀) ====
    arr.append(T[line][idx])
    dfs_triangle(arr, line+1, idx)
    arr.pop()
    
    if (idx + 1 <= line):
        arr.append(T[line][idx+1])
        dfs_triangle(arr, line+1, idx+1)
        arr.pop()
    
    
    # for i in range(line, n): #: 뽑을 행
    #     # 다음 행 왼쪽 대각선 뽑는 경우 (재귀) ====
    #     arr.append(T[i][idx])
    #     dfs_triangle(arr, i+1, idx)
    #     arr.pop()
        
    #     # 다음 행 오른쪽 대각선 뽑는 경우 (재귀) ====
    #     arr.append(T[i][idx+1])
    #     dfs_triangle(arr, i+1, idx+1)
    #     arr.pop()
        
# output ========
dfs_triangle([], 0, 0)
print(MAX_SUM)