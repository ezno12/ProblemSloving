# LeetCode 181 - Employees Earning More Than Their Managers

Pattern: Database (SQL Self-Join)

Difficulty: Easy

## Idea

Self-join the Employee table with itself: one alias (e) represents the employee, and another alias (m) represents their manager, joined on e.managerId = m.id.

Filter the joined rows to only those where the employee's salary is greater than their manager's salary, and select the employee's name.

## Complexity

* Time: Depends on the database engine's join implementation, typically O(n log n) or O(n) with proper indexing
* Space: Depends on the engine

## Mistakes

* Solved cleanly on the first accepted attempt. Self-joins (joining a table to itself with two aliases) are the standard technique whenever a row needs to be compared against another row in the SAME table via a foreign-key-like relationship.

## Recognition

Look for this pattern when you have:

* A single table where rows reference other rows in the same table (e.g., an employee referencing their manager, also an employee)
* Need to compare a row's attributes against the referenced row's attributes

## Keywords

* Database
* SQL
* Self-Join
* Filtering

## Similar Problems

* 197. Rising Temperature
* 175. Combine Two Tables
* 196. Delete Duplicate Emails