def calcMod(n, m):
    res = n%m
    return res if not res else res-m if n<0 else res

casos, modulo = [int(x) for x in input().split()]
dic = {}
while (casos != 0 and modulo != 0):
    for i in range(casos):
        num = int(input())
        dic[i] = (calcMod(num, modulo), num%2, num)

    dicOrd = sorted(dic.values(), key=lambda x: (x[0], -x[1], -x[2] if x[1] == 1 else x[2]))
    print(casos, modulo)
    for j in dicOrd:
        print(j[2])
    casos, modulo = [int(x) for x in input().split()]
    dic.clear()

print(0, 0)
