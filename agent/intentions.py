class Intentions:
    def __init__(self):
        self.actions = []

    def add(self, action):
        self.actions.append(action)

    def execute_all(self):
        for action in self.actions:
            action()
