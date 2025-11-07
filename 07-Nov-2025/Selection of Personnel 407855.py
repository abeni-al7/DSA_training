# Problem: Selection of Personnel - https://codeforces.com/problemset/problem/630/F

n = int(input())

fact = [0] * (n + 1)
fact[0] = fact[1] = 1

for i in range(2, n + 1):
    fact[i] = i * fact[i - 1]

group5 = (fact[n]) // (fact[n - 5] * fact[5])
group6 = (fact[n]) // (fact[n - 6] * fact[6])
group7 = (fact[n]) // (fact[n - 7] * fact[7])

print(group5 + group6 + group7)
