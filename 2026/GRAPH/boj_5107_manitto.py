'''
2026.GRAPH.boj_5107_manitto의 Docstring

문제
- 꼬리물기가 연결고리로 연결되는 경우가 몇개인지 찾기
해결
<접근법1>: 꼬리물기 시작점 설정하고 업데이트-> 되돌아오면 cnt+1하고 버리기
1) 일단 모든 사람에게 고유번호 및 진입차수 기록
	everyone[0] = {Sally, 1}
	

'''
import sys
input = sys.stdin.readline

N = int(input())
everyone = []
# 공백 기준 문자열 잘라 받기
for i in range(N):
    p1, p2 = input().split()
    everyone.append(p1)
    