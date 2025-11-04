# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

t = int(input())
for _ in range(t):
    word = input()
    first = ord(word[0]) - ord("a")
    second = ord(word[1]) - ord("a")
    index = (first * 25)
    if second > first:
        index += second
    else:
        index += second + 1
    print(index)