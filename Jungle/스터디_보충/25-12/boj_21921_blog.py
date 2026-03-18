'''
Jungle.스터디_보충.25-12.boj_21921_blog의 Docstring
(~8:30)

# 문제 조건 ===========
====
<input>
N X (블로그 시작하고 지난 일수 , 희망 집계 일수)
[1~N일차까지 각 하루 방문자수]

<output>
: x일동안 가장 많이 들어온 방문자 수 (0명->SAD 출력)
====

 * 1 <= x  <= N <= 25만
 
 * 0 <= 방문자수 <= 8000


# 접근 계획 ===========
1- 

 * 완탐이 가능한가?
	: 최악= 25만일 중 5일 -> 5만번 미만 반복? -> 가능?
 
1: 앞에서부터 x개 뽑아 합 구하기
2: 반복(N-x + 1회)하며 최대 합 갱신 (만약 같은 합 나오면 카운트)
'''
import sys
input = sys.stdin.readline
from collections import deque

N,X = map(int, input().split()) # 5 2
VISIT = list(map(int, input().split()))

def get_max_visited_term(VISIT):
    max_sum = -1
    same_sum_count = 0
    term_sum = 0
    # 일단 첫 x일간의 합 구하기 ====
    for i in range(X):
        term_sum += VISIT[i]
    
    max_sum = term_sum
    
    # 그 다음부턴 하나 빼고 하나 넣으며 전체 합 구하기 ====
    for i in range(X, N):
        remove_idx = i-X
        add_idx = i
        
        term_sum = term_sum - VISIT[remove_idx] + VISIT[add_idx]
        
        if (term_sum == max_sum):
            same_sum_count += 1
        
        if (term_sum > max_sum):
            same_sum_count = 0
            max_sum = term_sum
        
    return max_sum, same_sum_count

max_sum, same_sum_count = get_max_visited_term(VISIT)
if (max_sum == 0):
    print("SAD")
else:
    print(max_sum)
    print(same_sum_count+1) #최초 기간 포함
    
    
'''
<시간초과 해결 전략>
 - 2중 for문으로 매번 합 구하지 말고 앞에서 하나씩 pop, 뒤에 하나씩 append 하는 식
	> 

'''