# Akiba Technologies — Week 2 Python Tasks

## Student Information

- **Name:** Makda Solomon Gebreegziabher
- **Course:** Python Programming
- **Week:** 2
- **Repository:** [akiba-weekly-projects](https://github.com/Makda0-0/akiba-weekly-projects)
- **Week 2 folder:** [akiba-week-2-python](https://github.com/Makda0-0/akiba-weekly-projects/tree/main/akiba-week-2-python)

## Topics Covered

- Conditions (`if` / `elif` / `else`)
- Loops (`for`, `while`)
- Comparison and logical operators
- Input validation
- Computational Thinking
  - Understand
  - Break it down
  - Identify patterns
  - Design the logic
  - Implement
  - Test
  - Improve

## Completed Tasks

| #   | Task                 | File                         | Description                                                            |
| --- | -------------------- | ---------------------------- | ---------------------------------------------------------------------- |
| 1   | Even or Odd          | `task_01_even_odd.py`        | Reads a number and prints whether it is even or odd.                   |
| 2   | Largest of Three     | `task_02_largest_three.py`   | Finds the largest of three numbers using comparison operators.         |
| 3   | Prime Number Checker | `task_03_prime_checker.py`   | Determines whether a number is prime using a loop and modulo.          |
| 4   | Palindrome Checker   | `task_04_palindrome.py`      | Checks whether a word or phrase reads the same forwards and backwards. |
| 5   | Sum of Digits        | `task_05_sum_digits.py`      | Calculates the sum of all digits in a number.                          |
| 6   | FizzBuzz             | `task_06_fizzbuzz.py`        | Prints Fizz, Buzz, or FizzBuzz for numbers from 1 up to a limit.       |
| 7   | Number Guessing Game | `task_07_guessing_game.py`   | User guesses a random number between 1 and 100 with high/low hints.    |
| 8   | Count Numbers        | `task_08_count_numbers.py`   | Counts how many positives, negatives, and zeros the user enters.       |
| 9   | ATM PIN System       | `task_09_atm_pin.py`         | Simulates an ATM with a 3-attempt PIN and menu operations.             |
| 10  | Number Analyzer      | `task_10_number_analyzer.py` | Analyzes a list of numbers: count, sum, average, smallest, largest.    |

## Mini Project — Simple Bank Account System

**File:** `mini_project_bank.py`

A menu-driven bank program that demonstrates conditions, loops, and
computational thinking. Features:

- 3-attempt PIN authentication (default PIN: `1234`)
- Check balance
- Deposit money (rejects zero or negative amounts)
- Withdraw money (checks sufficient balance)
- Invalid-option handling — menu reappears
- Transaction counter (bonus challenge)

## Concepts Demonstrated

| Concept                         | Where it appears                    |
| ------------------------------- | ----------------------------------- |
| Variables                       | Every file                          |
| `input()`                       | Every file                          |
| `if` / `elif` / `else`          | Tasks 1, 2, 3, 4, 6, 8, 9, 10, bank |
| `while` loop                    | Tasks 7, 9, bank                    |
| `for` loop                      | Tasks 3, 5, 6, 8, 10                |
| Comparison operators            | Tasks 1, 2, 3, 4, 6, 8, 9, 10, bank |
| Logical operators (`and`, `or`) | Tasks 2, 6, bank                    |
| Input validation                | Task 9, bank                        |
| Computational thinking          | All tasks                           |

## Edge Cases Tested

- Even/odd: `0`, `1`, `-1`, very large numbers
- Largest of three: equal numbers, negatives, all same
- Prime: `0`, `1`, `2`, `4`, `97`, negative numbers
- Palindrome: single letter, `"racecar"`, `"hello"`, phrases with spaces
- Sum of digits: `0`, single digit, large numbers
- FizzBuzz: `1`, `5`, `15`, `100`
- Guessing game: lowest guess, highest guess, non-integer input
- Count numbers: `0` count, all positives, all negatives, mixed
- ATM PIN: correct PIN first try, correct PIN on third try, three wrong tries
- Bank: zero deposit, negative deposit, over-withdrawal, invalid menu option

## What I Learned

This week I practiced using conditional statements (`if` / `elif` / `else`)
and loops (`for` / `while`) to solve real problems. I learned how to:

1. Break a problem into smaller steps using computational thinking.
2. Validate user input so the program doesn't crash on unexpected values.
3. Test code with edge cases like `0`, `1`, negatives, and empty input.
4. Commit my work to GitHub regularly with clear, meaningful messages
   instead of one giant commit at the end.

The bank mini project helped me combine everything: a `while` loop for the
menu, `if` / `elif` / `else` for each option, input validation, and a
counter to track transactions.

## Submission
