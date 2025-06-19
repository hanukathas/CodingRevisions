def projects():
    # Read number of projects
    n = int(input())

    # Store projects as tuples of (start, end, reward)
    projects = []
    for _ in range(n):
        start, end, reward = map(int, input().split())
        projects.append((start, end, reward))

    # Sort projects by end time for dynamic programming
    projects.sort(key=lambda x: x[1])

    # dp[i] represents maximum profit achievable considering projects[0...i]
    dp = [0] * n

    # Helper function to find latest non-overlapping project before index i
    def binary_search(end_idx):
        # Find rightmost project that ends before current project starts
        target = projects[end_idx][0]  # Start time of current project
        left, right = 0, end_idx - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if projects[mid][1] < target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

    # Base case: first project
    dp[0] = projects[0][2]

    # Fill dp array
    for i in range(1, n):
        # Find latest non-overlapping project
        prev_project = binary_search(i)

        # Current project reward
        current_reward = projects[i][2]

        # Add previous non-overlapping project's profit if exists
        if prev_project != -1:
            current_reward += dp[prev_project]

        # Maximum of including current project or excluding it
        dp[i] = max(current_reward, dp[i - 1])

    # Print maximum profit possible
    print(dp[n - 1])


if __name__ == '__main__':
    projects()