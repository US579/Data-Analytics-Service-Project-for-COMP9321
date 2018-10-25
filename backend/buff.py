import sys

def first_num():
    N = int(input())
    if N <= 0 or N > 100:
        sys.stderr.write("Input wrong number,number should in 1 <= N <= 100\n")
        sys.exit()
    return N

def split():
    try:
        n = int(input())
        if n <= 0 or n > 100:
            raise ValueError
        num = map(int,sys.stdin.readline().split())

    except:
        sys.sterr.write("Input wrong number")
        raise ValueError
    return num

def sum_num(num):
    if num <=0:
        sys.stderr.write("No input\n")
    buff  = sum(map(lambda x:x*x,filter(lambda x:x>0,split())))
    print(buff)
    return sum_num(num-1)

num = split()
sum_num(num)
