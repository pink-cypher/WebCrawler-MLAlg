import random
import csv
import collections

class MarkovModel:
    def __init__(self):
        self.model = {}

    def train(self, data):
        for word in data:
            for i in range(len(word)):
                key = word[:i]
                next_char = word[i:i+1]
                if key not in self.model:
                    self.model[key] = []
                self.model[key].append(next_char)

    def generate(self, max_length=10):
        key = ""
        result = ""
        for _ in range(max_length):
            next_chars = self.model.get(key)
            if not next_chars:
                break
            next_char = random.choice(next_chars)
            result += next_char
            key = result[-len(key)-1:]
        return result

def generate_credentials(cleaned_csv_path, output_file='backend/data/crackedpass.txt'):
    # Load cleaned words
    words = []
    with open(cleaned_csv_path, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            content_words = row["content"].split()
            words.extend(content_words)

    # Train model and generate credentials
    model = MarkovModel()
    model.train(words)

    raw_generated = [model.generate() for _ in range(50)]
    root_counts = collections.defaultdict(list)
    final_creds = [] 

    # Enforcing an upper bound of 20% repetition for username/password roots
    max_final = 10
    max_per_root = max(1, int(max_final * 0.2))

    for cred in raw_generated:
        root = cred[:4]
        if len(root_counts[root]) < max_per_root:
            root_counts[root].append(cred)
            final_creds.append(cred)
        if len(final_creds) >= max_final:
            break
    
    print("Generated credentials:", final_creds)

    with open(output_file, "w") as f:
        for cred in final_creds:
            f.write(cred + "\n")

    return final_creds