def num_binary_search_trees(n):
    # dp[i] represents number of unique BSTs with i nodes
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i - j]
    return dp[n]

if __name__ == '__main__':
    # Example usage
    n = 3
    result = num_binary_search_trees(n)
    print(f"Number of unique BSTs with {n} nodes:", result)
