'''
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""​​​​​​​
##
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
##

=====
# 개념
두 문자열이 
- 유클리드 호제법


'''



# 정답코드 =====

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 같은 반복주기로 생긴 문자열인지 확인
        if (str1 + str2 != str2 + str1):
            return ""
        
        # 두 문자열 길이의 최대공약수 구하기
        len1 = max(len(str1), len(str2))
        len2 = min(len(str1), len(str2))

        def get_gcd(a, b):
            while b > 0:
                a, b = b, a%b
            return a
        cycle = get_gcd(len1, len2)
        rslt = str1[:cycle]
        return rslt
        

'''



# 내가푼코드 =====
<sol 1>
1: 더 짧은 문자열을 찾는다.
2: 최소 반복주기 문자열을 구한다. (ex. ABAB -> AB)
    - 이때, 반복주기가 없으면 전체문자열이 하나의 반복주기
3: 긴 문자열 앞에서부터 하나하나 문자 뽑아 비교하며 주기가 끝까지 반복되는지 확인한다.

<sol 2>
1: 문자열 2개에서 앞에서부터 하나씩 문자를 뽑아 비교
    -반복주기에 문자 추가하며 업데이트
        > 의문: 반복주기가 AB인데 ABAB로 처리되면, ABABAB일때 틀리도록 처리되지않나?
        > 의문: 반복주기가 ABAB로 나왔을때 이를 AB로 어떻게 알고 바꾸지?
                ABAAABAA일 경우 ABAA로 바꾸기

        --> * 그럼 끝나고 남은 문자들을 새로운 반복주기로 만들어서 기존 반복주기에
        나눠떨어지는지 체크 (이중체크방식)하자!
            > 반례: 반복주기가 나눠떨어지지않을수있음.. 1차가 5주기, 2차가 4주기일수있음
            
2: 한쪽이 끝나면 다른쪽은 주기의 첫번째부터 시작-> 끝까지 
    ABABCABAB / ABABC    |     ABABAB / ABAB     |     ABABA / AB
    - 
'''
import sys
input = sys.stdin.readline
from collections import deque

class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        cycle1 = deque() #1차 반복주기 (짧은 문자열)
        cycle2 = deque() #2차 반복주기 (남는 문자열 / 2차 검증용)
        if str1 == str2:
            return str1
        # 1차 반복주기 계산
        minLen = min(len(str1), len(str2))
        for i in range(minLen):
            if (str1[i] == str2[i]):
                cycle1.append(str1[i])
            else:
                return ""
        # 2차 반복주기 계산
        if (len(str1) > len(str2)):
            for i in range(minLen, len(str1)):
                cycle2.append(str1[i])
        else:
            for i in range(minLen, len(str2)):
                cycle2.append(str2[i])
        
        # 반복 주기 검증
        if (len(cycle1) >= len(cycle2)):    
            while (cycle1):
                for x in cycle2:
                    if not cycle1:
                        return ""
                    y = cycle1.popleft()
                    if x != y:
                        return ""
        else:
            while (cycle2):
                for x in cycle1:
                    y = cycle2.popleft()
                    if x != y:
                        return ""
        
        return "".join(cycle2)