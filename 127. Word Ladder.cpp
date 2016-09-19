// Time:  O(n)
// Space: O(n)

// BFS
class Solution {
public:
int ladderLength(string beginWord, string endWord, unordered_set<string>& wordList) {
        queue<string> toVisit;
        int dist = 2;
        wordList.insert(endWord);
        string word = beginWord;
        getNeighbour(beginWord, wordList, toVisit);
        while (!toVisit.empty()) {
            int size = toVisit.size();
            for (int i = 0; i < size; ++i) {
                word = toVisit.front();
                toVisit.pop();
                if (endWord == word)
                    return dist;
                else {
                    getNeighbour(word, wordList, toVisit);
                    wordList.erase(word);
                }
            }
            ++dist;
        }
        return 0;
    }

    void getNeighbour(string word, unordered_set<string>& wordList, queue<string>& toVisit) {
        string temp;
        for (int i = 0; i < word.length(); ++i) {
            temp = word;
            for (int j = 0; j < 26; ++j) {
                temp[i] = ('a' + j);
                if (wordList.find(temp) != wordList.end()) {
                    toVisit.push(temp);
                    wordList.erase(temp);
                }
            }
        }
    }
};

// Time:  O(n)
// Space: O(n)

// BFS from both end
class Solution {
public:
    int ladderLength(string beginWord, string endWord, unordered_set<string>& wordDict) {
        unordered_set<string> head, tail, *phead, *ptail;
        head.insert(beginWord);
        tail.insert(endWord);
        int dist = 2;
        while (!head.empty() && !tail.empty()) {
            if (head.size() <= tail.size()) {
                phead = &head;
                ptail = &tail;
            }
            else {
                phead = &tail; 
                ptail = &head;
            }
            unordered_set<string> tempSet; 
            for (auto itr = phead->begin(); itr != phead->end(); ++itr) {
                string word = *itr;
                wordDict.erase(word);
                for (int p = 0; p < word.length(); ++p) {
                    string temp = word;
                    for (int k = 0; k < 26; ++k) {
                        temp[p] = 'a' + k;
                        if (ptail->find(temp) != ptail->end())
                            return dist;
                        if (wordDict.find(temp) != wordDict.end()) {
                            tempSet.insert(temp);
                            wordDict.erase(temp);
                        }
                    }
                }
            }
            dist++;
            swap(*phead, tempSet);
        }
        return 0; 
    }
};