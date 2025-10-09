# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

t = int(input())

def count_factors_of_2(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(count_factors_of_2(x) for x in a)
    if total >= n:
        print(0)
    else:
        indices = [0] * (n + 1)
        for i in range(1, n + 1):
            indices[i] = count_factors_of_2(i)
        indices.sort(reverse=True)
        count = 0
        for val in indices:
            total += val
            count += 1
            if total >= n:
                break
        if total >= n:
            print(count)
        else:
            print(-1)

