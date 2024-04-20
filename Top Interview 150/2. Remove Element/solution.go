func removeElement(nums []int, val int) int {
    seen := 0
    for _, v := range nums {
        if v != val {
            nums[seen] = v
            seen++
        }
    }
    return seen
}