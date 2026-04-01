class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t
        
        window = {}
        tar = {}
        

        for c in t:
            tar[c] = 1 + tar.get(c, 0)

        have, need = 0, len(tar) 
        l = 0
        res = [-1, -1]
        resLen = float("infinity")

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in tar and window[char] == tar[char]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]


                window[s[l]] -= 1
                if s[l] in tar and window[s[l]] < tar[s[l]]:
                    have -= 1
                
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""




        