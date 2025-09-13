import sys
input = sys.stdin.readline

arr = [1,2,3,3,3,3,3,3,3,3,3,3,3,3,4,5]


def get_count(A, t_idx):	# 타깃인덱스 위아래까지 배열에 타깃값이 총 몇개들었는지 리턴
    amount = 1
    new_idx = t_idx
    
    while new_idx >= 0:
        new_idx = new_idx - 1
        if A[new_idx] == A[t_idx]:
            amount += 1
            continue
        break
    new_idx = t_idx
    while new_idx < len(A):
        new_idx = new_idx + 1
        if A[new_idx] == A[t_idx]:
            amount+= 1
            continue
        break
    return amount
        
print(get_count(arr, 3))  