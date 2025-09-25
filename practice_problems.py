"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False

"""
A set is used because it stores unique values and lets us quickly check if an item was seen before.
Checking and inserting into a set is very fast and usually takes constant time.
This makes it simple to detect duplicates while scanning through the list once.
"""

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

from collections import deque

class TaskQueue:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if self.tasks:
            return self.tasks.popleft()
        else:
            return None

"""
A deque is used because it lets us add items at the back and remove items from the front in constant time.
This matches the way a real queue works and avoids the slow shifting that happens with normal lists.
It is efficient and easy to use for task management in order.
"""

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len(self.unique_values)

"""
A set is used because it keeps only one copy of each value and ignores repeats automatically.
Adding items and checking the size of the set are very fast operations.
This makes it a simple way to track how many unique values have appeared so far.
"""