def get_grade(x):
	if x >= 90:
		return 'A'
	elif x >= 80:
		return 'B'
	elif x >= 70:
		return 'C'
	elif x >= 60:
		return 'D'
	else:
		return 'F'

x = int(input())

print(get_grade(x))
