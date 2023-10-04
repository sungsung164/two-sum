from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_gether = {}
    for i, num in enumerate(nums):
        rest = target - num
        if rest in num_gether:
            return [num_gether[rest], i]
        num_gether[num] = i
    return []