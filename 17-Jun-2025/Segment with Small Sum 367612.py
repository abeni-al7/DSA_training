# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    s = int(data[1])
    a = list(map(int, data[2:2+n]))

    left = 0
    current_sum = 0
    max_len = 0

    for right in range(n):
        current_sum += a[right]
        while current_sum > s:
            current_sum -= a[left]
            left += 1
        max_len = max(max_len, right - left + 1)
        
    print(max_len)

if __name__ == "__main__":
    main()