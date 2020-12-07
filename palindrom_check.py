def is_palindrome(string):
    start_pointer = 0
    end_pointer = len(string) - 1

    while start_pointer < end_pointer:
        if string[start_pointer] == string[end_pointer]:
            start_pointer += 1
            end_pointer -= 1
        else:
            return False

    return True

print(is_palindrome("abcdefghihgfeddcba"))
print(is_palindrome("abcdcba"))
