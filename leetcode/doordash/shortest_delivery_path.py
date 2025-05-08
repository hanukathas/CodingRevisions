from collections import defaultdict, deque


def shortest_delivery_path(start: str, destination: str, validlocations: list):
    if destination not in validlocations:
        return 0
    if start not in validlocations:
        validlocations.append(start)

    patterns = defaultdict(list)
    n = len(start)

    for location in validlocations:
        for i in range(n):
            pattern = location[:i] + '*' + location[i+1:]
            patterns[pattern].append(location)

    visted = set()
    queue = deque()
    queue.append((start, 1))

    while queue:
        print(queue)
        current, count = queue.popleft()
        visted.add(current)
        for i in range(n):
            pattern = current[:i] + "*" + current[i+1:]
            for location in patterns[pattern]:
                if location == destination:
                    return count
                if location != destination:
                    queue.append((location, count + 1))
    return 0


def word_ladder(start: str, end: str, word_list: set) -> list:
    if end not in word_list or start not in word_list:
        return []

        # Get all possible characters from the dictionary words
    all_chars = set(''.join(word_list))

    queue = deque([[start]])

    seen = {start}

    while queue:
        path = queue.popleft()
        word = path[-1]

        if word == end:
            return path

        # Try changing each position to each possible character
        for i in range(len(word)):
            for c in all_chars:
                next_word = word[:i] + c + word[i + 1:]
                if next_word in word_list and next_word not in seen:
                    queue.append(path + [next_word])
                    seen.add(next_word)

    return []  # No valid path found


if __name__ == '__main__':
    # print(shortest_delivery_path('abc123', 'bbc923', ['abc123', 'bbc923', 'abc923']))

    print(word_ladder('abc123', 'bbc923', {'abc123', 'bbc923', 'abc923'}))
    print(word_ladder('cat', 'dog', {'cat', 'cag', 'cog', 'dog'}))

