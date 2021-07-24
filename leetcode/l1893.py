from typing import List


def isCovered(ranges: List[List[int]], left: int, right: int) -> bool:
    diff = [0] * 52
    for l, r in ranges:
        diff[l] += 1
        diff[r + 1] -= 1
    sum = 0
    for i in range (1, 51):
        sum += diff[i]
        if left <= i <= right and sum <= 0:
            return False
    return True


a = isCovered([[50,50]], 1, 50)
print(a)
