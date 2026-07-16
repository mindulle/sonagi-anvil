class Solution:
    def append_item(self, item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items
