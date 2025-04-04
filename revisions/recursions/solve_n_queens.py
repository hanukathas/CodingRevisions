def solve_n_queens(n):
    solution = []
    cols = set()
    posdiag = set()
    negdiag = set()
    queens = [-1] * n
    def backtrack(row):
        if row == n:
            print(queens)
            solution.append(["-" * col + "q" + "-" * (n- col - 1) for col in queens])
            return
        for col in range(n):
            if col not in cols and row - col not in negdiag and row + col not in posdiag:
                queens[row] = col
                cols.add(col)
                posdiag.add(row + col)
                negdiag.add(row - col)

                backtrack(row+1)

                cols.remove(col)
                posdiag.remove(row + col)
                negdiag.remove(row - col)
    backtrack(0)
    return solution
if __name__ == '__main__':
    n = 4
    print(solve_n_queens(n))
    solutions = solve_n_queens(n)
    print(f"Number of solutions for {n}-queens: {len(solutions)}")
    for solution in solutions:
        for row in solution:
            print(row)

