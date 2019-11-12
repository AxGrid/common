
class Environment(object):
    def __init__(self):
        self.env = {}
        self.rules = {}

    def get(self, key, **kwargs):
        if key in self.rules:
            return self.__get(key, self.rules[key], kwargs)
        else:
            return self.env.get(key, kwargs.get("default", None))

    def __get(self, key, rules, args):
        location = rules.get("location", [key])
        