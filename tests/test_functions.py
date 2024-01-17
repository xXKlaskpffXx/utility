from utilitj import sum, avg

def test_sum():
    assert sum.sum(
        [2, 5, 3, 9, 100]
    ) == 119

def test_avg():
    assert avg.avg(
        [1, 1, 1, 1, 1]
    ) == 1