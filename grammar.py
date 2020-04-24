from rule import Composite, Primitive

class Sentence(Composite):
    def __init__(self):
        super(Sentence, self).__init__()
        self.add_option([
            Sentence,
            Conjunction,
            Sentence])
        self.add_option([
            NounPhrase,
            VerbPhrase])

class VerbPhrase(Composite):
    def __init__(self):
        super(Sentence, self).__init__()
        self.add_option([
            Verb])
        self.add_option([
            VerbPhrase,
            NounPhrase, # optional
            PrepositonalPrase,# optional
            Adverb]) # optional

class NounPhrase(Composite):
    def __init__(self):
        super(Sentence, self).__init__()
        self.add_option([
            Delimiter, # optional
            Adjective, # optional
            Noun,
            PrepositonalPrase]) # optional

class PrepositonalPrase(Composite):
    def __init__(self):
        super(Sentence, self).__init__()
        self.add_option([
            Prepersition,
            NounPhrase])

    
class Noun(Primitive):
    pass

class Verb(Primitive):
    pass

class Adjective(Primitive):
    pass

class Adverb(Primitive):
    pass

class Prepersition(Primitive):
    pass

class Conjunction(Primitive):
    pass

class interjection(Primitive):
    pass

class Pronoun(Primitive):
    # A class within noun?
    pass

class Delimiter(Primitive):
    pass
