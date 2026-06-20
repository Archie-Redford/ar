def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 6
    assert add(-1, 1) == 0


if __name__ == "__main__":
    test_add()
    print("All tests passed.")
