test1 = 0
test2 = 1
test3 = 5

def subsets(n):
    if n == 0:
        return 1
    else:
        return 2 * subsets(n-1)

if __name__ == '__main__':
    print(subsets(test1))
    print(subsets(test2))
    print(subsets(test3))