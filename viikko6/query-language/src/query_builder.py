from matchers import And, PlaysIn, HasAtLeast, All, HasFewerThan

class QueryBuilder:

    def __init__(self, query=All()):
        self.query = query

    def build(self):
        return self.query
    
    def playsIn(self, matchers):
        return QueryBuilder(And(self.query, PlaysIn(matchers)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))
    