from random import shuffle


class Questions:
    def __init__(self, is_full: bool = False):
        self.questions = []
        for a in range(1, 11):
            for b in range(1 if is_full else a, 11):
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
