'''
[1,2,3 더하기 4] : ~9:15

# 문제 조건 ========
 : n -> 1,2,3 합으로 n 나타내는 방법 수

<input>
* 테스트케이스 수
* (각 테스트케이스의 정수 n)

<output>
: 각 테스트케이스의 경우의수


# 접근 전략 ========
각 정수안에
	* '3' 최대 개 ~ '3' 0개
	and
	* '2' 최대 개 ~ '2' 0개
	* '1' 나머지

1- for문으로 3 최대 개수 ~ 0개 사용하는 경우를 돌린다.
2- 나머지 중에서 2 최대개수 ~ 0개 사용하는 경우를 돌린다.

'''
import sys
input = sys.stdin.readline

# 1,2,3합의 경우의수 반환 ====
def get_123_ways(num):
    left_num = num
    max_three = num // 3
    
    count=0
    for i in range(max_three+1):
        left_num = num - i*3
        
        max_two = left_num // 2
        count += max_two+1
            
    return count

# input ====
T = int(input())
ARR = []
for i in range(T):
    case = int(input())
    ARR.append(get_123_ways(case))

for i in ARR:
    print(i)