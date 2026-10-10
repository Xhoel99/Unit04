""" Exercise 2 """

import math
import random
from skills import calculate_speed, is_speeding, steps


def test_is_speeding_true():
    assert is_speeding(75, 65) is True


def test_is_speeding_false():
    assert is_speeding(45, 65) is False


""" Exercise 4 """


def test_steps_goal_achieved():
    random.seed(0)
    steps_walked = random.randint(0, 20000)
    assert steps(steps_walked) is True


def test_steps_goal_not_achieved():
    random.seed(1)
    steps_walked = random.randint(0, 20000)
    assert steps(steps_walked) is False


""" Exercise 5 """


def test_calculate_speed_exact():
    # 60 miles in 60 minutes = 60 mph
    result = calculate_speed(60, 60)
    assert math.isclose(result, 60.0)


def test_calculate_speed_fractional():
    # 48 miles in 23 minutes = ~125.21739130434781 mph
    result = calculate_speed(48, 23)
    expected = 125.21739130434781
    assert math.isclose(result, expected)