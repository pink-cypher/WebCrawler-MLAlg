import random

class MarkovModel:
    def __init__(self):
        self.model = {}

    def train(self, data):
        for word in data:
            for i in range(len(word)):
                prefix = word[:i]
                next_char = word[i]
                if prefix not in self.model:
                    self.model[prefix] = []
                self.model[prefix].append(next_char)

    def generate(self, max_length=12):
        prefix = ""
        result = ""
        while len(result) < max_length:
            if prefix not in self.model:
                break
            next_char = random.choice(self.model[prefix])
            result += next_char
            prefix += next_char
        return result