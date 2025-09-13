# 세자리수 2개 받기 > 각각 자릿수 반전시켜서 더 큰 수 출력하기
def reverse_num(n):
    n3 = n // 100
    n2 = (n // 10) % 10
    n1 = n % 10
    
    return n3 + n2*10 + n1*100

nums = list(map(int, input().split()))

a_rev = reverse_num(nums[0])
b_rev = reverse_num(nums[1])

if a_rev >= b_rev:
    print(f"{a_rev}")
else:
	print(f"{b_rev}")
