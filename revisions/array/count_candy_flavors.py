from collections import Counter


def count_candy_flavors(candies: list, k: int):
    """
    https://www.notion.so/karthikrajagopalan/Chime-1cae4932e4f180329656d5d2a5af0532?pvs=4#1f3e4932e4f1809eb8d2f842082e406c
    :param candies:
    :param k:
    :return:
    """
    n = len(candies)
    total_freq = Counter(candies)
    window = candies[:k]
    window_freq = Counter(window)
    # after initial division
    for flavor, candy in window_freq.items():
        total_freq[flavor] -= candy
    # max unique flavors
    max_unique = sum(1 for count in total_freq.values() if count > 0)

    for i in range(1, n-k+1):
        # remove left most element (give the candy)
        flavor = candies[i - 1]
        window_freq[flavor] -= 1
        total_freq[flavor] += 1

        # add kth (add a candy)
        flavor = candies[i + k - 1]
        window_freq[flavor] += 1
        total_freq[flavor] -= 1

        unique = sum(1 for count in total_freq.values() if count > 0)
        max_unique = max(max_unique, unique)
    return max_unique

if __name__ == '__main__':
    candies = [1, 2, 2, 3, 4, 3]
    k = 3
    print(count_candy_flavors(candies, k))

    candies = [2, 2, 2, 2, 3, 3]
    k = 2
    print(count_candy_flavors(candies, k))

    candies = [2, 4, 5]
    k = 0
    print(count_candy_flavors(candies, k))