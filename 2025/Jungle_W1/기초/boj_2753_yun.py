def get_yun(x):
	if x % 4 == 0 and (x%100 != 0 or x % 400 == 0):
		return 1
	else:
		return 0

x = int(input())
print(get_yun(x))