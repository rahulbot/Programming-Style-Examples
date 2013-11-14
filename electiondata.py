class ElectionResults:
  
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        self.file = open(self.filename, 'r')
        self.all_lines = self.file.readlines()

    def states(self):
        all_names = []
        for line in self.all_lines:
            columns = line.split(',')
            all_names.append(columns[1])
        return all_names[1:]

    def state_count(self):
        return len(self.states())