N = int(input())
pupils = {}
MARCS_COUNT = 3 

for _  in range(N):
    pupil =  input().split()
    last_name = pupil[0]
    pupils[last_name] = [int(i) for i in pupil[1:]]
    print(f'{last_name} {(sum(pupils[last_name]) / MARCS_COUNT):.2f}')
