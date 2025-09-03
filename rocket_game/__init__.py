class Rocket:
    """A simple rocket that can move upward."""

    def __init__(self):
        self.altitude = 0

    def move_up(self, amount: int = 1) -> None:
        """Move the rocket up by a given amount.

        Parameters
        ----------
        amount: int, default=1
            The number of units to increase the rocket's altitude.
        """
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.altitude += amount

    def get_altitude(self) -> int:
        """Return the current altitude."""
        return self.altitude


def main() -> None:
    rocket = Rocket()
    for _ in range(10):
        rocket.move_up()
        print(f"Rocket altitude: {rocket.get_altitude()}")


if __name__ == "__main__":
    main()
