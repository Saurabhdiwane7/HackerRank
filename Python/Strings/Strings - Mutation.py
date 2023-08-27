# Q =https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def mutate_string(string, position, character):
    a = str(string)
    l = list(string)
    l[position] = "k"
    a = "".join(l)
    return a


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)