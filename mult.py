from random import shuffle

tasks = []
for a in range(1, 11):
    for b in range(a, 11):
        tasks.append((a, b))
shuffle(tasks)

solved = 0
mistakes = 0

for a, b in tasks:
    expected = a * b
    actual = None
    while True:
        try:
            print(f"{a} * {b} = ", end="")
            actual = int(input().strip())
            if expected == actual:
                solved += 1
                progress = int((solved / len(tasks)) * 100)
                print(f"✅ прогресс {progress}%, ошибок: {mistakes}")
                break
            else:
                mistakes += 1
                print(f"❌ прогресс {progress}%, ошибок: {mistakes}")
        except KeyboardInterrupt:
            exit()
        except:
            pass
