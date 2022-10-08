N = int(input())
a = [int(s) for s in input().split()]
P = int(input())
a.insert(0,a.pop(P - 1))
print(" ".join([str(i) for i in a]))