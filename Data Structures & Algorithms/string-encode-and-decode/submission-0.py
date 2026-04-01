class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for strng in strs:
            encodedStr += str(len(strng)) + '#' + strng
        return encodedStr


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            print(s[i::j])
            res.append(s[i:j])
            i = j
        return res
       

