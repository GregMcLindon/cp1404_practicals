class Guitar:
    """CP1403 guitar types class"""

    def __init__(self, name: str="", year: int=0, cost: float=0):
        """initialise a guitar type"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Used for printing guitar details"""
        return "{} ({}) : ${}".format(
            self.name, self.year, self.cost)

    def get_age(self)->int:
        """calculate age of guitar relative to the year this code was written (2017)"""
        return 2017 - self.year

    def is_vintage(self)->bool:
        return self.get_age() > 50
