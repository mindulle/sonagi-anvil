# Anki Review - 2026-07-25

## Algorithm
- **Mutable Default Arguments**: Learned/reviewed that default arguments in Python are evaluated only once at definition time. Using mutable objects (like lists or dicts) as default arguments can lead to unintended shared state across function calls. The solution is to use `None` as the default value and initialize the mutable object inside the function body.

## System Design
- Reviewed key principles of LRU Cache (Least Recently Used) and its implementation using `OrderedDict` or a combination of `HashMap` and `DoublyLinkedList`.

## Daily Goal
- Algorithm Problem: 25_mutable_default_argument (Completed)
- Anki Review: Completed
