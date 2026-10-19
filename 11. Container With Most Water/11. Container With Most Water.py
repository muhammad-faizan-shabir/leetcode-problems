class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        size = len(height)
        l = 0
        r = size - 1
        maxWater = min(height[l], height[r]) * (r - l)

        while(l < r):
            water = min(height[l], height[r]) * (r - l)
            
            if(water > maxWater):
                maxWater = water
            
            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        
        return maxWater