class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]  # add extra 0s to handle edges
        count = 0

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
        return count >= n
