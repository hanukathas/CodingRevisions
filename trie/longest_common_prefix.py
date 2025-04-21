def longest_common_prefix(words: list):
    """
    start with the length of the first word
    and then for every word, calculate the min length of the two words
    run the loop for the length of the smaller word
    if there is a mismatch, that's length measured - 1 is the length of the common prefix
    :param words:
    :return:
    """
    common_prefix_len = len(words[0])

    for i in range(1, len(words)):

        common_prefix_len = min(common_prefix_len, len(words[i]))
        for j in range(common_prefix_len):
            if words[i][j] != words[0][j]:
                common_prefix_len = j
                break
    return words[0][:common_prefix_len]

if __name__ == '__main__':
    words = ["flower", "flow", "flight"]
    print(longest_common_prefix(words))








