# Enter your code here. Read input from STDIN. Print output to STDOUT
n_eng = int(input())
eng = set(map(int, input().split()))
n_fr = int(input())
fr = set(map(int, input().split()))

unique = eng.difference(fr)
print(len(unique))
