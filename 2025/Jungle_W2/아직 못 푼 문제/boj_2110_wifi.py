import sys
input = sys.stdin.readline

N,C = map(int, input().split()) #N: 집 개수, C: 공유기 개수
X = [int(input()) for i in range(N)] #X: 집 좌표들(N개)