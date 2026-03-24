import sys
input = sys.stdin.readline

# 문자열로 입력받아 뒤집기 (slicing)-- C: 문자열 끝에 \0 있다는거 이용해 swap 방식으로 구현해야함
A = input().strip()[::-1]
B = input().strip()[::-1]

## 방법 1) 짧은애 끝날때까지 carry 계산-> 긴쪽 carry 따로 계산 =========

def get_carry1 (A, B):
    CARRY = 0
    flag = 0
    
    for i in range(min(len(A), len(B))):
        if int(A[i]) + int(B[i]) + flag >= 10:
            flag = 1
            CARRY += 1
        else:
            flag = 0
            
    if flag == 1:  
        if len(A) > len(B):
            for i in range(len(B), len(A)):
                if int(A[i]) + flag >= 10:
                    CARRY += 1
                else:
                    break
        else:
            for i in range(len(A), len(B)):
                if int(B[i]) + flag >= 10:
                    CARRY += 1
                else:
                    break
                
    return CARRY
            
## 방법 2) 길이 따로 계산해서 짧은쪽 나머지부분을 0으로 채우기
def get_carry2 (A, B):
    CARRY = 0
    FLAG = 0
    i, j = len(A) - 1, len(B) - 1
    
    while i >= 0 or j >= 0:
        val_A = int(A[i]) if i >= 0 else 0 ### [!]
        val_B = int(B[j]) if j >= 0 else 0
        
        if val_A + val_B + FLAG >= 10:
            FLAG = 1
            CARRY += 1
        else:
            FLAG = 0
        i -= 1
        j -= 1
    
    return CARRY

print(get_carry1 (A,B))

'''
# 힌트

1: 입력받은 2개의 정수를 문자열 취급하여 reverse()처리
2: 역순 문자열 2개를 왼쪽부터 하나씩 차례로 더하며 carry수 계산
'''
