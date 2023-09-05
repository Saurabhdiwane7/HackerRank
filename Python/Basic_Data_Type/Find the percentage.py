# Q = https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    query_scores = student_marks.get(query_name, [])
    average_marks = sum(query_scores) / len(query_scores)

    print("{:.2f}".format(average_marks))
