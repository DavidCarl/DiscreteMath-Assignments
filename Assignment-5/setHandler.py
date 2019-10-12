class setHandler():

    def __init__(self):
        pass

    # This is the Membership method
    # a is the number you want to check against a set
    # S is the set you wanna check against.
    def membership(self, a, S):
        return a in S

    # This is the Intersection method
    # S1 and S2 is the 2 sets you wanna check against each other.
    def intersection(self, S1, S2):
        return {x for x in S1 if x in S2}

    # This is the Intersection method
    # S1 and S2 is the 2 sets you wanna check against each other.
    def union(self, S1, S2):
        pass

    def difference(self, a, S):
        pass

    def complement(self, a, S):
        pass
