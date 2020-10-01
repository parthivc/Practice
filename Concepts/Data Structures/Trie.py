# This is a Trie implementation, used for quick insertion, retrieval, and searching

class Node:

    def __init__(self):
        self.letters = [False] * 26
        self.word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def getIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, word):
        word = self.prepare(word)
        runner = self.root
        n = len(word)
        for level in range(n):
            index = self.getIndex(word[level])
            if not runner.letters[index]:
                runner.letters[index] = Node()
            runner = runner.letters[index]
        runner.word = True

    def prepare(self, word):
        word = word.lower().strip()
        if not word.isalpha():
            word = ''.join([letter for letter in word if letter.isalpha()])
        return word

    def search(self, word):
        runner = self.root
        n = len(word)
        for level in range(n):
            index = self.getIndex(word[level])
            if not runner.letters[index]:
                return False
            runner = runner.letters[index]
        return runner is not None and runner.word


def main():
    t = Trie()
    words = ["the", "a", "there", "anaswe", "any", "by", "their"]
    for word in words:
        t.insert(word)
    keys = ["the", "these", "their", "thaw"]
    for key in keys:
        print(t.search(key))


if __name__ == "__main__":
    print()
    main()
    print()
