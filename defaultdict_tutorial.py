# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
A = defaultdict(list)
B = []
for i in range(n):
    A[(input())].append(i + 1)
for i in range(m):
    B.append(input())

b_pos = defaultdict(list)
for word in B:
    if word in A:
        for item in A[word]:
            print(item, end=" ")
        print()
    else:
        print(-1)
    
