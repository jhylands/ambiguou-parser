class Rule:
    def next(self):
        pass

class Composite:
    def __init__(self, parent=None, index=None, prior=None):
        if parent is None:
            self.top_level = True
        else:
            self.top_level = False
            self.parent = parent
            self.next_index = index
        # Options is a list of token sequences
        self.options = []
        # Pointers will expand as the options are defined
        self.pointers = []

    def add_option(self, token_sequence):
        self.options.append(token_sequence)
        self.pointers.append(0)

    def next(self, prior=None):
        if prior is None:
            prior = Start(self)
        head_list = []
        for i in range(len(self.options)):
            head_list += self._next(i, prior)
        return head_list
            
    def _next(self, index, prior):
        if self.top_level and self.pointers[index] == len(self.options[index]):
            return [End(self, prior)]
        elif self.pointers[index] == len(self.options[index]):
            return self.parent._next(self.next_index, prior)
        else:
            next_option = self.options[index][self.pointers[index]]
            next_list = next_option(self, index, prior).next()
            self.pointers[index]+=1
            return next_list

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self.__class__.__name__

    def __eq__(self, other):
        return self.get_name() == other.get_name()


class Primitive:
    def __init__(self, parent, next_index, prior):
        self.next_index = next_index
        # The idea here is the primitive can be compressed
        self.parent = parent
        self.parents = [parent]
        self.next_call = False
        self.prior = prior

    def next(self):
        if self.next_call:
            return self.parent._next(self.next_index, prior=self)
        else:
            self.next_call = True
            return [self]

    def previous(self):
        return self.prior

    def get_name(self):
        return self.__class__.__name__

    def __eq__(self, other):
        if isinstance(other, Primitive):
            return self.get_name() == other.get_name()
        elif type(other) is type:
            return isinstance(self, other)

    def __repr__(self):
        return "<" + self.get_name() + self.parent.get_name() + ">"

class End(Primitive):
    def __init__(self, parent, prior):
        # The idea here is the primitive can be compressed
        self.parent = parent
        self.next_call = True
        self.prior = prior

    def next(self):
        return [self]

    def get_trace(self):
        previous = self
        while not isinstance(previous, Start): 
            print("Previous:", previous)
            print("Prior:", self.prior)
            yield previous
            previous = previous.previous()
        yield previous

class Start(Primitive):
    def __init__(self, parent):
        # The idea here is the primitive can be compressed
        self.next_call = False
        self.parent = parent

    def previous(self):
        return []

        
    def next(self):
        raise Exception("Can't call next on Start primitive")
