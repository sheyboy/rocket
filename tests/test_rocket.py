import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from rocket_game import Rocket

def test_move_up_increases_altitude():
    rocket = Rocket()
    rocket.move_up()
    assert rocket.get_altitude() == 1

def test_move_up_with_amount():
    rocket = Rocket()
    rocket.move_up(5)
    assert rocket.get_altitude() == 5

def test_move_up_negative_amount():
    rocket = Rocket()
    with pytest.raises(ValueError):
        rocket.move_up(-1)
