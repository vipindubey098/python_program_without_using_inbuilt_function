class solution(object):
    def reverseString(self,s):
        i, j = 0, len(s)-1
        # print(len(s)-1)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)

s = solution()
print(s.reverseString(["H","e","l","l","o"]))