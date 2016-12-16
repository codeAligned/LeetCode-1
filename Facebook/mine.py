# minesweeper
# Given a height and a width and number of mines, return a minesweeper.
# field with mines in random positions
# input: 2, 3, 3
# return:
# -------------
# -   -   - X -
# -------------
# - X - X -   -
# -------------

import random

row, col, mines = map(int, input().strip().split())
ms = [[0] * col for _ in range(row)]
rand_set = set()
for _ in range(mines):
	while True:
		rand = random.randrange(0, row*col)
		if rand not in rand_set:
			break

	r = rand // col
	c = rand % col
	ms[r][c] = 1
	print(rand)
	rand_set.add(rand)

print(ms)
