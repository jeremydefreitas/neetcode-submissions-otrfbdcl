func characterReplacement(s string, k int) int {
    res := 0
    l := 0
    maxF := 0
    count := make(map[byte]int)

    for r := 0; r < len(s); r++ {
        count[s[r]]++
        if count[s[r]] > maxF {
            maxF = count[s[r]]
        }

        if (r - l + 1) - maxF > k {
            count[s[l]]--
            l++
        }

        if res < r - l + 1 {
            res = r - l + 1
        }
    }
    return res


}
