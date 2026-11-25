"""Monday Morning Punchlines — one joke about Monday mornings.

The angle: the weekend was a free trial and Monday morning is the
paywall. It reframes the familiar Monday dread as a subscription
joke — the good part was never really free, and the bill arrives
with the alarm clock — instead of complaining about the day itself.

Why it works: the free-trial/paywall metaphor is a modern, relatable
frame that lands without leaning on the tired Monday clichés. There
is no alarm clock, no coffee dependency, and no flat "I hate Mondays"
complaint; the humour comes from the transaction, not from groaning
about the calendar. The punchline is the second sentence, and it
re-reads the first: "free trial" only makes sense once the paywall
shows up.

Writes the joke to /output/entry.txt (UTF-8, 1-200 chars, no trailing
newline).
"""

JOKE = "The weekend was a free trial. Monday morning is the paywall."


def load_joke():
    """Return the entry joke text."""
    return JOKE


def validate_joke(joke):
    """Check the gate: UTF-8, single line, 1-200 chars, not only whitespace.

    The entry is one punchline, so it must be exactly one line — any
    embedded newline would split the joke across lines in the output
    file. The char limit (1-200) is the competition gate; the extra
    UTF-8 byte-length check guards the same text at the encoding level
    (a 200-char entry of multi-byte characters must still fit a
    600-byte budget, i.e. 3 bytes per char worst case for the BMP).
    """
    if not isinstance(joke, str):
        raise TypeError("joke must be a string")
    if not joke.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line (no newline characters)")
    if len(joke) > 200:
        raise ValueError("joke exceeds 200 characters: %d" % len(joke))
    encoded = joke.encode("utf-8")
    if len(encoded) > 600:
        raise ValueError("joke exceeds 600 UTF-8 bytes: %d" % len(encoded))
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
