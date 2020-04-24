from rule import Composite, Primitive, End

def test_next():
    class Sequence(Composite):
        def __init__(self, parent=None):
            super(Sequence, self).__init__(parent)
            self.add_option([ABC, DEF])
    class ABC(Composite):
        def __init__(self, parent=None):
            super(ABC, self).__init__(parent)
            self.add_option([A,B,C])
    class DEF(Composite):
        def __init__(self, parent=None):
            super(DEF, self).__init__(parent)
            self.add_option([D,E,F])
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
    """
    This stack concept needs
    some forwards and backwards
    So I guess its more of a pointer.
    """
    pointer = Sequence().next()
    print(pointer)
    assert isinstance(pointer, Primitive)
    pointer = pointer.next()
    print(pointer)
    assert isinstance(pointer, Primitive)
    pointer = pointer.next()
    print(pointer)
    assert isinstance(pointer, Primitive)
    pointer = pointer.next()
    print(pointer)
    assert isinstance(pointer, Primitive)
    pointer = pointer.next()
    print(pointer)
    assert isinstance(pointer, Primitive)
    pointer = pointer.next()
    print(pointer)
    assert isinstance(pointer, Primitive)
    pointer = pointer.next()
    print(pointer)
    assert pointer == End
    
