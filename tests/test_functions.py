from utilitj import bscMath

def test_sum():
    assert bscMath.sum(
        [2, 5, 3, 9, 100]
    ) == 119

def test_avg():
    assert bscMath.avg(
        [1, 1, 1, 1, 1]
    ) == 1