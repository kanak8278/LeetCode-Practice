class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def utility(s, idx1, idx2):
            if idx1 >= idx2:
                return
            else:
                store = s[idx1]
                s[idx1] = s[idx2]
                s[idx2] = store
                idx1 += 1
                idx2 -= 1
                utility(s, idx1, idx2)

        utility(s, 0, len(s) - 1)

