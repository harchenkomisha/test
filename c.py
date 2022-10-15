N = int(input())
a = (input.split())
P = int(input())
a.pop(P-1)
(Q,K) = [int(s) for s in input().split()]
a.insert(K,Q - 1)
print(" ".join([str(i) for i in a]))