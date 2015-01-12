import sys
def main():
    #g = sys.stdin
    g = open('test')
    totalTest = int(g.readline())
    numbers = set('0123456789')
    for _ in range(totalTest):
        sizes = g.readline().split()
        n = int(sizes[0])
        m = int(sizes[1])

        result = 'YES'
        pre_line = g.readline().strip()
        if  pre_line[0] not in numbers or pre_line != pre_line[0] * m:
            result = 'NO'
        for lines in range(1, n):
            curr_line = g.readline().strip()
            if curr_line[0] not in numbers or \
                curr_line != curr_line[0] * m or \
                curr_line[0] == pre_line[0]:
                result = 'NO'
            pre_line = curr_line
        print result

if __name__ == '__main__':
    main()