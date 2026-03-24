'''
[등수 구하기] : ~9:20

# 문제 분석 ====

	0 <= N <= P <= 10
	0 <= score <= 200억

 * 입력: 랭킹기록점수개수(N) , 새 점수 , (랭킹에 올라갈 수 있는 점수 개수) / [현재 랭킹 리스트에 있는 점수(비오름차순)]
 * 출력: 새로운 점수의 등수 (랭킹에 못 올라가면 -1)
 
# 접근 전략 ====
 - 
 """""""""
 만약, 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.
 """""""""
  > 어떻게 해결?

'''
import sys
input = sys.stdin.readline

N, new, P = map(int, input().split())
RANK = list(map(int, input().split()))

# 점수들 넣으면 등수배열 반환
def get_rank(arr, new):
    # 이전 기록 없음-> 1등
    if(len(arr) == 0):
        return 1
    
    score_ranks = []
    arr.sort(reverse=True)
    
    idx = 1
    score_ranks.append(idx)
    # (고친 부분) ========================
    for i in range(1,N):
        idx += 1
        if (arr[i] < arr[i-1]):
            score_ranks.append(idx)
        else:
            score_ranks.append(score_ranks[-1])
    # (고친 부분) ========================
    
    for i in range(N):
        if (new >= arr[i]):
            return score_ranks[i]
    return N+1


new_rank = get_rank(RANK, new)
# 등수 조건 처리 - 점수판 꽉 참 + 동점일때
if(N == P and new <= RANK[-1]):
    new_rank = -1

print(new_rank)

## 틀린 이유: 같은 등수이면 2 2 4등 이렇게됨