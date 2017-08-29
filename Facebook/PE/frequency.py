# word frequency

import heapq
from collections import Counter

# s = input()
# out = "".join(c for c in s if c not in {'!', ',', '.', ':'})

text = ''
with open('text.txt') as f:
	for line in f:
		text += "".join(c for c in line if c not in {'!', ',', '.', ':', '?'})

word_list = text.strip().split()
cnt = Counter(word_list)

print(cnt.most_common(10))

print(heapq.nlargest(10, cnt.items(), key=lambda x: x[1]))
