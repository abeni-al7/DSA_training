# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
ans = True
for i in range(n):
    other = set(map(int, input().split()))
    if len(other.difference(A)) == 0 and len(A.difference(other)) > 0:
        continue
    else:
        ans = False
        print(ans)
        break
if ans:
    print(ans)
