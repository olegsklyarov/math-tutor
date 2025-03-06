from random import randint

m = [[False] * 11 for _ in range(11)]
ok = 0
while True:
    a = randint(1, 10)
    b = randint(1, 10)
    if m[a][b]:
        continue
    er = a * b
    ar = None
    while True:
        try:
            print(f"{a} * {b} = ", end="")
            ar = int(input().strip())
            break
        except KeyboardInterrupt:
            exit()
        except:
            pass
    if er == ar:
        m[a][b] = m[b][a] = True
        ok += 1
        if ok == 50:
            break
    print('✅' if er == ar else '❗️');

