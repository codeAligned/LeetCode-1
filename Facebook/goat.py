# Goat Latin
# 1. English 转化为 Goat Latin Language。
# 规则：
#         1. vowel 开头的单词，要在单词后面加 ma
#         2. consonant 开头的单词，把这个 consonant 移动到单词末尾。
#         3. 所有的单词末尾都要加上一个 String，这个 String 在第一个单词后面是 a，第二个单词后面是 aa，以此类推。
#         ex：
#                 I speak Goat Latin -> Imaa peaksaa oatGaaa atinLaaaa

s = input()
word_list = s.strip().split()
vowel = {'a', 'e', 'i', 'o', 'u'}
for i, word in enumerate(word_list):
	if word[0].lower() in vowel:
		word_list[i] = word + 'ma'
	else:
		word_list[i] = word[1:] + word[0]
	word_list[i] +=  'a' * (i + 1)

print(' '.join(word_list))