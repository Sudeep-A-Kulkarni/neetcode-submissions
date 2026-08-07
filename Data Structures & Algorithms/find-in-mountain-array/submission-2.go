/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * type MountainArray struct {
 * }
 * func (this *MountainArray) get(index int) int {}
 * func (this *MountainArray) length() int {}
 */

func findInMountainArray(target int, mountainArr *MountainArray) int {
    n := mountainArr.length()

    for i := 0; i < n; i++ {
        if mountainArr.get(i) == target {
            return i
        }
    }

    return -1
}