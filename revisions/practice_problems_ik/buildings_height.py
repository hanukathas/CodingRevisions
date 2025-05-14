def buildings_height(heights:list):
    """
    https://leetcode.com/problems/buildings-with-an-ocean-view/description/
    :param heights:
    :return:
    """
    oceans = []
    for i in range(len(heights)):
        while oceans and oceans[-1] <= heights[i]:
            oceans.pop()
        oceans.append(heights[i])
    return oceans

if __name__ == '__main__':
    print(buildings_height([4,2,1,3,13]))