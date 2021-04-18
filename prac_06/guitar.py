CURRENT_YEAR = 2021
VINTAGE_YEAR = 50


class Guitar:
    """represent type of guitar"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        if CURRENT_YEAR - self.year >= VINTAGE_YEAR:
            return True
        return False
