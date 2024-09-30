n, k = map(int, input().split())

data = 1
for i in range(k):
    data *= (n-i)
for j in range(1, k+1):
    data /= j

print(data % 1000000007)