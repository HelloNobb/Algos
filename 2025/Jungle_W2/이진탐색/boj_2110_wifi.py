# import sys
# input = sys.stdin.readline

N,C = map(int, input().split()) #N: 집 개수, C: 공유기 개수
X = [int(input()) for i in range(N)] #X: 집 좌표들(N개)
X.sort()

def lower_bound(A, d, last):
    li = 1
    ri = len(A)-1
    last = 0 #일단 제일 왼쪽 집에 무조건 설치
    while li <= ri:
        mid = (li + ri) // 2
        
        if A[mid] - A[last] < d:
            li = mid+1
        else:
            ri = mid
    
    return ri
# 해당 갭으로 좌표 범위 내에 C만큼의 공유기를 설치할 수 있는지 여부 반환
def can_place(X, C, d): #X:집 좌표들, C:공유기 개수, d: 예상갭
    count = 1
    last = X[0]
    for i in range(1, len(X)): #그다음집고를때 선형검색해도됐음.(이진탐색만 생각하다 놓침)
        if X[i] - last >= d:
            count+= 1
            last = X[i]
            if count >= C: #핵심_ C개 모두 설치할만한 거리인지
                return True
    return False
# 예상거리 이진탐색으로 얻어 설치여부 확인하며 최소의 최대길이 계산          
def solve(X, C): #lo,hi,mid 모두 실제 갭 값
    X.sort()
    lo,hi = 1, X[-1]-X[0] # **배열[-1] : 배열의 마지막 원소 / 갭범위: 1~최대갭(=맨앞-맨뒤 거리)
    ans = 0
    while lo <= hi:
        mid = (lo+hi) // 2
        if can_place(X,C,mid):
            ans = mid
            lo = mid + 1
        else: #설치 못한단얘기는 간격이 너무 크단얘기
            hi = mid - 1
    return ans
'''
	-막힌 지점 :배치했을때 거리들 계산을 하나하나 구해 어떻게 다 비교하지?
	-접근법 아이디어[gpt] : 
	0) 일단 제일 왼쪽 집에 설치
 	1)답을 직접 찾기보다 최소거리를 x로 미리 잡고 x를 이진탐색으로
	 탐색하며 진짜 x를 구하면 됨.
	2)최소 거리 d로 설치 가능? -> 하나씩 d이상 거리되게끔 타깃개수만큼 설치해보기
		> 안되면 거리 좁히기
		> 되면 거리 넓혀보기
     ** 최소거리를 탐색하는게 핵심(최소: 나머지도 이것 이상이어야한다)
     
    ## 사고 오류-> 솔루션
		/ 거리후보를 만들려함 -> 오히려 비효율적(차라리 1~최대거리 이진탐색으로 갭찾는게나음)
			: 후보개수 개많아짐 N(N-1)/2
			> 갭 d로 C개의 공유기를 설치 가능한지 여부는 
   			  간단히 for문으로 마지막 설치집으로부터의 거리 차 이상인곳에 넣어보면서 개수 세어 판변하면됨

		/ 
'''