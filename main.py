
def solution(self, nums: list[int], target: int) -> list[int]:
    val_idx = {}
    for i, num in enumerate(nums):
        if target - num in val_idx:
            return[i, val_idx[target]]
        val_idx[num] = i
        