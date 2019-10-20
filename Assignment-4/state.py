class State:
    def __init__(self):
        self.states = {}
        self.rules = {}
        self.load_rules()

    def load_rules(self):
        with open('rules', 'r') as rules:
            for line in rules:
                line = line.strip()
                tmp = line.split(':',1)
                self.rules[tmp[0]] = tmp[1].split(',')

    def change_state(self, instance, next_state):
        if instance not in self.states:
            self.states[instance] = 0
        if str(next_state) not in self.rules[str(self.states.get(instance))]:
            raise Exception(f'{instance} Illegal Action!')
            # return False
        else:
            self.states[instance] = next_state
            # return True