class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        start = math.inf
        count = 0
        indexes = []
        # print(s)
        for idx, _ in enumerate(s):
            if s[idx] != " ":
                if start > idx:
                    start = idx
                count += 1
            if s[idx] == " " or idx == len(s) - 1:
                if count != 0:
                    indexes.append((start, count))
                    # if idx == len(s)-1:
                    #     indexes.append()
                count = 0
                start = math.inf
        print(indexes)
        indexes = indexes[::-1]
        string = ""
        for idx, (x, y) in enumerate(indexes):
            string += s[x:x + y]
            if idx != len(indexes) - 1:
                string += " "
        return string

