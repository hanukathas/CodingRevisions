def cheapest_stops_flight(n: int, edges: list, src: int, dst: int, k: int):
    """
    https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
    fundas: directed graph and weights are positive
    :param n:
    :param edges:
    :param src:
    :param dst:
    :param k:
    :return:
    """
    dp = [[float('inf')] * (k+2) for _ in range(n)] # up to k+1 starting at 0, so k + 2
    dp[0][0] = 0

    for col in range(1, k+2):
        for row in range(n): # on a new iteration, set the previously calculated values
            dp[row][col] = dp[row][col-1]

        for (s, d, w) in edges: # for the given destination, calculate the min cost from source
            dp[d][col] = min(dp[s][col-1] + w, dp[d][col])

    return dp[dst][k+1] if dp[dst][k+1] != float('inf') else -1


if __name__ == '__main__':
    n = 4
    edges = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    print(cheapest_stops_flight(n, edges, src, dst, k))
