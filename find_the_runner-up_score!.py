if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    uniques = []
    for i in range(n):
        if arr[i] not in uniques:
            uniques.append(arr[i])
    maximum = float('-inf')
    max_index = 0
    for i in range(len(uniques)):
        if uniques[i] >= maximum:
            maximum = uniques[i]
            max_index = i
    uniques.pop(max_index)
    print(max(uniques))
        
