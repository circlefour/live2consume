import random

class SearchStringGenerator:
    def __init__(self, word_list='words.txt', min_words=1, max_words=3):
        self.min_words = min_words
        self.max_words = max_words

        with open(word_list) as f:
            self.word_list = [line.rstrip('\n') for line in f if line.strip()]

        print('a collected word from the word txt', word_list[0])

    def get_rand_word(self):
        return random.choice(self.word_list)

    def get_search_string(self):
        word_count = random.randint(self.min_words, self.max_words)
        return ' '.join(self.get_rand_word() for _ in range(word_count))
