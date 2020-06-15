from stack import Stack
from rule import Composite, Primitive

def test_consume():
    """
    A test to take the element of the top of a stack
    """
    class Sequence(Composite):
        def __init__(self, parent=None, next_from_parent=None):
            super(Sequence, self).__init__(parent, next_from_parent)
            self.add_option([ABC, DEF])
            self.add_option([DEF])
    class ABC(Composite):
        def __init__(self, parent=None, next_from_parent=None, prior=None):
            super(ABC, self).__init__(parent, next_from_parent, prior)
            self.add_option([A,B,C])
            self.add_option([B,C])
    class DEF(Composite):
        def __init__(self, parent=None, next_from_parent=None, prior=None):
            super(DEF, self).__init__(parent, next_from_parent, prior)
            self.add_option([D,E,F])
            self.add_option([A])
            self.add_option([B, C, D])
    class A(Primitive):
        pass
    class B(Primitive):
        pass
    class C(Primitive):
        pass
    class D(Primitive):
        pass
    class E(Primitive):
        pass
    class F(Primitive):
        pass
    stack = Stack(Sequence)
    input_string = [A, B, C, D, E, F]
    accept_stack = stack.consume(input_string)
    print(accept_stack)
    assert len(accept_stack) >0
    assert all([len(row) == len(input_string) + 2 for row in accept_stack])


def test_consume_multiple_options():
    """
    A test to take the element of the top of a stack
    """
    class Sequence(Composite):
        def __init__(self, parent=None, next_from_parent=None):
            super(Sequence, self).__init__(parent, next_from_parent)
            self.add_option([ABC, DEF])
            self.add_option([DEF])
    class ABC(Composite):
        def __init__(self, parent=None, next_from_parent=None, prior=None):
            super(ABC, self).__init__(parent, next_from_parent, prior)
            self.add_option([A,B,C])
            self.add_option([B,C])
            self.add_option([A])
    class DEF(Composite):
        def __init__(self, parent=None, next_from_parent=None, prior=None):
            super(DEF, self).__init__(parent, next_from_parent, prior)
            self.add_option([D,E,F])
            self.add_option([A])
            self.add_option([B, C, D])
    class A(Primitive):
        pass
    class B(Primitive):
        pass
    class C(Primitive):
        pass
    class D(Primitive):
        pass
    class E(Primitive):
        pass
    class F(Primitive):
        pass
    stack = Stack(Sequence)
    input_string = [A, B, C, D, E, F]
    accept_stack = stack.consume(input_string)
    print(accept_stack)
    assert len(accept_stack) >0
    assert all([len(row) == len(input_string) + 2 for row in accept_stack])


