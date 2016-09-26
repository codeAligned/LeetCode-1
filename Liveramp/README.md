### Liveramp

#### My Online Assesment

*   task1. Monkey
```cpp
// Time: O(N)
// Space: O(N)

#include <queue>

int solution(vector<int> &A, int D) {
    // write your code in C++11 (g++ 4.8.2)
    int size = A.size();
    vector<int> earliestTime;
    deque<int> dq;
    if (D <= 0)
        return -1;
    int count = 0;
    for (int i = 0; i < size; ++i) {
        // remove numbers out of range
        while (!dq.empty() && dq.front() < i - D + 1)
            dq.pop_front();
        // remove numbers greater than the incoming number
        while (!dq.empty() && A[i] != -1 && A[dq.back()] > A[i])
            dq.pop_back();
        // D -1 in a row will fail to cross river
        if (A[i] != -1) {
            dq.push_back(i);
            count = 0;
        }
        else
            count += 1;
        if (count == D)
            return -1;
        // record earliest time for each sliding window
        if (i >= D - 1)
            earliestTime.push_back(A[dq.front()]);
    }
    // cross river time depends on the biggest time among all earliest time
    int max = -1;
    for (size_t j = 0; j < earliestTime.size(); ++j) {
        if (earliestTime[j] > max)
            max = earliestTime[j];
    }
    return max;
}
```
*   task2. 
    *   explain
    *   why LiveRamp excite you.

>   1.

>   I treat step length D as a window slot, which can represent the range of how far the monkey can reach at one time.

>   Then I use a deque, which is a double-end queue, to record the index of the possible minimum time of reaching each window slot (length D). Then the goal becomes to find the maximum among all the possible minimum time.

>   As the sliding window moves on, the deque will pop from the front to kick out the index that is out of range. Then the deque will also compare the number on the back with the incoming number (according to the index). If the number in the deque is already bigger than the incoming number, then it has no chance to becoming the minimum, so we remove it from the back, and push the new number in the deque.

>   So at any time, the deque keeps the original sequence in order, as well as the minimum at the front.

>   And during the iteration, we need to handle the situation that there are D -1 in a row, which means there is no way to cross the river.

>   Since the numbers are push to or pop from the deque only once, the time complexity of this algorithms is O(N), where N is the length of array A. While the space complexity is O(N) as well, because the dq is at most D in length, the earliestTime is at most N - D in length.

>   2.

>   I see the big data area so promising that everyone should be connected in some way through any form of data. As a Computer Science major undergraduate student, I had solid foundations on computer systems programming, but far more than enough skills on data science. So I took Machine Learning and Data Science courses online during this Summer, and had an overview of what we can do with a huge amount of data, which really excite me to engage in this area. Since LiveRamp is the leader in data connectivity, which perfectly matches my goal, I really want to join and discover more in the industry, hone my skills with the help of those excellent engineers, and fianlly contribute myself to this area.


Interview Preparation
---

#### 算法题：青蛙过河。


 输入一个Array, X，D，最早可以跳过X的时刻。 

1. 有只青蛙要过河，起始位置position 0，一路跳到 X，每次跳得距离 在1 ~ D，一秒可以跳很多次的样子只要有叶子可以停。。。
2. 每秒都会落下一片叶子，青蛙可以停在上面（叶子不会消失）
3. 给了一个Array, Array[k] 表示，k秒落下叶子的位置

>	我的算法是根据输入数组A[]，构建一个新数组，下标是位置，数组元素是叶子落在这个位置的最短时间，如果没有叶子掉落在这个位置，则为正无穷。然后在这个新数组上做类似于leetcode那道maximum sliding window，这时window size是青蛙能跳的最大步数，每次sliding window返回最小值。然后取这些最小值里的最大值。如果最大值是正无穷，说明没法到达对岸，返回-1。

```cpp
// Time:  O(n), because each element is push or pop once
// Space: O(k)

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> result;
        deque<int> dq;
        for (int i = 0; i < n; ++i) {
            while (!dq.empty() && dq.front() < i - k + 1) // remove numbers out of range k
                dq.pop_front();
            while (!dq.empty() && nums[dq.back()] < nums[i]) // remove numbers less than incoming number
                dq.pop_back();  
            dq.push_back(i);
            if (i >= k - 1) 
                result.push_back(nums[dq.front()]);
        }
        return result;
    }
};
```

<br>

>   感谢楼主分享，这道题其实可以用类似于Maximum Gap的思想来做：把0~X这X+1个格子按照每个bin长为D+1等分，共N = (X+1)/(D+1)个bin（不是整数的话取ceil）

>   因为青蛙最大能够跳过D的距离，所以

>   1. 在同一个bin内的任意两片叶子肯定能跳过，
>   2. 中间隔了一个或以上bin的两片叶子肯定无法直接跳过（即青蛙必定要从一个bin跳到相邻的bin，不可能跨bin跳）
>   因此，青蛙必定要在这N个bin之间跳正好N-1次（这以外的跳跃都是发生在bin内部，所以就不管了），才能到达X。我们只要看这N个bin间是不是建立起了N-1次联系就可以了。为此，我们给每个bin维护一个min和max值。每次加入一片叶子，就更新其对应bin的min/max值。然后检查：是否因为这个叶子加入，使得该bin和其相邻的bin能够建立起联系。如果是的话，“联系”值++。最后，能够跳到X的充要条件是“联系”值==N-1。

>   该算法将每片叶子放入bin，检查与周围bin的连接情况等都是O(1)操作，因此最后总复杂度是O(arrLen)。空间复杂度则是O(X/D)。

<br>

>	青蛙过河。感谢地里大家分享的解法，这里提供一个自己的另一个思路吧。这道题最tricky的地方应该就是，原先落下的叶子够不到，但是在更新的过程中，突然又能够到了，怎么样有效更新当前的状态呢？我用了下几个变量/结构来保存/更新状态：

>	*	一个hashset，暂且叫做reachable， 用于保存当前能够到达的所有position，空间复杂度是O(N + D)。更新过程是顺序增长，即1,2,3,4,5,6，不会出现1,2,5,6的情况（下面会解释），则一旦它的长度大于等于我们的距离X，则表示能够到达对岸。
>	*	第二个hashset，暂且叫做unused，用于保存当前已经存在却无法够到的所有叶子，空间复杂度O(N)。
>	*	一个边界，在此边界前的所有叶子都没有价值，或者说通过那些叶子不能帮助青蛙跳得更远，暂且叫做usefulBound。

>	分析情况如下

>	1. basecase。根据我们上述的定义
>		1. 如果reachable已经覆盖了X，我们返回当前时间 
>		2. 如果遍历了所有可用的叶子依然不能到达X，返回-1
>	2. 更新过程，一共会有三种情况：
>		*	case 1：如果叶子的位置在usefulBound之前，我们直接跳过。
>		*	case 2：如果叶子的位置不在reachable里，表示目前无法够到，我们把这个叶子存入unused里。
>		*	case 3：除去前两种情况，我们可以用当前的叶子更新我们的状态。假设当前时间是 i，叶子位置是 s，reachable的size是k（则表示1 - k都可达），青蛙踩在 s 上能够到达最远的地方则是 s + D，我们需要插入reachable的位置就只有 pos = [k + 1, s + D]。我们挨个插入保证了reachable的范围是无缝的，并且每个position最多插入一次。这时候我们需要再做另一件事，每当我们插入一个新的pos到reachable，我们检查pos是否存在unused里，如果存在，我们只需要把更新的范围从s + D延长到 pos +Ｄ。由于pos是单调递增的，我们保证了每个叶子最多只被检查了一次。
>	3. 更新结束后做两件事，（i）更新usefulBound = reachable.size() - D + 1，比如当前能覆盖1 - 6， D = 3，那新叶子至少必须在4及其以后才会有用。（2）判断reachable是否覆盖目的地X，如果覆盖，返回当前时间i

 >	复杂度：空间是O（N+D）不用多说，关于时间，由于input给的叶子array长度是N，则叶子数量不会超过N，时间也不超过N；对于reachable，最远的可达范围是最后一片叶子+最后一跳，所以是N + D，并且这些位置最多只会被插入一次；对于每次检查当前时间的叶子，三种情况都只做了常数次操作，而且每个叶子也仍然最多被插入unused这个set里一次，并且由于reachable递增的特性，每个unused里的叶子也最多只被check一次。总的下来时间复杂度就是O(N + D)，由于两者量级相同可以简化为O(N)。不知道分析有没有遗漏的地方。

---

#### 关于我做过的free response的第一题，怎么解释你的算法

>	这个没什么特别多说的，因为大家算法不同，但我觉得你如果写到白板上要注意以下几点. 

>	1. 有逻辑，进行分段或者标数字. 
>	2. 尽量不要说得太难太复杂，因为估计看你答案的都是HR
>	3. 运用方法标出重点，比如我最喜欢用的就是 find the *ONLY* node that .....
>	4. 对于解释算法，我觉得可以这样，用一段两三句话说整体思路，比如为什么用DP/DFS/...
>	5. 然后两到三段解释几个重点的edge case，或者你代码中的难点，说白了就是如果你给这段代码做comment，那么就重点解释comment，因为其他部分你不说别人也能懂
最后用一段一两句话总结

---

#### 猴子过河

>	这道题其实换汤不换药，但是要注意两个地方：

>	1. 青蛙过河的初始位置是0，目的地位置是X；但是猴子过河初始是-1，到达的位置是河对岸，比如 [0,1,2,3,4,5]，则需要到达6才算过河，一共需要跳7步以上。
>	2. 青蛙过河的input是 时间--->出现叶子的位置，猴子过河里变成了  石头位置--->出现时间。我们需要做的只是预处理把猴子过河里的input 转置一下，就和青蛙过河的input完全一样了。值得一提的是，题目说同一时间只会有一块石头出现，省得我们再想太多。

>	关于复杂度的问题，就是因为（ii）的预处理，导致我们需要首先判断 “最长的时间 t”，也就是数组A中的max，然后开辟一个数组长度为 t + 1来保存  时间--->石头位置，这样问题又退化到青蛙过河。但是这时候的时间长度可能会比原始数组A要长，所以最后的时空复杂度要求是O(N + max(A))。

```cpp
// Time: O(N)
// Space: O(N)

#include <queue>

int solution(vector<int> &A, int D) {
    // write your code in C++11 (g++ 4.8.2)
    int size = A.size();
    vector<int> earliestTime;
    deque<int> dq;
    if (D <= 0)
        return -1;
    int count = 0;
    for (int i = 0; i < size; ++i) {
        // remove numbers out of range
        while (!dq.empty() && dq.front() < i - D + 1)
            dq.pop_front();
        // remove numbers greater than the incoming number
        while (!dq.empty() && A[i] != -1 && A[dq.back()] > A[i])
            dq.pop_back();
        // D -1 in a row will fail to cross river
        if (A[i] != -1) {
            dq.push_back(i);
            count = 0;
        }
        else
            count += 1;
        if (count == D)
            return -1;
        // record earliest time for each sliding window
        if (i >= D - 1)
            earliestTime.push_back(A[dq.front()]);
    }
    // cross river time depends on the biggest time among all earliest time
    int max = -1;
    for (size_t j = 0; j < earliestTime.size(); ++j) {
        if (earliestTime[j] > max)
            max = earliestTime[j];
    }
    return max;
}
```

>   I treat step length D as a window slot, which can represent the range of how far the monkey can reach at one time.

>   Then I use a deque, which is a double-end queue, to record the index of the possible minimum time of reaching each window slot (length D). Then the goal becomes to find the maximum among all the possible minimum time.

>   As the sliding window moves on, the deque will pop from the front to kick out the index that is out of range. Then the deque will also compare the number on the back with the incoming number (according to the index). If the number in the deque is already bigger than the incoming number, then it has no chance to becoming the minimum, so we remove it from the back, and push the new number in the deque.

>   So at any time, the deque keeps the original sequence in order, as well as the minimum at the front.

>   And during the iteration, we need to handle the situation that there are D -1 in a row, which means there is no way to cross the river.

>   Since the numbers are push to or pop from the deque only once, the time complexity of this algorithms is O(N), where N is the length of array A. While the space complexity is O(N) as well, because the dq is at most D in length, the earliestTime is at most N - D in length.


---

#### M City

 一个图，节点表示城市，有M个节点和M-1条边，所以是没有环的，用一个array表示这个图，比如T[x]=y的话那么节点x就和y相连，如果T[x]=x就说明x是首都。现在要分别求出到首都距离为1，2，3...M-1的节点数。hashmap结合arraylist搞定。

> 用一个hashmap重新建了一个图，这样方便查找所有相邻的节点，而不用每次查找整个array。然后用bfs来求每个距离上的节点数。

```python
class Solution:

    def count_dist(self,T):
        distance=[-1]*len(T)
        count=[0]*(len(T)-1)
        for i in range(len(T)):
            if distance[i]<0:
                self.get_dist(T,distance,i)
        for i in range(len(T)):
            if distance[i]>0:
                count[distance[i]-1]+=1
        return count

    def get_dist(self,T,distance,i):
        next=T[i]
        if next==i:
            distance[i]=0
            return 0
        elif distance[next]>0:
            distance[i]=distance[next]+1
            return distance[i]
        else:
            distance[i]=self.get_dist(T,distance,next)+1
            return distance[i]
```

---

#### sequence

 其实是求最大subset，这个set满足里面的数最大的数和最小的数相差不超过1，比如[3,1,2,2,3,4]，那么最长的是[3,2,2,3]，返回4 

>	*	用hashmap统计每个数的重复次数，得到k个不同的数，然后one-by-one scan这k个数，对每个数，计算count[k-1] + count[k] 和 count[k] + count[k+1]的数量，然后更新maxLen。时空复杂度都是O(N)

```python
def max_subsequence(a):
    count={}
    for num in a:
        count[num]=count.get(num,0)+1
    max_len=0
    for num in count:
        max_len = max(max_len,count[num]+count.get(num+1,0))
    return max_len
```

<br>

>	*	sort and count，其实实现的难度和（1）一样，甚至逻辑没有那么清晰，需要考虑清楚index和off-by-one的问题。常数的空间复杂度+O(nlogn)的时间

---

#### six-degree

>	这道题看地里的意思应该就是描述算法优缺点然后做选择了？比较好描述的是DFS, BFS, Dijkstra，然后Bi-direction DFS/BFS/Dijkstra吧，很惭愧没有仔细看过A*算法。

>	这个虽然我没有被面到，但还是想重点来说一说，我觉得这个题特别好；以我本科的角度来看，研究生都是能做到很多很厉害的项目，但其实面试的时候，除非那个人特别懂你做的这类东西，不然你们两个也很难说到细节；但是Six Degree作为一道图形基础题，实现的方式包含的最基础也最重要的算法，我觉得值得好好准备。不光是简单的有思路，我觉得如果有可能，建议自己写一下，一定会对图形题有很大的帮助。而且其实也不难的，我曾经做过这个的作业，就是周作业那种，很快就能写完。但是我们的作业要求只实现三个算法，后来我又自己写了其他，这里简单说一下：

>	*	DFS：这个主要问题就是如果选错的入口，就要一直走到底，可以考虑limited DFS，用stack实现
>	*	BFS：用queue，会缩短平均遍历长度，但是如果每个node的分支很多，会造成不必要的浪费
>	*	DIJKSTRA：这个是给每条边增加权重，实质和BFS一样
>	*	A\*：这个可以帮助解决BFS的弊端，给每个点增加“正确率”的特性，缺点是需要了解计算正确率的function，但是本质还是DFS
>	*	Bi-Direc BFS/Dijk/A*：本质相同，都需要两个queue，两个HashSet，分别给左起点和右起点用

>	最后，再说一句，DFS比较容易记录正确的路径，而剩下几个如果想要track path则需要辅助方法以及precessor

---

### The Max

 Bubble sort is O(n) at best, O(n^2) at worst, and its memory usage is O(1). Merge sort is always O(n log n), but its memory usage is O(n). Explain which algorithm you would use to implement a function that takes an array of integers and returns the max integer in the collection, assuming that the length of the array is less than 1000. What if the array length is greater than 1000? 

>	I believe this is very cool trick question and I would always use Bubble Sort because in the first iteration of bubble Sort my last element would always be the max Integer.Try it with example, you will see. So it does not really matter if the length1000. Infact Bubble Sort would essentially give you runtime of O(n) with only one iteration, last element always being max Int. While using Merge Sort would be costly in running time and memory usage i.e O(nlogn) and O(n) respectively.

---

 Your best friend Betty thinks IMDB is too complicated and challenges you to create a simple movie web site. One page will display movies (with movie name, date it was released, and list of actors). Click on an actor and you're taken to the actor page (with actor name, birthday, bio, and list of movies actor has been in). Please outline the relational table structure of the database for this.. 

>   *   Movie(movie_id(primary), movie_name, movie_year)
>   *   Actor(actor_id(primary), actor_name, actor_birthday, actor_bio)
>   *   acted_in(actor_id(foreign), movie_id(foreign))

---

 If you roll 5 standard six-sided dice, what's the probability that you get at least three 2s? 

>	(C_5^3 * 5^2 + C_5^4 * 5 + 1) / 6^5 = 23/648

<br>

>	1 - 5^5 / 6^5 - C_5^1 * 5^4 / 6^5 - C_5^2 * 5^3 / 6^5 = 23/648

---

#### An Activity to Further Your Gambling Addiction

 Also: you are offered the following bet: we pay you $1000 if you roll at least three 2s but you have to pay LiveRamp $200 if you don't. Would you take the bet? Why or why not? 

>   The other answer is correct except that the dice can occur in multiple orders/permutation

>   *   probability of getting five 2s is: P1 = 5C5 * (1/6)^5
>   *   probability of getting four 2s is: P2 = 5C4 * (1/6)^4 * (5/6)
>   *   probability of getting three 2s is: P3 = 5C3 * (1/6)^3 * (5/6)^2

>   probability of getting at least three 2s = P1 + P2 + P3

---

 Your friend Matt tells you to close your eyes while he rolls two dice. He promises you that he'll leave the room if and only if both of the dice show the same number. When you open your eyes, he's still in the room. What's the probability that the two dice sum to 8? 

>	P = Pr(Sum is 8 and he is in the room) / Pr(He is in the room) = 4/36 / (36 - 6)/36 = 2/15

---

*	 Coin Change (leetcode) 

```cpp
// Time:  O(n * k), n is the number of coins, k is the amount of money
// Space: O(k)

// dynamic programming
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int Max = amount + 1;
        vector<int> dp(amount + 1, Max);
        dp[0] = 0;
        for (int i = 1; i <= amount; ++i) {
            for (int j = 0; j < coins.size(); ++j) {
                if (coins[j] <= i)
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
```

*	 word ladder II (leetcode) 

---

#### why liveramp

>	What excites me about working at LiveRamp is that I can get the chance to work on distributed systems and practical data infrastructure problems and I can learn from the top engineers in this industry, working with a bunch of brilliant engineers. I truely believe that it improves and inspires people to get better and work harder to work with greate people in a team. And LiveRamp is exactly the brilliant and energitc team that motivates people in it to reach their best.

<br>

>	In order to avoid cliche that everyone uses to present their passion, I prefer to use a more elegant way to express my thought, that is - use ten bullet point to show my interests.
>
>	*	Data is one of the key aspects in business. To some extent it can be regarded as the future, and I want to be part of the future.
>	*	It is always interesting to extend my knowledge of computer science and math to other areas.
>	*	LiveRamp's work can be applied on so many fields that there must be many challenges and excitement to work on that.
>	*	The key ability to explore the world is building connections.
>	*	That's what LiveRamp do and what I want to get involved.
>	*	Though lots of people talking about Online to Offline, working on Offline to Online may also be vital to business success.
>	*	Most importantly, I can work on different things everyday as tomorrow will never be another today in LiveRamp.
>	*	I really love the creed Fewer Rules, More Responsibility. That's the creed that every company should follow.
>	*	Combining the tasks of data science, business and computer science, working in LiveRamp will surely be a heart-racing journey.
>	*	(bonus) I really love San Francisco!
>
>	Thanks for your time.

<br>

>	这个问题，或者说这类问题是蛮常见的，尤其是小公司特别重视这个。之前也有人问我简答题有没有模板，我想说没有，而且就算是有也不建议用。我觉得，这个问题，无论你是去面哪家公司，都是很重要的。说实话，写代码这个其实最后大家都不会差太多，无非是你的解法巧妙点，他的时间快一点，总之多做题一定会有帮助的。再不济也能写出常规算法，而且你想面试官面过那么多人，你是很难在这个部分别出心裁的。. 

>	再次重申，这个部分对小公司真的很重要！一定要特别重视！我是明年本科毕业，正在找全职，之前找实习期间大小公司都有面过。大公司比如FLAG那些真的就是纯拼代码，但是相反小公司特别重视behavior这种题目，记得我去面concur的时候，他家HR还专门发了一份这类题目的总结。
个人经验是，

>	1. 每个公司一定要真的去做research，不用多深但是一定要把握这个公司的特点。
>	2. 一定要努力把公司的特点和自己的特点结合起来，也就是为什么公司招你不找别人。
>	3. 一定一定要有热情，就是如果文字叙述就要go in details，如果口头交流一定要让对方感受到你是真的喜欢这个。我知道这点可能对很多男生来讲比较	难，我自己可能因为确实很容易对很多东西感兴趣，所以通常都是只要你给我一点时间，我都能把它说的让你觉得我就是很喜欢它，甚至说的你也很喜欢他（总被小伙伴说应该去做marketing，总是说的人感兴趣却又不反感）；当然这个可能不是很容易做到，但是我觉得练一练吧，如果你想要去小公司的话~~~不过，如果一个公司你在努力都无法对它充满热情，那就放弃吧，你去了也会不开心的~

>	然后来举几个例子说说我一般怎么来发掘我对公司喜好和了解，这个部分不一定要很多条，但是一定要有重点有特点：

>	1. 准备两三个大公司和小公司工作的好处，这里的大小并非单纯指公司规模，而是还要看码农类的规模；比如有些公司历史久远，但是软件类才刚起步。所以大公司和小公司工作的好处都会用得到。比如，可以看看他有没有分公司或者跨国公司，这样子可以说到机会多，或者接收到多元文化；如果是小公司，我可能会说，新生活里，让我觉得很有动力工作
>	2. 查一查口碑，比如“近年”获得什么荣誉称号，这个一定很好找到，谁不把自己的名声摆出来呀是吧~然后挑重点，可以说哇塞。居然XXX都跟你有合作啊！好厉害呀！吓到宝宝了呢！然后我就好想融入这么牛逼的公司呀~~~
>	3. 每一个公司都会有自己的idea，找到他们最特殊的，一般都会带个引号或者单门有个网页，然后就说“嗯你这个点真的很吸引我，虽然做这方面项目的公司很多，但我认为你这个比其他人怎么怎么好，怎么怎么切实际”
>	4. 结合个人特点，这个特别重要，我觉得也可以作为吸引人的亮点，这个就是看你能怎么样发觉自己啦~~~我来举几个例子，都是亲身经验，这个也要注意不要刻意造假一面说不出细节
>		1. 面Concur的时候，这是一个做Business Travel 和 Reimbursement的公司，我就会说“我曾经在旅行社工作过三个月，也接触过很多公务团的组团，以及带领过公务团，所以比较了解这类注资方和旅行者分别的需求”
>		2. 面LiveRamp之类的公司，因为都是Big Data嘛，我就会结合我的专业说，我之前是“Applied Math”的“Statistic”分支，最近刚转到"Scientific Computation & Numerical Analysis"分支，就会很好帖
>		3. 面Epic的时候，因为和医疗有关，我是double major，另一个就是biochemistry制药相关，所以也是一个点.

>	当然，我的例子可能不适用于你，但是只是想说，一定要发掘自己最独特的，这样子会对这类问题很有帮助

<br>

>   I see the big data area so promising that everyone should be connected in some way through any form of data. As a Computer Science major undergraduate student, I had solid foundations on computer systems programming, but far more than enough skills on data science. So I took Machine Learning and Data Science courses online during this Summer, and had an overview of what we can do with a huge amount of data, which really excite me to engage in this area. Since LiveRamp is the leader in data connectivity, which perfectly matches my goal, I really want to join and discover more in the industry, hone my skills with the help of those excellent engineers, and fianlly contribute myself to this area.

