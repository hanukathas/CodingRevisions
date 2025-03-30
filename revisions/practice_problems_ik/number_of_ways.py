from arrays.moving_average_window import moving_average_window


def number_of_ways(n, k):
    mod = int(1e9) + 7
    same = [0] * (n+1)
    diff = [0] * (n + 1)
    if n == 0:
        return 0
    if n == 1:
        return k
    same[0] = 0
    same[1] = 1

    diff[0] = 0
    diff[1] = 0

    same[2] = k
    diff[2] = k*(k-1)

    for fence in range(3,n+1):
        same[fence] = diff[fence-1] * 1 # only one way to choose the same color as the prev fence color
        diff[fence] = (((same[fence-1] % mod + diff[fence-1] % mod) % mod) * (k-1)) % mod

    return (same[n] % mod + diff[n] % mod) % mod

def number_of_ways_revision(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    else:
        same = [0] * (n+1)
        diff = [0] * (n+1)

        same[2] = k * 1# kC1 for the 2nd one
        diff[2] = k * (k-1) #k for the first one and k-1 options for the second

        for i in range(3, n+1):
            same[i] = diff[i-1] * 1
            diff[i] = (same[i-1] + diff[i-1]) * (k-1)

        return same[n] + diff[n]


if __name__ == '__main__':
    print(number_of_ways(3,2))
    print(number_of_ways_revision(3, 2))



