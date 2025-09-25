'''최소신장트리 minimum spanning tree (MST)'''

# 정점 번호: 1..V
# edges: (w, u, v) 형태의 리스트 (가중치, 정점, 정점)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
    
    def find(self, x):
        #경로 압축 안한 버전 (-> 새 부모로 )
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return self.parent[x]
        # 경로 압축
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        # union: a가 속한 집합과 b가 속한 집합 합침
        ra, rb = self.find(a), self.find(b)