t = int(input())
nms = []
for i in range(t):
    n, m = map(int, input().split())
    nms.append((n,m))

for nm in nms:
    a = 1
    n, m = nm
    for i in range(n):
        a *= (m-i)
    for i in range(n):
        a /= i+1
    print(round(a))