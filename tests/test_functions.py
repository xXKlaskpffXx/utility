from utilitj import functions

def test_sum():
    assert functions.sum(
        [2, 5, 3, 9, 100]
    ) == 119

def test_avg():
    assert functions.avg(
        [1, 1, 1, 1, 1]
    ) == 1