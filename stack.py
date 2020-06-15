from rule import End

class Stack:
    def __init__(self, rule):
        # (Stack, Composite)->None
        # rule should be a parentless composite
        self.rule = rule

    def consume(self, tokens):
        head_list = self.rule().next()
        for token in tokens:
            print(":Token::", token)
            next_head_list = []
            if head_list == []:
                raise Exception("String left unconsumed")
            for p in head_list:
                print(":Prior:", p)
                if p == token:
                    next_head_list += p.next()
                print("Head->", next_head_list)
            head_list = next_head_list
        accepted_states = [e for e in next_head_list if isinstance(e, End)]
        if accepted_states == []:
            raise Exception("String not accepted.")
        return [list(e.get_trace()) for e in accepted_states]
