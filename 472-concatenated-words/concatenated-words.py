class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        w = set(words)
        incorrect = set()
        def dfs(word):
            if word in w:
                return True
            elif word in incorrect:
                return False
            else:
                for i in range(1, len(word)):
                    if word[:i] in w:
                        if dfs(word[i:]):
                            return True
                        else:
                            incorrect.add(word[i:])
                incorrect.add(word)
                return False
        for word in words:
            w.remove(word)
            if dfs(word):
                res.append(word)
            w.add(word)
        return res