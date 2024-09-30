a = {}
b = {}
total = 0
answer = "3"

while not answer == "":
    answer = input()
    if a.get(answer):
        a[answer] += 1
    else:
        a[answer] = 1

total = sum(a.values())

for key, value in a:
    b[key] = round(value / total * 100, 4)

b = sorted(b.items())

for i in b:
    print(i[0]+ " " + i[1])