class Person():
    def __init__(self, height ,weight):
        self.height = height
        self.weight = weight
        self.imc = 0
        self.description = ''

    def from_dict(dictionary):
        height = dictionary['height']
        weight = dictionary['weight']

        p = Person(height, weight)
        return p
    
    def to_dict(self):
        d = dict()
        d['height'] = self.height
        d['weight'] = self.weight
        d['imc'] = self.imc
        d['description'] = self.description

        return d