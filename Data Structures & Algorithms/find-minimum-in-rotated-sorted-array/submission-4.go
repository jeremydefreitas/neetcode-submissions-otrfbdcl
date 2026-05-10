func findMin(nums []int) int {
    l, r := 0, len(nums) - 1
    res := nums[0]

    for l <= r {
        if nums[l] < nums[r] {
            if res > nums[l] {
                res = nums[l]
            }
            break
        }

        mid := l + (r-l)/2
        if nums[mid] < res {
            res = nums[mid]
        }
        if nums[mid] >= nums[l] {
            l = mid + 1
        } else {
            r = mid - 1
        }
    }

    return res

}
