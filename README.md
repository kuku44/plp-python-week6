# PLP Python Week 6 Assignment

## Files

* `times_table.py` — Prints the multiplication table for a number from 1 to 10.
* `skip_counter.py` — Prints even numbers from 0 to 20 and counts down from 10 to 0.
* `loop_hospital.py` — Fixes three broken loops using `range()`, `while`, and a running total.
* `screenshots/` — Contains screenshots showing each program running.

## Off-by-One Error

An off-by-one error happens when a loop runs one time too many or one time too few because the starting or ending value is incorrect. To avoid this, remember that Python's `range()` stops before the ending number, so check the range bounds carefully. For example, use `range(1, 11)` when you need the numbers 1 through 10.
