from operator import length_hint


N = int(input())
P = [int(x) for x in input().split()]
M = int(input())
Q = [int(x) for x in input().split()]

length_R = max(N,M) + 1
R = [0] * length_R
for i in range(length_R):
    R[i] = (P[i] if i <= N else 0 ) + (Q[i] if i <= M else 0)
while length_R > 0 and R[length_R - 1] == 0:
    length_R -= 1
if length_R == 0:
    print(0)
else:
    print(*R[:length_R])
 