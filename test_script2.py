def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("Was it a car or a cat I saw")
    assert not is_palindrome("hello")


if __name__ == "__main__":
    test_is_palindrome()
    print("All tests passed.")
