def sentence_screen_fitting(sentence: list, m: int, n: int):
    s = ' '.join(sentence) + ' '
    total_chars = n - (n % len(s))
    print(total_chars, len(s))
    count_line = total_chars // len(s)
    return m * count_line

if __name__ == '__main__':
    print(sentence_screen_fitting(["how", "are", "you"], 5, 5))