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


if __name__ == '__main__':
    print(max_area_container_revision([4,3,2,1,4]))