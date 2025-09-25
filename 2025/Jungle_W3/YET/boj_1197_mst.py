#최소신장트리 Minimum Spanning Tree
import sys
input = sys.stdin.readline
# V: vertex / E: 간선
V,E = map(int, input().split())

for i in range(E):
    A,B,C = map(int, input().split())