func isPalindrome(s string) bool {

    var cleaned []rune

    for _, ch := range s {
        if unicode.IsLetter(ch) || unicode.IsDigit(ch) {
            cleaned = append(cleaned, unicode.ToLower(ch))
        }
    }    

    left := 0
    right := len(cleaned) - 1

    for left < right {
        if cleaned[left] != cleaned[right] {
            return false
        } else {
            left++
            right--
        }
    }

    return true
}
