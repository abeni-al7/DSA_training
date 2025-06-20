# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
a = list(map(int, input().split()))

max_len = 0
current_sum = 0
left = 0
for right in range(n):
    current_sum += a[right]
    while current_sum > s:
        current_sum -= a[left]
        left += 1
    max_len = max(max_len, right - left + 1)
print(max_len)