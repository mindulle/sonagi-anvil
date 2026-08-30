class Solution:
    # TODO: Fix the bug where default arguments are shared across function calls.
    def append_to_list(self, val, lst=None):
        """
        Appends a value to a list. If no list is provided, it should create a new one.
        However, the current implementation has a bug related to mutable default arguments.
        Fix the implementation.
        """
        if lst is None:
            lst = []
        lst.append(val)
        return lst
