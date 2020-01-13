class Beverage:
    def __init__(self, name, pumps):
        self.name = name
        self.pumps = pumps

    def getingredients(self):
        ingredients = []
        for ingredient in self.pumps:
            ingredients.append(ingredient.name)
        return ", ".join(ingredients)

    def volume(self):
        volume = 0
        for pump in self.pumps:
            volume += int(pump.amount)
        return volume

    def caclsiszes(self):
       return {"Small": int(self.volume()/3*2), "Medium": self.volume(), "Big": int(self.volume()/2*3)}
