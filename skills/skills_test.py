""" Exercise 2 """

from skills import is_speeding

def test_is_speeding_true():
    assert is_speeding(75, 65) is True

def test_is_speeding_false():
    assert is_speeding(45, 65) is False

""" Exercise 4 """

import random
from skills import steps


def test_steps_goal_achieved():
    random.seed(0)  # Seed 0 produces 12,888 steps
    steps_walked = random.randint(0, 20000)
    assert steps(steps_walked) is True


def test_steps_goal_not_achieved():
    random.seed(1)  # Seed 1 produces 4,348 steps
    steps_walked = random.randint(0, 20000)
    assert steps(steps_walked) is False