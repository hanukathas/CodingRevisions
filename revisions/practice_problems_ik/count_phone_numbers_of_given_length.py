def count_phone_numbers_of_given_length(start_digit, phone_number_length):
    moves = {
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        4: (3, 9, 0),
        5: tuple(),  # 5 has no valid moves
        6: (1, 7, 0),
        7: (2, 6),
        8: (1, 3),
        9: (2, 4),
        0: (4, 6)
    }

    # Initialize dp array
    # dp[l][d] represents count of numbers of length l starting from digit d
    dp = [[0] * 10 for _ in range(phone_number_length + 1)]
    dp[1][start_digit] = 1

    for l in range(2, phone_number_length + 1):
        for d in range(10):
            # For each digit, sum up the counts from all possible previous digits
            for prev_digit in range(10):
                if d in moves[prev_digit]:
                    dp[l][d] += dp[l - 1][prev_digit]

        print(dp)

        # Return total count for required length
    return sum(dp[phone_number_length])




if __name__ == '__main__':
    print(count_phone_numbers_of_given_length(1,3))