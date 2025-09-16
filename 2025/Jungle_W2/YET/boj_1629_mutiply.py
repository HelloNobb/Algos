# A,B,C 모두 2억이하 자연수 / A를 B번 곱한 수를 알고 싶다! (결과를 C로 나눈수)
import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())

tmp = 1
for i in range(B):
    tmp *= A

result = tmp % C
print(result)