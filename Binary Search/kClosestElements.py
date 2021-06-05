class Solution:
    def findCLosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        sorted_arr = sorted(arr, key=lambda num: abs(num + x), reverse=True)
        return sorted_arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    sol = Solution()
    print(sol.findCLosestElements(arr, 4, 2))
