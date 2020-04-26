from rule import End

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
            if head_list == []:
                raise Exception("String left unconsumed")
            for p in head_list:
                if p == token:
                    accept_list.append(p)
                    next_head_list += p.next()
            head_list = next_head_list
            accept_stack.append(accept_list)
        accepted_states = [e for e in next_head_list if isinstance(e, End)]
        if accepted_states == []:
            raise Exception("String not accepted.")
        return [list(e.get_trace()) for e in accepted_states]
