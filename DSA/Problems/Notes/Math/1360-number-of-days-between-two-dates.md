# LeetCode 1360 - Number of Days Between Two Dates

Pattern: Math (Date Arithmetic)

Difficulty: Easy

## Idea

Parse both date strings into datetime objects using strptime with the "%Y-%m-%d" format.

Subtract the two dates to get a timedelta, and return the absolute value of its .days attribute.

## Complexity

* Time: O(1)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. Using the standard library's datetime module avoids manually implementing calendar/leap-year logic, which would be much more error-prone.

## Recognition

Look for this pattern when you have:

* Need to compute a difference between calendar dates, accounting for varying month lengths and leap years
* A standard date/time library handles the calendar complexity reliably

## Keywords

* Math
* Date Arithmetic
* Standard Library
* Leap Year Handling

## Similar Problems

* 3622. Check Divisibility by Digit Sum and Product
* 1185. Day of the Week