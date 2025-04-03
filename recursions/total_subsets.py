test1 = 0
test2 = 1
test3 = 5

def subsets(n):
    if n == 0:
        return 1
    else:
        return 2 * subsets(n-1)

def subsets_revision(n):
    if n == 0:
        return 1
    else:
        return 2 * subsets_revision(n - 1)

if __name__ == '__main__':
    print(subsets_revision(test1))
    print(subsets_revision(test2))
    print(subsets_revision(test3))