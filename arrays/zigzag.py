def zigzag(arr: list):
    for i in range(1, len(arr)):
        if (i-1) % 2 == 0:
            if arr[i-1] >= arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
        elif (i-1) % 2 == 1:
            if arr[i-1] <= arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

    return arr

def zigzag_revision(arr: list):
    for i in range(1, len(arr)):
        if i % 2 == 0:
            if arr[i-1] <= arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
        else:
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]

    return arr



def longestRepeatedSubstring(s: str) -> str:
    n = len(s)
    # Create a list of all possible substrings with their starting positions
    suffixes = [(s[i:], i) for i in range(n)]

    # Sort suffixes lexicographically
    suffixes.sort()

    result = ""
    # Compare adjacent suffixes to find longest common prefix
    for i in range(n - 1):
        curr_str = suffixes[i][0]
        next_str = suffixes[i + 1][0]
        j = 0

        # Find common prefix between adjacent strings
        while j < len(curr_str) and j < len(next_str) and curr_str[j] == next_str[j]:
            j += 1

        # Check if this common prefix is from different positions
        if j > 0 and abs(suffixes[i][1] - suffixes[i + 1][1]) != j:
            common = curr_str[:j]
            if len(common) > len(result):
                result = common

    return result


if __name__ == '__main__':
    print(zigzag_revision([10,9,8,7,6,5,4,3,2,1]))

