from rocket import countdown

def test_countdown_default():
    assert countdown(3) == ["3", "2", "1", "Liftoff!"]

def test_countdown_invalid():
    import pytest
    with pytest.raises(ValueError):
        countdown(-1)
