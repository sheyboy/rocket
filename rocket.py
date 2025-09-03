"""Simple rocket countdown game."""

def countdown(start: int = 10) -> list[str]:
    """Return countdown messages from start down to liftoff.

    Args:
        start: Starting number of the countdown. Must be non-negative.

    Returns:
        A list of strings representing the countdown.

    Raises:
        ValueError: If ``start`` is negative.
    """
    if start < 0:
        raise ValueError("start must be non-negative")
    messages = []
    for n in range(start, 0, -1):
        messages.append(str(n))
    messages.append("Liftoff!")
    return messages

def main() -> None:
    """Run a default countdown and print messages."""
    for message in countdown():
        print(message)

if __name__ == "__main__":
    main()
