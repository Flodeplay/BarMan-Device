class Beverage:
    def __init__(self, name, volume, pumps):
        self.name = name
        self.volume = volume
        self.pumps = pumps

    def getingredients(self):
        ingredients = []
        for ingredient in self.pumps:
            ingredients.append(ingredient.name)
        return ", ".join(ingredients)

