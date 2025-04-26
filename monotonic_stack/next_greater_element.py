def next_greater_element(nums2: list, nums1: list):
    next_greater_element_stack = []
    greater_element = {}
    for i in range(len(nums2) -1, -1, -1):
        while next_greater_element_stack and next_greater_element_stack[-1] < nums2[i]:
            next_greater_element_stack.pop()
        if next_greater_element_stack:
            greater_element[nums2[i]] = next_greater_element_stack[-1]
        else:
            greater_element[nums2[i]] = -1
        next_greater_element_stack.append(nums2[i])

    # we want this only for nums1 which is a subset
    ans = []
    for i in range(len(nums1)):
        ans.append(greater_element[nums1[i]])

    return ans

def next_greater_element_r(nums2: list, nums1: list):
    nge_stack = []
    ans = []
    for i in range(len(nums2) -1, -1, -1):
        while nge_stack and nge_stack[-1][0] <= nums2[i]:
            nge_stack.pop()
        if nge_stack:
            ans.append(nge_stack[-1][1])
        else:
            ans.append(-1)

        nge_stack.append([nums2[i], i])
    ans.reverse()
    return ans

if __name__ == '__main__':
    print(next_greater_element([1,4,2,3], [1,4,2]))
    print(next_greater_element_r([1, 4, 2, 3], [1, 4, 2]))





