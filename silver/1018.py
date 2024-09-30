n, m = map(int, input().split())
isB = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    wbs = input()
    for sq in range(len(wbs)):
        isB[i][sq] = wbs[sq] == "B"

smallCnt = 10000000
# print(isB)

for y in range(n-7):
    for x in range(m-7):
        cnt = 0
        firstIsB = isB[y][x]
        # print(x, y, firstIsB)
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    if firstIsB != isB[i+y][j+x]:
                        cnt+=1
                else:
                    if firstIsB == isB[i+y][j+x]:
                        cnt+=1
        cnt = min(cnt, 64-cnt)
        smallCnt = min(cnt, smallCnt)

print(smallCnt)
