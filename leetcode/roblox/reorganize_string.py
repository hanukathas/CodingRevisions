import heapq
from collections import Counter

def re_organize_string(s: str):
    """
        we need to fulfill the requirement of arranging all the letters, high frequency letters has to get fulfilled in a way we balance all the letters
        we need to count the frequency of letters and order by it. something like a heap storage, that helps with ordering which is required in this case will
        be useful
        1. count frequency of each character
        2. build max heap, order descending
    :param s:
    :return:
    """
    letter_freq = Counter(s)

    max_heap = [(-freq, char) for char, freq in letter_freq.items()]
    # print(max_heap)

    heapq.heapify(max_heap)
    # print(max_heap)

    # alternate character spacing, so no two letters are same
    result = []
    while len(max_heap) >= 2:
        freq_1, char_1 = heapq.heappop(max_heap)
        freq_2, char_2 = heapq.heappop(max_heap)

        result.extend([char_1, char_2])

        if freq_1 + 1 < 0:
            heapq.heappush(max_heap,  (freq_1 +1, char_1))
        if freq_2 + 1 < 0:
            heapq.heappush(max_heap, (freq_2 + 1, char_2))

    if max_heap:
        freq_1, char_1 = heapq.heappop(max_heap)
        print(freq_1, char_1)
        if freq_1 < -1:
            return ""
        result.extend([char_1])

    return  "".join(result)


if __name__ == '__main__':
    # print(re_organize_string("aaab"))
    # print(re_organize_string("aaabcd"))
    # print(re_organize_string("baaba"))
    # print(re_organize_string("aaabbccdddd"))

    set1 = {"ab", "abc", "ddd", "bc", "abc hello"}
    set2 = {"ab", "abc"}

    print(list(set1.symmetric_difference(set2)))