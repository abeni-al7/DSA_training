# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())

match = "codeforces"
for _ in range(t):
    s = input()
    count = 0
    for i in range(10):
        if s[i] != match[i]:
            count += 1
    print(count)