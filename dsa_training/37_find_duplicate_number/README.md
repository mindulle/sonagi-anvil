# Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

## Solution
Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
Time Complexity: O(n)
Space Complexity: O(1)
