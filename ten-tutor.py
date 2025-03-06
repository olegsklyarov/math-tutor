from random import randint


while True:
    a = randint(1, 10)
    b = randint(1, 10)
    er = a + b
    ar = None
    while True:
        try:
            print(f"{a} + {b} = ", end="")
            ar = int(input().strip())
            break
        except KeyboardInterrupt:
            exit()
        except:
            pass
    print('✅' if er == ar else '❗️');

