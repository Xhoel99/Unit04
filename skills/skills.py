""" Exercise 1 """

def is_speeding(speed, speed_limit):
    """Returns True if the car's speed is strictly greater than the speed limit."""
    return speed > speed_limit

def main():
    print("--- Exercise 1 Tests ---")
    print("Car speed: 45, Limit: 65 -> Speeding:", is_speeding(45, 65))
    print("Car speed: 75, Limit: 65 -> Speeding:", is_speeding(75, 65))

if __name__ == "__main__":
    main()