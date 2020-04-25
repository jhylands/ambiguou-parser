from rule import Composite, Primitive, End

def test_next():
    class Sequence(Composite):
        def __init__(self, parent=None, next_from_parent=None):
            super(Sequence, self).__init__(parent, next_from_parent)
            self.add_option([ABC, DEF])
    class ABC(Composite):
        def __init__(self, parent=None, next_from_parent=None):
            super(ABC, self).__init__(parent, next_from_parent)
            self.add_option([A,B,C])
            self.add_option([B,C])
    class DEF(Composite):
        def __init__(self, parent=None, next_from_parent=None):
            super(DEF, self).__init__(parent, next_from_parent)
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
    def next_map(xs):
        return [option for x in xs for option in x.next()]

    head_list = Sequence().next()
    print(head_list)
    assert all([isinstance(e, Primitive) for e in head_list])
    a_expand = head_list[0].next()
    print("A expand:", a_expand)
    b_expand = head_list[1].next()
    print("B expand:", b_expand)
    head_list = a_expand + b_expand
    print(head_list)
    assert all([isinstance(e, Primitive) for e in head_list])
    head_list = next_map(head_list)
    print(head_list)
    assert all([isinstance(e, Primitive) for e in head_list])
    head_list = next_map(head_list)
    print(head_list)
    assert all([isinstance(e, Primitive) for e in head_list])
    head_list = next_map(head_list)
    print(head_list)
    assert all([isinstance(e, Primitive) for e in head_list])
    head_list = next_map(head_list)
    print(head_list)
    assert all([isinstance(e, Primitive) for e in head_list])
    head_list = next_map(head_list)
    print(head_list)
    assert all([isinstance(e, Primitive) for e in head_list])
    
def test_primitive_eq():
    class Sequence(Composite):
        def __init__(self, parent=None, next_from_parent=None):
            super(Sequence, self).__init__(parent, next_from_parent)
            self.add_option([A])
    class A(Primitive):
        pass

    a = A(Sequence(), None)
    other_a = A(Sequence(), None)
    assert A==A
    assert a==a
    assert a==other_a
    assert a==A
