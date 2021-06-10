class Solution:
    def findCLosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        sorted_arr = sorted(arr, key=lambda num: abs(num + x), reverse=True)
        result = []
        result.extend(sorted_arr[:k])
        return sorted(result)



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    sol = Solution()
    print(sol.findCLosestElements(arr, 4, 2))
