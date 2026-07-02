class WordDictionary:

    def __init__(self):
        self.trie={}

    def addWord(self, word: str) -> None:
        d=self.trie
        for c in word:
            if c not in d:
                d[c]={}
            d=d[c]
        d['.']='.'

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return '.' in node
            c = word[i]
            if c == '.':
                # Try all possible paths
                for key in node:
                    if key != '.' and dfs(i + 1, node[key]):
                        return True
                return False
            if c not in node:
                return False
            return dfs(i + 1, node[c])
        return dfs(0,self.trie)
