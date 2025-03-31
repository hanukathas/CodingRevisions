def max_length_0_1(nums: list):
    hmap = {0:0} #empty sub array
    global_max = 0 #get the length
    excess = 0 #for 1, add an excess and for a 0, subtract excess. so excess = 0 for 1,0
    for i in range(len(nums)):
        if nums[i] == 1:
            excess += 1
        else:
            excess -= 1
        if excess in hmap:
            global_max = max(global_max, i+1 - hmap[excess])
        if excess in hmap:
            hmap[excess] += 1
        else:
            hmap[excess] = 1
    return global_max

if __name__ == '__main__':
    print(max_length_0_1([0, 1]))
    print(max_length_0_1([0, 1, 0]))
    print(max_length_0_1([0, 1, 1, 1]))
    print(max_length_0_1([0, 1, 1, 1, 0]))