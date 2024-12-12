class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for p in punctuation:
                        content = content.replace(p, '')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words
    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        positions = {}
        for name, words in all_words.items():
            if word in words:
                positions[name] = words.index(word) + 1
            else:
                positions[name] = -1
        return positions
    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        counts = {}
        for name, words in all_words.items():
            counts[name] = words.count(word)
        return counts
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))