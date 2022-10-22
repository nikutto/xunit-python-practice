def inc(x):
    return x + 1


def test_inc_2():
    assert inc(2) == 3


def test_inc_minus_1():
    assert inc(-1) == 0


def test_a():
    from app.myhello import get_message

    assert "Hello" in get_message()
