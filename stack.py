class Stack:
    def __init__(self, rule):
        # (Stack, Composite)->None
        # rule should be a parentless composite
        self.rule = rule
        self.head_list = []

    def pop(self):
        # ()-> Generator(Primitive)
        for head in self.head_list:
            yield head.next()
