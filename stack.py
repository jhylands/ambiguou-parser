class Stack:
    def __init__(self, rule):
        # (Stack, Composite)->None
        # rule should be a parentless composite
        self.rule = rule

    def consume(self, tokens):
        head_list = self.rule().next()
        accept_stack = []
        for token in tokens:
            next_head_list = []
            accept_list = []
            for p in head_list:
                if p == token:
                    accept_list.append(p)
                    next_head_list += p.next()
            head_list = next_head_list
            accept_stack.append(accept_list)
        return accept_stack
