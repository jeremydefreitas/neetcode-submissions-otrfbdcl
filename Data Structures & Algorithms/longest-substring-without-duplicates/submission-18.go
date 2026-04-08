func lengthOfLongestSubstring(s string) int {
    mp := make(map[byte]int)
    l := 0
    res := 0

    for r := 0; r < len(s); r++{
        if idx, ok := mp[s[r]]; ok{
            l = max(idx + 1, l)
        }
        mp[s[r]] = r
        res = max(res, r - l + 1)
    }
    return res
}
