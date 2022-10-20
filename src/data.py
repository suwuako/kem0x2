import datetime

class user:
    def __init__(self, before, after):
        self.before_activities = before.activities
        self.after_activities = after.activities

    def update(self):
        pass