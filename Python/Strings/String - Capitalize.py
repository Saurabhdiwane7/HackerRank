# Q -https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true


def solve(s):
    text = s.split()
    new_text = [n.capitalize() for n in text]
    capitalized_text = " ".join(new_text)
    return capitalized_text

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()