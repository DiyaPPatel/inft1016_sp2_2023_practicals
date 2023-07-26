class Coin:
    def __init__(self, name, value, year=2010):
        self.name = name
        self.value = value
        self.year = year
        
    def __str__(self):
        return f"{self.name} " + \
            f"has a value of {self.value}" + \
            f" and was made in {self.year}."

coin = Coin("Coin 1", 1.0, 2010)
print(coin)

