def removal_game():
    n = int(input())
    nums = list(map(int, input().split()))

    # dp[i][j] stores (first_player_score, second_player_score)
    # for the subarray nums[i:j+1]
    dp = [[(0, 0)] * n for _ in range(n)]

    # Initialize diagonal (single elements)
    for i in range(n):
        dp[i][i] = (nums[i], 0)

    # Fill dp array
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Take left element
            left_sum = nums[i] + dp[i + 1][j][1]
            # Take right element
            right_sum = nums[j] + dp[i][j - 1][1]

            # Choose maximum of left and right options
            if left_sum > right_sum:
                dp[i][j] = (left_sum, dp[i + 1][j][0])
            else:
                dp[i][j] = (right_sum, dp[i][j - 1][0])

    # Print first player's score
    print(dp[0][n - 1][0])


if __name__ == '__main__':
    removal_game()