"""Reference solutions for the sample coding benchmark tasks."""


def count_vowels(text: str) -> int:
    """Return the number of English vowels (a, e, i, o, u) in text."""
    vowels = set("aeiou")
    return sum(1 for character in text.lower() if character in vowels)


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards.

    Non-alphanumeric characters are ignored, and comparison is case-insensitive.
    """
    cleaned = "".join(character.lower() for character in text if character.isalnum())
    return cleaned == cleaned[::-1]


def find_missing_number(numbers: list[int]) -> int:
    """Find the missing integer from the range 0..n.

    The input must contain distinct integers from 0 through n, with exactly
    one number missing. For example, [3, 0, 1] returns 2.
    """
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum
