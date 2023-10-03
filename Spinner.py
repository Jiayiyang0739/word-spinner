import random

class Spinner:
    def __init__(self, filename):
        self.synonyms = {}
        self.load_synonyms(filename)

    def load_synonyms(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                word, synonym_string = line.split(':')
                synonyms = synonym_string.split(',')
                self.synonyms[word] = synonyms

    def spin_text(self, text, probability=50):
        words = text.split()
        spun_words = []

        for word in words:
            if word in self.synonyms and random.randint(1, 100) > probability:
                spun_words.append(random.choice(self.synonyms[word]))
            else:
                spun_words.append(word)

        return ' '.join(spun_words)
