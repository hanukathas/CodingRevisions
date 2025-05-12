def check_for_word(word: str, board: [[]]):
    found = False
    for char in word:
        found = False
        for row in board:
            if char in row:
                row.pop(row.index(char))
                found = True
                break
    return found

if __name__ == '__main__':
    print(check_for_word("ABCCEDG", [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]))


