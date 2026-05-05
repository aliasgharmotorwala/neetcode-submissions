class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def merge_sort(nums):

            if len(nums) <= 1:
                return nums

            m = len(nums) // 2
            
            left = nums[:m]
            right = nums[m:]

            merge_sort(left)
            merge_sort(right)

            l = r = i = 0

            while l < len(left) and r < len(right):
                if left[l] > right[r]:
                    nums[i] = left[l]
                    l += 1
                else:
                    nums[i] = right[r]
                    r += 1
                i += 1

            while l < len(left):
                nums[i] = left[l]
                l += 1
                i += 1

            while r < len(right):
                nums[i] = right[r]
                r += 1
                i += 1


        merge_sort(piles)

        max_k = piles[0]

        if h <= len(piles):
            return max_k

        k = 1
        min_k = max_k

        l = 1
        r = max_k

        while l <= r:
            k = (l+r)//2 # middle value
            th = h
            i = 0
            while i < len(piles):
                if piles[i] <= k:
                    th -= (len(piles) - i)
                    break
                else:
                    he = (piles[i] // k)
                    if piles[i] % k > 0:
                        he += 1
                    th -= he
                    i += 1
                if th < 0:
                    break
            if th < 0:
                l = k + 1
            if th >= 0:
                min_k = min(k, min_k)
                r = k - 1

        return min_k


        