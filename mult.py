from questions import Questions


solved = 0
mistakes = 0

for a, b, progress in Questions(is_full=False):
    expected = a * b
    actual = None
    while True:
        try:
            print(f"{a} * {b} = ", end="")
            actual = int(input().strip())
            if expected == actual:
                solved += 1
                print(f"✅ прогресс {progress}%, верно: {solved}, ошибок: {mistakes}")
                break
            else:
                mistakes += 1
                print(f"❌ прогресс {progress}%, верно: {solved}, ошибок: {mistakes}")
        except KeyboardInterrupt:
            exit()
        except:
            pass
