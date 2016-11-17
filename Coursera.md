### Coursera

#### My Online Assesment

*	Grid Game
	*	each step add 1 from (1, 1) to (a, b)
	*	count #(greatest number)
```python3
# find the rules
def  countX(steps):
    min_a = float("inf")
    min_b = float("inf")
    for step in steps:
        a, b = map(int, step.split())
        min_a = min(a, min_a)
        min_b = min(b, min_b)
    return min_a * min_b
```

*	Longest Subarray
	*	given sum, array
	*	find the longest subarray whose sum is less than or equal to given
```python3
# dp backtrack
def  maxLength(a, k):
    max_len = 0
    size_a = len(a)
    sum = 0
    cur_len = 0
    for i in range(size_a):
        if sum + a[i] <= k:
            sum += a[i]
            cur_len += 1            
            max_len = max(max_len, cur_len)
        else:
            sum -= a[i - cur_len]
            cur_len -= 1
            while sum + a[i] > k:
                sum = sum - a[i - cur_len]
                cur_len -= 1
            sum += a[i]
            cur_len += 1
            max_len = max(max_len, cur_len)
    return max_len
```