class Planets:
    def __init__(self, name, size, weight, density, ratio):
        self.name = name
        self.size = size
        self.weight = weight
        self.density = density
        self.ratio = ratio

    def planet_size(self):
        return "The size of {} is {} km.".format(self.name, self.size)

    def planet_weight(self):
        return "The weight of {} is {} kg.".format(self.name, self.weight)

    def planet_density(self):
        return "The density of {} is {} g/cm³.".format(self.name, self.density)

    def calculate_your_weight(self, your_weight):
        my_weight = float(self.ratio) * float(your_weight)
        return "Your weight on {} is {} kg.".format(self.name, my_weight)
