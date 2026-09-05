# Prompt
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Implement the `encode` and `decode` methods.

# Buggy Code
```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        return "-".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("-")
```

# Solution
The buggy code fails when the original strings contain the delimiter character `-`.
To fix this, we can encode the string by appending the length of the string followed by a delimiter (e.g. `#`) before the actual string content.

```python
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded
```

**Complexity**
- Time Complexity: O(N) where N is the total number of characters in the list of strings for both encode and decode.
- Space Complexity: O(1) for encode (ignoring the output string) and decode.

**Feedback Template**
- Did you handle strings containing the delimiter character?
- Did you consider empty lists or lists with empty strings?
