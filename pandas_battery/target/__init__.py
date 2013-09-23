class Target(object):
    def __init__(self, maker):
        self.maker = maker

    def __call__(self):
        return self.maker()
