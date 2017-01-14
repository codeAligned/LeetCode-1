### Twitter
* 433   Minimum Genetic Mutation
* 296   Best Meeting Point
* 269   Alien Dictionary
* 341   Flatten Nested List Iterator
* 251   Flatten 2D Vector
* 355   Design Twitter
* 218   The Skyline Problem
* 12    Integer to Roman
* 161   One Edit Distance
* 146   LRU Cache
* 202   Happy Number
* 208   Implement Trie (Prefix Tree
* 140   Word Break II
* 60    Permutation Sequence
* 42    Trapping Rain Water
* 149   Max Points on a Line
* 10    Regular Expression Matching
* 206   Reverse Linked List
* 43    Multiply Strings
* 23    Merge k Sorted Lists
* 20    Valid Parentheses
* 235   Lowest Common Ancestor of a Binary Search Tree
* 118   Pascal's Triangle
* 56    Merge Intervals
* 378   Kth Smallest Element in a Sorted Matrix
* 380   Insert Delete GetRandom O(1)
* 323   Number of Connected Components in an Undirected Graph
* 468   Validate IP Address
* 407   Trapping Rain Water II
* 44    Wildcard Matching


#### My Online Assesment
*	Parent, Child and Tree
	*	given a table with id and p_id 
	*	print id and type (root, inner, leaf) by order
```mysql
/* left join results to decide parents or children */
select distinct t1.Id, if(t1.P_id, if(t2.Id, "Inner", "Leaf"), "Root") as node_tpye 
from tree as t1 
left join tree as t2 on t1.Id = t2.P_id 
order by t1.Id
```


*	Hacking Time
	*	calculate a shifting letter encryption algorithm
	*	use key to decrypt message
```python3
# Complete the function below.
# need to decide the starting number
key = "8251220"

def  decrypt(encrypted_message):
    res = ""
    key_len = len(key)
    i = 0
    for c in encrypted_message:
        if c.isalpha():
            ascii_c = ord(c)
            start_ascii = ord('a' if c.islower() else 'A')
            res += chr(start_ascii + (ord(c) - start_ascii - int(key[i % key_len])) % 26)
            i += 1
        else:
            res += c
    return res
```


*	Tweet Recommendation
	*	given follow and like relations
	*	decide whether to recommend a tweet to user
```python3
# Complete the function below.
# followGraph_edges is a list of tuples (userId, userId)
# likeGraph_edges is also a list of tuples (userId, tweetId)

from collections import Counter

def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    f_dict = {}
    l_dict = {}
    # collect follow relations
    for f in followGraph_edges:
        if f[0] in f_dict:
            f_dict[f[0]].add(f[1])
        else:
            f_dict[f[0]] = {f[1]}
    # collect likes relations
    for l in likeGraph_edges:
        if l[0] in l_dict:
            l_dict[l[0]].add(l[1])
        else:
            l_dict[l[0]] = {l[1]}
    
    target_follows = f_dict[targetUser]
    cnt = Counter()
    # count likes for tweets from the following people
    for t in target_follows:
        if t in l_dict:
            cnt += Counter(l_dict[t])

    rec_tweet = []
    # decide whether to recommend
    for tweet, times in cnt.items():
        if times >= minLikeThreshold:
            rec_tweet.append(tweet)
    
    return rec_tweet
```


*	Searching a Log File
	*	given a log file with time and message
	*	search for logs within in time range
```java
public Collection<String> search(Collection<String> logLines, LocalTime startDate, LocalTime endDate) {
    List<String> res = new ArrayList<>();
    for (String line: logLines) {
        // fetch time string
        String[] log = line.split("\t");
        String time = log[0];
        
        // parse time string to LocalTime
        DateTimeFormatter dtf = DateTimeFormatter.ISO_DATE_TIME;
        try {
            LocalTime lt = LocalTime.parse(time, dtf);
            if ((lt.equals(startDate) || lt.isAfter(startDate)) && lt.isBefore(endDate))
                res.add(line);
        } catch (Exception e) {
            res.add(line); // multi-line message handling
        }
    }
    return res;
}
```
