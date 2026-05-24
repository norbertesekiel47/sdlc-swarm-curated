"""String utility module with intentional bugs."""


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def count_vowels(s: str) -> int:
    """Count vowels in a string."""
    vowels = "aeiou"
    return sum(1 for c in s.lower() if c in vowels)


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each word."""
    return s.title()


def count_words(s: str) -> int:
    """Count the number of words in a string."""
    return len(s.split())


def remove_duplicates(s: str) -> str:
    """Remove duplicate characters from a string."""
    seen: set[str] = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return "".join(result)


def truncate(s: str, max_length: int) -> str:
    """Truncate string to max_length, adding ellipsis if truncated."""
    if len(s) <= max_length:
        return s
    return s[:max_length]  # BUG: should add "..." indicator


def is_anagram(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams."""
    return sorted(s1.lower()) == sorted(s2.lower())  # BUG: doesn't strip spaces


def slugify(s: str) -> str:
    """Convert string to URL-safe slug."""
    return s.lower().replace(" ", "-")  # BUG: doesn't remove special chars


def camel_to_snake(s: str) -> str:
    """Convert camelCase to snake_case."""
    result = []
    for i, c in enumerate(s):
        if c.isupper() and i > 0:
            result.append("_")
        result.append(c.lower())
    return "".join(result)
