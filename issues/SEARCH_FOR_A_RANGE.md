Title: Search for a Range

Description:
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

Requirements:
- Time complexity: O(log n)
- Language: Python3 (solutions live under `Python/7. binary search/`)

Examples:
1) Input: `nums = [5,7,7,8,8,10]`, `target = 8`  -> Output: `[3,4]`
2) Input: `nums = [5,7,7,8,8,10]`, `target = 6`  -> Output: `[-1,-1]`
3) Input: `nums = []`, `target = 0`              -> Output: `[-1,-1]`

Constraints:
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is non-decreasing

Suggested labels: `algorithm`, `binary-search`, `python`, `good-first-issue`

Notes:
- Add solution file under `Python/7. binary search/` as `find_first_and_last_position.py`.
- Include unit tests and a short README snippet referencing the LeetCode problem "Find First and Last Position of Element in Sorted Array" (problem 34).

Created by automation on behalf of repository contributor.
