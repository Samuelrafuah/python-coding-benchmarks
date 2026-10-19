# Python Coding Benchmarks

A small learning project demonstrating coding-task design, reference solutions, automated tests, and a reproducible evaluation runner.

> **Project status:** Beginner portfolio project. It is not an official Terac project and does not claim professional or production experience.

## What it does

This repository contains three simple programming challenges:

1. Count vowels in a string.
2. Check whether text is a palindrome, ignoring spaces, punctuation, and letter case.
3. Find the missing number from a sequence containing each integer from `0` through `n` except one.

The benchmark runner checks each reference solution against defined examples and prints a pass/fail summary.

## Requirements

- Python 3.10 or newer
- No third-party packages required

## Run the benchmark

From the repository root:

```bash
python run_benchmarks.py
```

## Run the automated tests

```bash
python -m unittest discover -s tests -v
```

## Repository layout

```text
python-coding-benchmarks/
├── .github/
│   └── workflows/
│       └── tests.yml
├── src/
│   └── solutions.py
├── tests/
│   └── test_solutions.py
├── run_benchmarks.py
└── README.md
```

## How the benchmark is evaluated

Each task has inputs and expected outputs. The runner compares the actual result from the reference implementation with the expected result. The unit tests also cover edge cases such as empty strings, punctuation, and small input sequences.

A useful next improvement would be to add deliberately incorrect candidate implementations and verify that the tests catch their failures.

## Limitations and next steps

This is a small educational demonstration, not a secure sandbox for running arbitrary code. Do not use it to execute untrusted submissions. Future improvements could include:
- Separate candidate solutions from reference solutions.
- Add task metadata and difficulty labels.
- Produce JSON reports.
- Add mutation tests to check whether tests catch known bugs.
- Extend the project with TypeScript and Playwright for realistic application-level tasks.

## Author

Created as a personal learning project to practice benchmark design, testing, and code evaluation.
