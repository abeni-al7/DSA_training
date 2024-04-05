
def split_and_join(line):
    # write your code here
    sp = line.split(" ")
    con = "-".join(sp)
    return con

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
