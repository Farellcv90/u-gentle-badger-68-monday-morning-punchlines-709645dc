"""Monday Morning Punchlines — one joke about Monday mornings.

Writes the joke to /output/entry.txt (UTF-8, 1-200 chars, no trailing
newline). The joke turns the weekend into a free trial and Monday
morning into the paywall: a fresh twist, no alarm, no coffee, no
"I hate Mondays" complaint.
"""

JOKE = "The weekend was a free trial. Monday morning is the paywall."


def load_joke():
    """Return the entry joke text."""
    return JOKE


def validate_joke(joke):
    """Check the gate: UTF-8, 1-200 chars, not only whitespace."""
    if not isinstance(joke, str):
        raise TypeError("joke must be a string")
    if not joke.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if len(joke) > 200:
        raise ValueError("joke exceeds 200 characters: %d" % len(joke))
    joke.encode("utf-8")
    return joke


def write_entry(joke, path="/output/entry.txt"):
    """Write the validated joke to path, creating parent dirs as needed."""
    import os

    validate_joke(joke)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(joke)
    return path


def main():
    joke = load_joke()
    path = write_entry(joke)
    print("Wrote %d chars to %s" % (len(joke), path))


if __name__ == "__main__":
    main()
