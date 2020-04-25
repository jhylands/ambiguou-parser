from stack import Stack
from rule import Composite, Primitive

def test_pop():
    """
    A test to take the element of the top of a stack
    """
    stack = Stack(rule)
    for p in stack.pop():
        assert isinstance(p, Primitive)



