from letter_combinations import letter_combinations

def test_letter_combinations():
    assert set(letter_combinations("23")) == set(["ad","ae","af","bd","be","bf","cd","ce","cf"])
    assert letter_combinations("") == []
    assert set(letter_combinations("2")) == set(["a","b","c"])
