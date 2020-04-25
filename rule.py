class Rule:
    def next(self):
        pass

class Composite:
    def __init__(self, parent=None, parent_next=None):
        if parent is None:
            self.top_level = True
        else:
            self.top_level = False
            self.parent = parent
            self.next_from_parent = parent_next
        # Options is a list of token sequences
        self.options = []
        # Pointers will expand as the options are defined
        self.pointers = []

    def add_option(self, token_sequence):
        self.options.append(token_sequence)
        self.pointers.append(0)

    def next(self):
        head_list = []
        for i in range(len(self.options)):
            head_list += self._next(i)
        return head_list
            
    def _next(self, index):
        """
        So in this run we are assuming
        len(options) == 1
        """ 
        if self.top_level and self.pointers[index] == len(self.options[index]):
            return [End(self, None)]
        elif self.pointers[index] == len(self.options[index]):
            return self.next_from_parent()
        else:
            next_option = self.options[index][self.pointers[index]]
            next_from_self = lambda:self._next(index)
            print(next_option)
            next_list = next_option(self, next_from_self).next()
            self.pointers[index]+=1
            return next_list

    def __str__(self):
        return str(self.__class__)


class Primitive:
    def __init__(self, parent, next_function):
        self.next_from_parent = next_function
        # The idea here is the primitive can be compressed
        self.parent = parent
        self.parents = [parent]
        self.next_call = False

    def next(self):
#        print("pr:", self.__class__, "next", self.next_call)
        if self.next_call:
            return self.next_from_parent()
        else:
            self.next_call = True
            return [self]
    def __repr__(self):
        return "<" + str(self.__class__)[36:-2] + str(self.parent)[36:-2] + ">"

class End(Primitive):
    def next(self):
        return [self]
    
    def __repr__(self):
        return "<END" + str(self.parent)[36:-2] + ">"
