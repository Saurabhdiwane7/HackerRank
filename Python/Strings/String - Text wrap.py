#Q =https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true


import textwrap


def wrap(string, max_width):
    wrapped_text = "\n".join([string[i:i + max_width] for i in range(0, len(string), max_width)])
    return wrapped_text


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)