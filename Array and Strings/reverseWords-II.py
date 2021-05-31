class Solution:
    def reverseWords(self, s: str) -> str:
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
        string = ""
        for idx, (x, y) in enumerate(indexes):
            # print(s[x:x+y][::-1])

            string += s[x:x + y][::-1]
            if idx != len(indexes) - 1:
                string += " "
        return string

