def r_next_greater_element(nums1: list, nums2: list):
    greater_element_stack = []
    distance = {}
    for i in range(len(nums2)-1,-1,-1):
        while greater_element_stack and greater_element_stack[-1] <= nums2[i]:
            greater_element_stack.pop()

        if greater_element_stack:
            distance[nums2[i]] = greater_element_stack[-1]
        else:
            distance[nums2[i]] = -1
        greater_element_stack.append(nums2[i])

    return distance


if __name__ == '__main__':
    print(r_next_greater_element([4,1,2], [1,3,4,2]))

