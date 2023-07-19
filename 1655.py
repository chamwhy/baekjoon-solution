n = int(input())

arr = []
newArr = []

    

for i in range(n):
    arr.append(int(input()))

for i in range(n):
    ind = 0
    for j in range(len(newArr)):
        if arr[i] > newArr[j]:
            ind = j
            break

    newArr.insert(ind, arr[i])

    if len(newArr) % 2 == 0:
        print(min(newArr[len(newArr)/2-1], newArr[len(newArr)/2]))
    else:
        print(newArr[(len(newArr)-1)/2])

