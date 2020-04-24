class Stack:
    def __init__(self, rule):
        # (Stack, Composite)->None
        self.rule = rule
        self.head_list = rule.next()

    def pop(self):
        # ()-> Generator(Primitive)
        for head in self.head_list:
            yield head.next()
