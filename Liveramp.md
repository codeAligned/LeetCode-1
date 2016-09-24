### Liveramp
*	Your friend Matt tells you to close your eyes while he rolls two dice. He promises you that he'll leave the room if and only if both of the dice show the same number. When you open your eyes, he's still in the room. What's the probability that the two dice sum to 8?
*	why liveramp
---
*	city (hashmap, bfs)
*	有M个城市，总共有M-1个边，有一个城市是首都，求从首都距离1，2，3，...，M-1的距离的城市个数。反正，很直观，acyclic directed graph的bfs。输入一个vector：i.e. T[0] = 9 (表示9结点指向的下一个结点是0结点), T[1] = 1 (如果T和i相等，那么i就是首都)，T[2] = 4，T[3] = 9，T[4] = 0，T[5] = 4，T[6] = 8，T[7] = 9，T[8] = 0，T[9] = 1
输出结果：[1, 3, 2, 3, 0, 0, 0, 0, 0]
(反正思路真的很直观，拿个vector<vector<int>>重建图，再用个queue逐层遍历就是了)
---

*	算法题：青蛙过河。

输入一个Array, X，D，最早可以跳过X的时刻。

1 有只青蛙要过河，起始位置position 0，一路跳到 X，每次跳得距离 在1 ~ D，一秒可以跳很多次的样子只要有叶子可以停。。。
2 每秒都会落下一片叶子，青蛙可以停在上面（叶子不会消失）
3 给了一个Array, Array[k] 表示，k秒落下叶子的位置

int solution(vector<int> &A, int X, int D) {
    if(X<=D) return 0;
    vector<int> res(X+1,100000);
    map<int,int> leaf;
    res[0]=0;
    leaf[0]=0;
    leaf[X]=0;
    for(int i=0;i<A.size();++i){
        if(leaf.count(A)) continue;
        else leaf[A]=i;
    }
    for(int i=1;i<=X;++i){
        if(!leaf.count(i)) continue;
        if(i<=D){
            if(leaf.count(i)) res=leaf;. 1point3acres.com/bbs
        }. 鐣欏鐢宠璁哄潧-涓€浜╀笁鍒嗗湴
        else{. 1point 3acres 璁哄潧
            for(int k=D;k>0;--k){
                if(leaf<=res[i-k]) res=min(res,res[i-k]);
                else res=min(res,leaf);. 1point 3acres 璁哄潧
            } 
        }
    } 
    return res[X];
}
---
*	一个sequence，里面都是整数，求最长的subsequence的长度，使得这个subsquence的最大值和最小值相差不超过1. 比如[1,3,2,2,5,2,3,7]最长的subsequence是[3,2,2,2,3],所以应该返回5. 其实挺简单的一道题，开始我以为subsequence要求连续，就用dp做，run了一下结果不对，发现subsequence可以是不连续的，这样的话只需要用一个hashtable统计一下各个整数的个数，所以最长的长度应该就是count[k]+count[k+1]的最大值，k是这个sequence里的某一个数，count[k]是它出现的次数。另外一个思路就是排序，这样空间复杂度小点，但是时间复杂度要高一些。
*	一个图，节点表示城市，有M个节点和M-1条边，所以是没有环的，用一个array表示这个图，比如T[x]=y的话那么节点x就和y相连，如果T[x]=x就说明x是首都。现在要分别求出到首都距离为1，2，3...M-1的节点数。
这题我用一个hashmap重新建了一个图，这样方便查找所有相邻的节点，而不用每次查找整个array。然后用bfs来求每个距离上的节点数。
---

*	MDB 2.0 - Movie DB Table Structure
Your best friend Betty thinks IMDB is too complicated and challenges you to create a simple movie web site. One page will display movies (with movie name, date it was released, and list of actors). Click on an actor and you're taken to the actor page (with actor name, birthday, bio, and list of movies actor has been in). Please outline the relational table structure of the database for this.   View Answers (3). visit 1point3acres.com for more.
*	Six Degrees of Turkey Bacon
You've always been intrigued with the Six Degrees of Kevin Bacon game. Let's say if two actors have been in the same movie we call them 'friends' and if two actors have not been in the same movie, we say they are not 'friends'. Now choose any two actors at random -- we want to calculate the number of degrees of separation and the path between them. How do you go about this problem?
*	Discuss your algorithm ideas. For each algorithm talk about the tradeoffs.
*	Choose which method you think is best for solving this problem and describe how it works. You may also want to talk about what data structures you would use to implement it.   View Answer. From 1point 3acres bbs
*	The Max
Bubble sort is O(n) at best, O(n^2) at worst, and its memory usage is O(1) . Merge sort is always O(n log n), but its memory usage is O(n). Explain which algorithm you would use to implement a function that takes an array of integers and returns the max integer in the collection, assuming that the length of the array is less than 1000. What if the array length is greater than 1000?   View Answers (2)
*	An Activity to Further Your Gambling Addiction. visit 1point3acres.com for more.
If you roll 5 standard six-sided dice, what's the probability that you get at least three 2s?
Also: you are offered the following bet: we pay you $1000 if you roll at least three 2s but you have to pay LiveRamp $200 if you don't. Would you take the bet? Why or why not?   View Answers (2)
*	Why LiveRamp?
We’re excited that you’re interested in a position here at LiveRamp. How did you hear about us and why are you interested in working at LiveRamp in particular? What about LiveRamp excites you? Please limit yourself to 1-2 paragraphs.   Answer Question
---
*	Bubble sort is O(n) at best, O(n^2) at worst, and its memory usage is O(1) . Merge sort is always O(n log n), but its memory usage is O(n). Explain which algorithm you would use to implement a function that takes an array of integers and returns the max integer in the collection, assuming that the length of the array is less than 1000. What if the array length is greater than 1000?
. From 1point 3acres bbs
*	You've always been intrigued with the Six Degrees of Kevin Bacon game. Now, let's say if two actors have been in the same movie we call them 'friends' and if two actors have not been in the same movie, we say they are not 'friends'. Now choose any two actors at random -- we want to calculate the number of degrees of separation and the path between them. How do you go about this problem? Discuss ideas, trade-offs, algorithm ideas, and more.
*	Your best friend Betty thinks IMDB is too complicated and challenges you to create a simple movie web site. One page will display movies (with movie name, date it was released, and list of actors). Click on an actor and you're taken to the actor page (with actor name, birthday, bio, and list of movies actor has been in). Please outline the relational table structure of the database for this..
create table Movie(Name varchchar, Date date, primary key ID identifying);
create table Actor (Name varchar, birtday date, bio varchar, primary key ID identifying);
create table MovieActor(MovieID integer references Movie, ActorID integer references Actor ) Primary key (MovieID , ActorID);
*	If you roll 5 standard six-sided dice, what's the probability that you get at least three 2s?
---
1. why LiveRamp excites you这个问题，或者说这类问题是蛮常见的，尤其是小公司特别重视这个。之前也有人问我简答题有没有模板，我想说没有，而且就算是有也不建议用。我觉得，这个问题，无论你是去面哪家公司，都是很重要的。说实话，写代码这个其实最后大家都不会差太多，无非是你的解法巧妙点，他的时间快一点，总之多做题一定会有帮助的。再不济也能写出常规算法，而且你想面试官面过那么多人，你是很难在这个部分别出心裁的。. 
再次重申，这个部分对小公司真的很重要！一定要特别重视！我是明年本科毕业，正在找全职，之前找实习期间大小公司都有面过。大公司比如FLAG那些真的就是纯拼代码，但是相反小公司特别重视behavior这种题目，记得我去面concur的时候，他家HR还专门发了一份这类题目的总结。
个人经验是，. 鐣欏鐢宠璁哄潧-涓€浜╀笁鍒嗗湴
（1）每个公司一定要真的去做research，不用多深但是一定要把握这个公司的特点。
（2）一定要努力把公司的特点和自己的特点结合起来，也就是为什么公司招你不找别人。. 1point 3acres 璁哄潧
（3）一定一定要有热情，就是如果文字叙述就要go in details，如果口头交流一定要让对方感受到你是真的喜欢这个。我知道这点可能对很多男生来讲比较难，我自己可能因为确实很容易对很多东西感兴趣，所以通常都是只要你给我一点时间，我都能把它说的让你觉得我就是很喜欢它，甚至说的你也很喜欢他（总被小伙伴说应该去做marketing，总是说的人感兴趣却又不反感）；当然这个可能不是很容易做到，但是我觉得练一练吧，如果你想要去小公司的话~~~不过，如果一个公司你在努力都无法对它充满热情，那就放弃吧，你去了也会不开心的~

然后来举几个例子说说我一般怎么来发掘我对公司喜好和了解，这个部分不一定要很多条，但是一定要有重点有特点：
（1）准备两三个大公司和小公司工作的好处，这里的大小并非单纯指公司规模，而是还要看码农类的规模；比如有些公司历史久远，但是软件类才刚起步。所以大公司和小公司工作的好处都会用得到。比如，可以看看他有没有分公司或者跨国公司，这样子可以说到机会多，或者接收到多元文化；如果是小公司，我可能会说，新生活里，让我觉得很有动力工作
（2）查一查口碑，比如“近年”获得什么荣誉称号，这个一定很好找到，谁不把自己的名声摆出来呀是吧~然后挑重点，可以说哇塞。居然XXX都跟你有合作啊！好厉害呀！吓到宝宝了呢！然后我就好想融入这么牛逼的公司呀~~~
（3）每一个公司都会有自己的idea，找到他们最特殊的，一般都会带个引号或者单门有个网页，然后就说“嗯你这个点真的很吸引我，虽然做这方面项目的公司很多，但我认为你这个比其他人怎么怎么好，怎么怎么切实际”
（4）结合个人特点，这个特别重要，我觉得也可以作为吸引人的亮点，这个就是看你能怎么样发觉自己啦~~~我来举几个例子，都是亲身经验，这个也要注意不要刻意造假一面说不出细节
【1】面Concur的时候，这是一个做Business Travel 和 Reimbursement的公司，我就会说“我曾经在旅行社工作过三个月，也接触过很多公务团的组团，以及带领过公务团，所以比较了解这类注资方和旅行者分别的需求”
【2】面LiveRamp之类的公司，因为都是Big Data嘛，我就会结合我的专业说，我之前是“Applied Math”的“Statistic”分支，最近刚转到"Scientific Computation & Numerical Analysis"分支，就会很好帖
【3】面Epic的时候，因为和医疗有关，我是double major，另一个就是biochemistry制药相关，所以也是一个点.
当然，我的例子可能不适用于你，但是只是想说，一定要发掘自己最独特的，这样子会对这类问题很有帮助

2. Six Degree
这个虽然我没有被面到，但还是想重点来说一说，我觉得这个题特别好；以我本科的角度来看，研究生都是能做到很多很厉害的项目，但其实面试的时候，除非那个人特别懂你做的这类东西，不然你们两个也很难说到细节；但是Six Degree作为一道图形基础题，实现的方式包含的最基础也最重要的算法，我觉得值得好好准备。不光是简单的有思路，我觉得如果有可能，建议自己写一下，一定会对图形题有很大的帮助。而且其实也不难的，我曾经做过这个的作业，就是周作业那种，很快就能写完。但是我们的作业要求只实现三个算法，后来我又自己写了其他，这里简单说一下：
DFS：这个主要问题就是如果选错的入口，就要一直走到底，可以考虑limited DFS，用stack实现
BFS：用queue，会缩短平均遍历长度，但是如果每个node的分支很多，会造成不必要的浪费
DIJKSTRA：这个是给每条边增加权重，实质和BFS一样
A*：这个可以帮助解决BFS的弊端，给每个点增加“正确率”的特性，缺点是需要了解计算正确率的function，但是本质还是DFS
Bi-Direc BFS/Dijk/A*：本质相同，都需要两个queue，两个HashSet，分别给左起点和右起点用
最后，再说一句，DFS比较容易记录正确的路径，而剩下几个如果想要track path则需要辅助方法以及precessor

3. 关于我做过的free response的第一题，怎么解释你的算法
这个没什么特别多说的，因为大家算法不同，但我觉得你如果写到白板上要注意以下几点. 
（1）有逻辑，进行分段或者标数字. 
（2）尽量不要说得太难太复杂，因为估计看你答案的都是HR
（3）运用方法标出重点，比如我最喜欢用的就是 find the *ONLY* node that .....
（4）对于解释算法，我觉得可以这样，用一段两三句话说整体思路，比如为什么用DP/DFS/...
然后两到三段解释几个重点的edge case，或者你代码中的难点，说白了就是如果你给这段代码做comment，那么就重点解释comment，因为其他部分你不说别人也能懂
最后用一段一两句话总结
---
*	Coin Change (leetcode)
*	word ladder II (leetcode)
---
1.青蛙过河。感谢地里大家分享的解法，这里提供一个自己的另一个思路吧。这道题最tricky的地方应该就是，原先落下的叶子够不到，但是在更新的过程中，突然又能够到了，怎么样有效更新当前的状态呢？我用了下几个变量/结构来保存/更新状态：

*一个hashset，暂且叫做reachable， 用于保存当前能够到达的所有position，空间复杂度是O(N + D)。更新过程是顺序增长，即1,2,3,4,5,6，不会出现1,2,5,6的情况（下面会解释），则一旦它的长度大于等于我们的距离X，则表示能够到达对岸。. more info on 1point3acres.com
*第二个hashset，暂且叫做unused，用于保存当前已经存在却无法够到的所有叶子，空间复杂度O(N)。
*一个边界，在此边界前的所有叶子都没有价值，或者说通过那些叶子不能帮助青蛙跳得更远，暂且叫做usefulBound。

（1）base case。根据我们上述的定义，（i）如果 reachable已经覆盖了X，我们返回当前时间；（ii）如果遍历了所有可用的叶子依然不能到达X，返回-1. 鐗涗汉浜戦泦,涓€浜╀笁鍒嗗湴
（2）更新过程，一共会有三种情况：
（i）case 1：如果叶子的位置在usefulBound之前，我们直接跳过。
（ii）case 2：如果叶子的位置不在reachable里，表示目前无法够到，我们把这个叶子存入unused里。
（iii）case 3：除去前两种情况，我们可以用当前的叶子更新我们的状态。假设当前时间是 i，叶子位置是 s，reachable的size是k（则表示1 - k都可达），青蛙踩在 s 上能够到达最远的地方则是 s + D，我们需要插入reachable的位置就只有 pos = [k + 1, s + D]。我们挨个插入保证了reachable的范围是无缝的，并且每个position最多插入一次。这时候我们需要再做另一件事，每当我们插入一个新的pos到reachable，我们检查pos是否存在unused里，如果存在，我们只需要把更新的范围从s + D延长到 pos +Ｄ。由于pos是单调递增的，我们保证了每个叶子最多只被检查了一次。
（3）更新结束后做两件事，（i）更新usefulBound = reachable.size() - D + 1，比如当前能覆盖1 - 6， D = 3，那新叶子至少必须在4及其以后才会有用。（2）判断reachable是否覆盖目的地X，如果覆盖，返回当前时间 i 。

复杂度：空间是O（N+D）不用多说，关于时间，由于input给的叶子array长度是N，则叶子数量不会超过N，时间也不超过N；对于reachable，最远的可达范围是最后一片叶子+最后一跳，所以是N + D，并且这些位置最多只会被插入一次；对于每次检查当前时间的叶子，三种情况都只做了常数次操作，而且每个叶子也仍然最多被插入unused这个set里一次，并且由于reachable递增的特性，每个unused里的叶子也最多只被check一次。总的下来时间复杂度就是O(N + D)，由于两者量级相同可以简化为O(N)。不知道分析有没有遗漏的地方。

2. 猴子过河。这道题其实换汤不换药，但是要注意两个地方：
（1）青蛙过河的初始位置是0，目的地位置是X；但是猴子过河初始是-1，到达的位置是河对岸，比如 [0,1,2,3,4,5]，则需要到达6才算过河，一共需要跳7步以上。
（2）青蛙过河的input是 时间--->出现叶子的位置，猴子过河里变成了  石头位置--->出现时间。我们需要做的只是预处理把猴子过河里的input 转置一下，就和青蛙过河的input完全一样了。值得一提的是，题目说同一时间只会有一块石头出现，省得我们再想太多。
关于复杂度的问题，就是因为（ii）的预处理，导致我们需要首先判断 “最长的时间 t”，也就是数组A中的max，然后开辟一个数组长度为 t + 1来保存  时间--->石头位置，这样问题又退化到青蛙过河。但是这时候的时间长度可能会比原始数组A要长，所以最后的时空复杂度要求是O(N + max(A))。

3. sequence，其实是求最大subset，这个set满足里面的数最大的数和最小的数相差不超过1，比如[3,1,2,2,3,4]，那么最长的是[3,2,2,3]，返回4。有两种思路：
（1）用hashmap统计每个数的重复次数，得到k个不同的数，然后one-by-one scan这k个数，对每个数，计算count[k-1] + count[k] 和 count[k] + count[k+1]的数量，然后更新maxLen。时空复杂度都是O(N)
（2）sort and count，其实实现的难度和（1）一样，甚至逻辑没有那么清晰，需要考虑清楚index和off-by-one的问题。常数的空间复杂度+O(nlogn)的时间

4. M cities，找出离capital距离为1,2,3....M-1的城市数量。很典型的BFS，需要的是先建立一个adjacent list，然后用queue做BFS，注意更新和使用queue的长度。

5. six-degree，这道题看地里的意思应该就是描述算法优缺点然后做选择了？比较好描述的是DFS, BFS, Dijkstra，然后Bi-direction DFS/BFS/Dijkstra吧，很惭愧没有仔细看过A*算法。

6. 选择题和behavior看我分享的第一个链接吧，那个大神描述的很详细了。

估计现在还是有不少和我一样当初太过自信导致如今毕业了仍然待业的筒子们，当初一步慢，步步慢啊。。。。不过没关系，大家一起努力坚持，一定会有好结果！
