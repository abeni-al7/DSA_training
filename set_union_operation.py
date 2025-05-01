# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(map(int, input().split()))
b = int(input())
fr = set(map(int, input().split()))

comb = eng.union(fr)
print(len(comb))
