A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9, 0}
C = {5, 6}

print(C.issubset(A))
print(C.issubset({5, 7}))
print(A.issuperset(C))
print(A.union(B))
print(A.intersection(B))
print(A.symmetric_difference(B))

D = A.copy()
print(D)