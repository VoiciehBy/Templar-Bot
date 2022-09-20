class thread:

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __eq__(self, t):
        if (self.name == t.name and self.link == t.link):
            return True
        else:
            return False