# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
min_deque = deque()
max_deque = deque()
count = 0

for r in range(n):
    while min_deque and min_deque[-1] > a[r]:
        min_deque.pop()

    while max_deque and max_deque[-1] < a[r]:
        max_deque.pop()

    min_deque.append(a[r])
    max_deque.append(a[r])
    while max_deque[0] - min_deque[0] > k:
        if min_deque[0] == a[l]:
            min_deque.popleft()
        if max_deque[0] == a[l]:
            max_deque.popleft()
        l += 1
    count += r - l + 1
    
print(count)