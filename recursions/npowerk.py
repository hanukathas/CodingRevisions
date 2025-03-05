test1 = [0,1]
test2 = [1,5]
test3 = [5,4]
test4 = [-3,-3]
test5 = [-3,4]

def npowerk(n,k):
    if k == 0:
        return 1
    else:

        return n * npowerk(n, k-1)

if __name__ == '__main__':
    print(npowerk(test5[0], test5[1]))
    print(npowerk(test3[0], test3[1]))
    print(npowerk(test2[0], test2[1]))
    print(npowerk(test1[0], test1[1]))