

class c1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"c1: {self.name}"

    def __repr__(self):
        return f"c1({self.name})"