import sys

def split():
    try:
        n = int(input())
        if n <= 0 or n > 100:
            raise ValueError
        num = map(int,sys.stdin.readline().split())
    except:
        sys.stderr.write("Input wrong number")
        raise ValueError
    return num

def sum_num(num):
    try:
        if num == 0:
            return
        buff  = sum(map(lambda x: x * x,filter(lambda x:x > 0,split())))
        print(buff)
        return sum_num(num-1)
    except:
        sys.stderr.write("Input wrong number")


if __name__ == '__main__':
    N = int(input('Input:\n'))
    if N <= 0 or N > 100:
        sys.stderr.write("Input wrong number,number should in 1 <= N <= 100\n")
        sys.exit()
    sum_num(N)
