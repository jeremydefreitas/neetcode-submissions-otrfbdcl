func maxArea(heights []int) int {

    l := 0
    r := len(heights) - 1
    res := 0

    for l < r {
        capacity := min(heights[l], heights[r]) * (r - l)
        res = max(capacity, res)
        if heights[l] < heights[r]{
            l++
        } else {
            r--
        }
        
    }

    return res

}

func min(a, b int) int {
    if a < b{
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b{
        return a
    }
    return b
}
