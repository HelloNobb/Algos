
## 일단 1~N까지 각자 그래프 만들어서 연결된애들 걍 싸그리넣기
## 그다음, 루트 1부터 시작해서 for 자식 검색해서 자식이 키인 딕셔너리의 값에서 루트 지우기
## 반복하다보면 

import sys
from pprint import pprint
def rl():
	return sys.stdin.readline().rstrip()
K = int(rl())
print(K)
l_list = {}
for _ in range(K - 1):
	l, r = map(int, rl().split())
	if l in l_list:
		l_list[l].append(r)
	else:
		l_list[l] = [r]
	if r in l_list:
		l_list[r].append(l)
	else:
		l_list[r] = [l]
pprint(l_list)
plr = {}
son_mom = [0] * (K + 20)
for k, ele in l_list.items():
	print(k, ele)
cou = 0
def findFamily(p):
	children = l_list[p]
	plr[p] = [*children]
	for child in plr[p]:
		son_mom[child] = p
		#print("=========", child, p)
		# plr에 가서 child의 부모 삭제
		l_list[child].remove(p)
		if child not in plr:
			findFamily(child)
findFamily(1)
print("==============================")
print(plr)
for i in range(2,K):
    print(son_mom[i])
    
    #### 리커젼 제한 1000번 풀면 되긴함