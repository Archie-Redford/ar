def reverse_words(s):
    return " ".join(s.split()[::-1])


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("one two three") == "three two one"
    assert reverse_words("single") == "single"


if __name__ == "__main__":
    test_reverse_words()
    print("All tests passed.")
