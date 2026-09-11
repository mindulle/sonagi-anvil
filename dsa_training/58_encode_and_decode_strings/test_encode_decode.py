import pytest
from encode_decode import Codec

def test_encode_decode():
    codec = Codec()
    
    # Test case 1: normal strings
    strs1 = ["Hello", "World"]
    encoded1 = codec.encode(strs1)
    assert codec.decode(encoded1) == strs1
    
    # Test case 2: empty list
    strs2 = []
    encoded2 = codec.encode(strs2)
    assert codec.decode(encoded2) == strs2
    
    # Test case 3: empty strings in list
    strs3 = [""]
    encoded3 = codec.encode(strs3)
    assert codec.decode(encoded3) == strs3
    
    # Test case 4: strings with special characters
    strs4 = ["a#b", "c", ""]
    encoded4 = codec.encode(strs4)
    assert codec.decode(encoded4) == strs4

    # Test case 5: numbers in strings
    strs5 = ["123", "456", "7890"]
    encoded5 = codec.encode(strs5)
    assert codec.decode(encoded5) == strs5
