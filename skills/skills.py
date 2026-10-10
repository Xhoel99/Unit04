""" Exercise 1 """


def is_speeding(speed, speed_limit):
    return speed > speed_limit


""" Exercise 3 """

import random


def steps(steps_walked):
    step_goal = 10000
    return steps_walked >= step_goal


""" Exercise 5 """


def calculate_speed(distance, duration):
    hours = duration / 60
    return distance / hours


def main():
    # Exercise 1 Tests
    print("--- Exercise 1 Tests ---")
    print("Car speed: 45, Limit: 65 -> Speeding:", is_speeding(45, 65))
    print("Car speed: 75, Limit: 65 -> Speeding:", is_speeding(75, 65))

    # Exercise 3 Tests
    print("\n--- Exercise 3 Tests ---")
    steps_walked = random.randint(0, 20000)
    print(f"Steps walked: {steps_walked}")
    print(f"Step goal achieved: {steps(steps_walked)}")

    # Exercise 5 Tests
    print("\n--- Exercise 5 Tests ---")
    dist = 48
    dur = 23
    speed = calculate_speed(dist, dur)
    print(f"Required speed for {dist} miles in {dur} mins: {speed:.2f} mph")


if __name__ == "__main__":
    main()