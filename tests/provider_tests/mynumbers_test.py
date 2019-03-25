
from app.provider import mynumbers


def test_generate_integers_length():
    assert len(mynumbers.generate_integers(1, 10, 2)) == 5


def test_generate_integers_start_and_stop():
    nums = mynumbers.generate_integers(1, 10, 2)
    assert 1 in nums
    assert 10 not in nums


def test_generate_integers_step():
    nums = mynumbers.generate_integers(1, 10, 2)
    assert all(n in nums for n in (1, 3, 5, 7, 9))


def test_generate_integers_fail():
    assert len(mynumbers.generate_integers(1, 10, 2)) > 20
