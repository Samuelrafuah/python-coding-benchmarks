"""Run the example benchmark cases and print a concise report."""

from src.solutions import count_vowels, is_palindrome, find_missing_number


BENCHMARKS = [
    {
        "name": "count_vowels",
        "function": count_vowels,
        "cases": [
            ("hello", 2),
            ("AEIOU", 5),
            ("rhythm", 0),
            ("", 0),
        ],
    },
    {
        "name": "is_palindrome",
        "function": is_palindrome,
        "cases": [
            ("Race car", True),
            ("A man, a plan, a canal: Panama!", True),
            ("python", False),
            ("", True),
        ],
    },
    {
        "name": "find_missing_number",
        "function": find_missing_number,
        "cases": [
            ([3, 0, 1], 2),
            ([0, 1], 2),
            ([1], 0),
            ([], 0),
        ],
    },
]


def main() -> int:
    total = 0
    passed = 0

    for benchmark in BENCHMARKS:
        task_passed = 0
        for inputs, expected in benchmark["cases"]:
            total += 1
            actual = benchmark["function"](inputs)
            if actual == expected:
                passed += 1
                task_passed += 1
            else:
                print(
                    f"FAIL {benchmark['name']}: input={inputs!r}, "
                    f"expected={expected!r}, actual={actual!r}"
                )
        print(f"{benchmark['name']}: {task_passed}/{len(benchmark['cases'])} passed")

    print(f"\nOverall: {passed}/{total} cases passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
