def max_area_container_revision(height: list):
    left = 0
    right = len(height) - 1
    max_vol = 0
    while left < right:
        vol = (right - left)  * min(height[left], height[right])
        max_vol = max(max_vol, vol)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return max_vol

def max_area_container_revision_r(height: list):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, (right-left)*min(height[left], height[right]))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == '__main__':
    print(max_area_container_revision([1,8,6,2,5,4,8,3,7]))
    print(max_area_container_revision_r([1, 8, 6, 2, 5, 4, 8, 3, 7]))