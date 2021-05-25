import random

class Words:
    
    def __init__(self):
        self.words = []
        wordfile = open('3000english.txt', 'r')
        self.words = [w.strip('\n').upper() for w in wordfile.readlines()]
        wordfile.close()

    def random_word_choice(self):
        random_word = ''
        random_word = random.choice(self.words)
        print('the word is selected randomly')
        return random_word

if __name__ == '__main__':
    allwords = Words()
    print(allwords.words)
    print(allwords.random_word_choice())
