from src import app

def test_addition_with_positive_numbers():
    result = app.addition(1, 2, 3)
    assert result == 6

def test_addition_with_negative_numbers():
    result = app.addition(-1, 3, -2)
    assert result == 0

def test_addition_with_single_number():
    result = app.addition(-1)
    assert result == -1
