def weird_algo(n: int):
    slack = []
    while  n != 1:
        if n % 2 == 0:
            n = n // 2
            slack.append(n)
        else:
            n = 3 * n + 1
            slack.append(n)
    print(slack)
    return n


if __name__ == '__main__':
    print(weird_algo(125))

