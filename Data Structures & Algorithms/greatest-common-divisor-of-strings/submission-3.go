func gcdOfStrings(str1 string, str2 string) string {
    len1, len2 := len(str1), len(str2)

    isDivisor := func(l int) bool {
        if len1%l != 0 || len2%l != 0 {
            return false
        }
        f1, f2 := len1/l, len2/l
        sub := str1[:l]
        repeated1, repeated2 := "", ""
        for i := 0; i < f1; i++ {
            repeated1 += sub
        }
        for i := 0; i < f2; i++ {
            repeated2 += sub
        }
        return repeated1 == str1 && repeated2 == str2
    }

    minLen := len1
    if len2 < minLen {
        minLen = len2
    }
    for l := minLen; l > 0; l-- {
        if isDivisor(l) {
            return str1[:l]
        }
    }

    return ""
}