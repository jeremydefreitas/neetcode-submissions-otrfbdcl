func maxProfit(prices []int) int {
    l := 0
    r := 1
    maxProfit := 0

    for r < len(prices){
        if prices[l] < prices[r]{
            maxProfit = max(maxProfit, (prices[r] - prices[l]))
        } else {
            l = r
        }
        r++
    }
    return maxProfit
}

func max(a, b int) int{
    if a > b{
        return a
    }
    return b
}
