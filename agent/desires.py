class Desires:
    def __init__(self):
        self.goals = []

    def add(self, goal):
        self.goals.append(goal)

    def get_all(self):
        return self.goals
