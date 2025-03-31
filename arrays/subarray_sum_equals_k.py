def subarray_sum_equals_k(arr: list, k: int) -> int:
    prefix_sum = 0
    equals_k = 0
    hmap = {}

    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum - k in hmap.keys():
            equals_k += 1
        if prefix_sum in hmap.keys():
            hmap[prefix_sum] += 1
        else:
            hmap[prefix_sum] = 0

    print(hmap.items(), prefix_sum, equals_k)

def count_subarrays_with_sum_k(arr, k):
    # Dictionary to store cumulative sum frequencies
    sum_freq = {0: 1}  # Initialize with 0 sum having frequency 1
    curr_sum = 0
    count = 0

    for num in arr:
        # Add current number to running sum
        curr_sum += num

        # Check if (curr_sum - k) exists in dictionary
        # If it does, add its frequency to count
        if curr_sum - k in sum_freq:
            count += sum_freq[curr_sum - k]

        # Update frequency of current sum in dictionary
        sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1

    print(count)

def count_subarrays_with_sum_k_revision(arr, k):
    hmap = {0: 1}
    prefix_sum = 0
    total = 0
    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum - k in hmap:
            total += hmap[prefix_sum - k]
        if prefix_sum in hmap:
            hmap[prefix_sum] += 1
        else:
            hmap[prefix_sum] = 1
    return total



if __name__ == '__main__':
    subarray_sum_equals_k([1, 2, 3, -3, 1, 1, 1, 4], 3)
    count_subarrays_with_sum_k([1, 2, 3, -3, 1, 1, 1, 4], 3)
    print(count_subarrays_with_sum_k_revision([1, 2, 3, -3, 1, 1, 1, 4], 3))


