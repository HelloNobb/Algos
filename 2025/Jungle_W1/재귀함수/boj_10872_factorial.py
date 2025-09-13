# factorial calculate  >> 재귀함수
def get_factorial(n):
	if (n <=1):
		return 1
	return n * get_factorial(n-1)

N = int(input()) # 0<=N<=12
print(get_factorial(N))