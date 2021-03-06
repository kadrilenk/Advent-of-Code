ans = 0
with open("input01.txt") as f:
    for line in f:
        mark = line[0]
        num = int(line[1:])
        if mark == "+":
            ans += num
        else:
            ans -= num
print("First puzzle:", ans)


ans = 0
i = 0
list = []
with open("input01.txt") as f:
    while i < 10000:
        for line in f:
            mark = line[0]
            num = int(line[1:])
            if mark == "+":
                ans += num
            else:
                ans -= num
            if ans in list:
                print("Second puzzle:", ans)
                i = 10000
                break
            else:
                list.append(ans)
            #print(list)
        i += 1
        f.seek(0)
