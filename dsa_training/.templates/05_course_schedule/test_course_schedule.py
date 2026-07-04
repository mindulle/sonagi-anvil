import pytest
from course_schedule import canFinish

def test_can_finish_success():
    # 0 -> 1
    assert canFinish(2, [[1, 0]]) == True

def test_can_finish_cycle():
    # 0 -> 1 -> 0
    assert canFinish(2, [[1, 0], [0, 1]]) == False

def test_complex_graph_success():
    assert canFinish(5, [[1,4], [2,4], [3,1], [3,2]]) == True

def test_complex_graph_cycle():
    assert canFinish(4, [[1,0], [2,1], [3,2], [1,3]]) == False

def test_disconnected_graph():
    assert canFinish(5, [[1,0], [3,2]]) == True

def test_no_prerequisites():
    assert canFinish(3, []) == True
