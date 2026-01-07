class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        count = 0
        visited = {beginWord}
        queue = deque([(beginWord, 1)])
        als = 'abcdefghijklmnopqrstuvwxyz'

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for b in als:
                    mut = word[:i] + b + word[i+1:]
                    if mut in words and mut not in visited:
                        queue.append((mut, steps+1))
                        visited.add(mut)
        
        return 0