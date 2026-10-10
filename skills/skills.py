""" Exercise 1 """

def is_speeding(speed, speed_limit):
    return speed > speed_limit

def main():
    print("--- Exercise 1 Tests ---")
    print("Car speed: 45, Limit: 65 -> Speeding:", is_speeding(45, 65))
    print("Car speed: 75, Limit: 65 -> Speeding:", is_speeding(75, 65))

if __name__ == "__main__":
    main()


""" Exercise 3 """

import random


def steps(steps_walked):
    """Returns True if steps_walked meets or exceeds 10,000 steps."""
    step_goal = 10000
    return steps_walked >= step_goal


def main():
    # Exercise 1 Manual Tests
    print("--- Exercise 1 Tests ---")
    print("Car speed: 45, Limit: 65 -> Speeding:", is_speeding(45, 65))
    print("Car speed: 75, Limit: 65 -> Speeding:", is_speeding(75, 65))

    # Exercise 3 Manual Tests
    print("\n--- Exercise 3 Tests ---")
    steps_walked = random.randint(0, 20000)
    print(f"Steps walked: {steps_walked}")
    print(f"Step goal achieved: {steps(steps_walked)}")


if __name__ == "__main__":
    main()