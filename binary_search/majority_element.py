from collections import Counter


def majority_element(nums: list, target: int):
    """
    if the frequency of target > size / 2 then return that element
    :param nums:
    :param target:
    :return:
    """
    nums_counter = Counter(nums)
    print(nums_counter)
    return nums_counter[target] > len(nums) // 2

if __name__ == '__main__':
    print(majority_element([2,4,5,5,5,5,5,6,6], 5))
    print(majority_element([10, 100, 101, 101], 101))
