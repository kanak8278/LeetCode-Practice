class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def prefix(strs, s, idx):
            for string in strs:
                if string[idx] == s:
                    continue
                else:
                    return ""
            return s

        pre = ""
        n = self.min_len_string(strs)
        for idx in range(n):
            s = strs[0][idx]
            sc = prefix(strs, s, idx)
            if sc == "":
                break
            else:
                pre += sc
        return pre

    def min_len_string(self, strs):
        len_strs = []
        for string in strs:
            len_strs.append(len(string))
        return min(len_strs)

