from random import shuffle


class Questions:
    def __init__(self):
        self.questions = []
        for a in range(1, 11):
            for b in range(a, 11):
                self.questions.append((a, b))
        shuffle(self.questions)

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        l = len(self.questions)
        if self.i == l:
            raise StopIteration
        progress = int(((self.i + 1) / l) * 100)
        return (*self.questions[self.i], progress)


solved = 0
mistakes = 0

for a, b, progress in Questions():
    expected = a * b
    actual = None
    while True:
        try:
            print(f"{a} * {b} = ", end="")
            actual = int(input().strip())
            if expected == actual:
                solved += 1
                print(f"✅ прогресс {progress}%, ошибок: {mistakes}")
                break
            else:
                mistakes += 1
                print(f"❌ прогресс {progress}%, ошибок: {mistakes}")
        except KeyboardInterrupt:
            exit()
        except:
            pass
