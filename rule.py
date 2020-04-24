class Rule:
    def next(self):
        pass

class Composite:
    def __init__(self, parent=None):
        if parent is None:
            self.top_level = True
        else:
            self.top_level = False
            self.parent = parent
        # Options is a list of token sequences
        self.options = []
        self.pointers = 0

    def add_option(self, token_sequence):
        self.options.append(token_sequence)

    def next(self):
        """
        So in this run we are assuming
        len(options) == 1
        """ 
#        print("->{}: toplevel:{}, pointer: {}".format(self.__class__, self.top_level, self.pointers))
        if self.top_level and self.pointers == len(self.options[0]):
            return End
        elif self.pointers == len(self.options[0]):
            return self.parent.next()
        else:
#            print("Cl:", self.__class__, "options: ", self.options[0])
            next_object = self.options[0][self.pointers](self).next()
            self.pointers+=1
            return next_object

class Primitive:
    def __init__(self, parent):
        self.parent = parent
        self.next_call = False

    def next(self):
#        print("pr:", self.__class__, "next", self.next_call)
        if self.next_call:
            return self.parent.next()
        else:
            self.next_call = True
            return self
    def __repr__(self):
        return "<" + str(self.__class__)[-5:]

class End(Primitive):
    pass
