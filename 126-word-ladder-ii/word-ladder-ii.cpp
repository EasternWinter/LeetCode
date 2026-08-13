class Solution {
public:
    vector<vector<string>> findLadders( string beginWord, string endWord, vector<string>& wordList) {
        vector<vector<string>> ans;

        unordered_set<string> words(wordList.begin(), wordList.end());
        if (!words.count(endWord))
            return ans;

        // parent[word] = words that can precede `word`
        unordered_map<string, vector<string>> parent;

        unordered_set<string> current{beginWord};
        words.erase(beginWord);

        bool found = false;

        while (!current.empty() && !found) {
            unordered_set<string> next;

            for (const string& word : current) {
                string temp = word;

                for (int i = 0; i < temp.size(); ++i) {
                    char original = temp[i];

                    for (char c = 'a'; c <= 'z'; ++c) {
                        if (c == original)
                            continue;

                        temp[i] = c;

                        if (!words.count(temp))
                            continue;

                        next.insert(temp);
                        parent[temp].push_back(word);

                        if (temp == endWord)
                            found = true;
                    }

                    temp[i] = original;
                }
            }

            // Remove only after processing the whole level.
            // This allows multiple shortest parents.
            for (const string& word : next)
                words.erase(word);

            current = move(next);
        }

        if (!found)
            return ans;

        // Reconstruct paths from endWord -> beginWord.
        vector<string> path{endWord};

        function<void(const string&)> dfs = [&](const string& word) {
            if (word == beginWord) {
                vector<string> result(path.rbegin(), path.rend());
                ans.push_back(move(result));
                return;
            }

            for (const string& p : parent[word]) {
                path.push_back(p);
                dfs(p);
                path.pop_back();
            }
        };

        dfs(endWord);
        return ans;
    }
};